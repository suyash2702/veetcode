import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';
import { Language, Problem } from '../problems/types';

export const EXTENSIONS: Record<Language, string> = {
  python: 'py',
  javascript: 'js',
};

export const LANGUAGE_IDS: Record<Language, string> = {
  python: 'python',
  javascript: 'javascript',
};

/** Owns where solution files live and how a file maps back to a problem. */
export class SolutionWorkspace {
  constructor(private readonly fallbackRoot: string) {}

  /** Root directory that holds one folder per attempted problem. */
  root(): string {
    const folders = vscode.workspace.workspaceFolders;
    const sub = vscode.workspace.getConfiguration('veetcode').get<string>('workspaceFolder', 'veetcode');
    if (folders && folders.length > 0) {
      return path.join(folders[0].uri.fsPath, sub);
    }
    // No folder open: keep solutions in the extension's global storage.
    return path.join(this.fallbackRoot, sub);
  }

  problemDir(problem: Problem): string {
    return path.join(this.root(), `${String(problem.id).padStart(3, '0')}-${problem.slug}`);
  }

  solutionPath(problem: Problem, language: Language): string {
    return path.join(this.problemDir(problem), `solution.${EXTENSIONS[language]}`);
  }

  /** Creates the solution file from starter code if it does not exist yet. */
  ensureSolutionFile(problem: Problem, language: Language, overwrite = false): string {
    const file = this.solutionPath(problem, language);
    if (overwrite || !fs.existsSync(file)) {
      fs.mkdirSync(path.dirname(file), { recursive: true });
      fs.writeFileSync(file, this.starterFor(problem, language), 'utf8');
    }
    return file;
  }

  private starterFor(problem: Problem, language: Language): string {
    const starter = problem.starter[language];
    if (starter) {
      return starter.endsWith('\n') ? starter : starter + '\n';
    }
    const comment = language === 'python' ? '#' : '//';
    return `${comment} No starter code bundled for ${language}. Define ${problem.functionName}(${problem.params.join(', ')}).\n`;
  }

  /** Reverses solutionPath: given an open file, which problem is it for? */
  identify(file: string): { slug: string; language: Language } | undefined {
    const ext = path.extname(file).slice(1);
    const language = (Object.keys(EXTENSIONS) as Language[]).find((l) => EXTENSIONS[l] === ext);
    if (!language) {
      return undefined;
    }
    const dir = path.basename(path.dirname(file));
    const match = /^\d+-(.+)$/.exec(dir);
    if (!match) {
      return undefined;
    }
    // Only treat it as a solution file if it sits under the configured root.
    const rel = path.relative(this.root(), file);
    if (rel.startsWith('..') || path.isAbsolute(rel)) {
      return undefined;
    }
    return { slug: match[1], language };
  }
}
