import { spawn } from 'child_process';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import * as vscode from 'vscode';
import { Language, Problem, RunSummary, TestResult } from '../problems/types';

const RESULT_PREFIX = '__VEETCODE_RESULT__';

interface HarnessOutput {
  results: Array<Omit<TestResult, 'input' | 'expected'>>;
  compileError?: string | null;
}

export class TestRunner {
  constructor(private readonly runnersDir: string) {}

  async run(
    problem: Problem,
    language: Language,
    solutionPath: string,
    mode: 'sample' | 'submit',
    token?: vscode.CancellationToken
  ): Promise<RunSummary> {
    const config = vscode.workspace.getConfiguration('veetcode');
    const timeoutMs = config.get<number>('testTimeoutMs', 10000);
    const tests = mode === 'sample' ? problem.tests.filter((t) => t.sample) : problem.tests;

    const payload = {
      solutionPath,
      functionName: problem.functionName,
      paramTypes: problem.paramTypes ?? [],
      returnType: problem.returnType ?? 'json',
      checkArg: problem.checkArg ?? null,
      compare: problem.compare ?? 'exact',
      design: problem.design ?? null,
      prepare: problem.prepare ?? null,
      timeoutMs,
      tests: tests.map((t) => ({ input: t.input, output: t.output })),
    };

    const payloadFile = path.join(os.tmpdir(), `veetcode-${problem.slug}-${Date.now()}.json`);
    fs.writeFileSync(payloadFile, JSON.stringify(payload), 'utf8');

    const { command, args } = this.commandFor(language, payloadFile, config);
    const started = Date.now();

    try {
      const raw = await this.spawn(command, args, path.dirname(solutionPath), timeoutMs, token);
      const output = this.parse(raw);
      const results: TestResult[] = output.results.map((r) => ({
        ...r,
        input: tests[r.index]?.input ?? [],
        expected: tests[r.index]?.output,
      }));
      return {
        problemSlug: problem.slug,
        language,
        mode,
        results,
        passed: results.filter((r) => r.passed).length,
        total: tests.length,
        totalMs: Date.now() - started,
        compileError: output.compileError ?? undefined,
      };
    } finally {
      fs.rmSync(payloadFile, { force: true });
    }
  }

  private commandFor(
    language: Language,
    payloadFile: string,
    config: vscode.WorkspaceConfiguration
  ): { command: string; args: string[] } {
    if (language === 'python') {
      return {
        command: config.get<string>('pythonPath', 'python3'),
        args: [path.join(this.runnersDir, 'harness.py'), payloadFile],
      };
    }
    return {
      command: config.get<string>('nodePath', 'node'),
      args: [path.join(this.runnersDir, 'harness.js'), payloadFile],
    };
  }

  private spawn(
    command: string,
    args: string[],
    cwd: string,
    timeoutMs: number,
    token?: vscode.CancellationToken
  ): Promise<{ stdout: string; stderr: string; code: number | null; timedOut: boolean }> {
    return new Promise((resolve, reject) => {
      const child = spawn(command, args, { cwd, env: { ...process.env, PYTHONIOENCODING: 'utf-8' } });
      let stdout = '';
      let stderr = '';
      let timedOut = false;

      // The harness runs every case in one process, so the budget covers the whole batch.
      const timer = setTimeout(() => {
        timedOut = true;
        child.kill('SIGKILL');
      }, timeoutMs + 2000);

      const cancel = token?.onCancellationRequested(() => child.kill('SIGKILL'));

      child.stdout.on('data', (d) => (stdout += d.toString()));
      child.stderr.on('data', (d) => (stderr += d.toString()));
      child.on('error', (err) => {
        clearTimeout(timer);
        cancel?.dispose();
        reject(new Error(`could not start "${command}": ${err.message}`));
      });
      child.on('close', (code) => {
        clearTimeout(timer);
        cancel?.dispose();
        resolve({ stdout, stderr, code, timedOut });
      });
    });
  }

  private parse(raw: { stdout: string; stderr: string; code: number | null; timedOut: boolean }): HarnessOutput {
    const line = raw.stdout.split('\n').find((l) => l.startsWith(RESULT_PREFIX));
    if (line) {
      return JSON.parse(line.slice(RESULT_PREFIX.length)) as HarnessOutput;
    }
    if (raw.timedOut) {
      return {
        results: [],
        compileError: 'Timed out. Your solution ran longer than veetcode.testTimeoutMs (likely an infinite loop).',
      };
    }
    const detail = (raw.stderr || raw.stdout).trim();
    return {
      results: [],
      compileError: detail || `Test process exited with code ${raw.code} and produced no output.`,
    };
  }
}
