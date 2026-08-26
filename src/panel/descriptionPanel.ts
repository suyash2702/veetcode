import * as vscode from 'vscode';
import { Language, Problem, RunSummary, TestResult } from '../problems/types';
import { describe } from '../problems/generated';
import { EDITORIAL_UNLOCK_AT, ProblemProgress } from '../storage/progress';
import { escapeHtml, renderMarkdown } from './markdown';

export interface PanelCallbacks {
  onRun: (slug: string, mode: 'sample' | 'submit') => void;
  onReset: (slug: string) => void;
  onOpenEditor: (slug: string) => void;
  onChangeLanguage: (slug: string, language: Language) => void;
  onOpenSupport: () => void;
}

/** Single reusable webview showing the statement, examples and last run. */
export class DescriptionPanel {
  private panel?: vscode.WebviewPanel;
  private current?: Problem;
  private currentLanguage: Language = 'python';
  private lastSummary?: RunSummary;
  /** Set when the editorial should open as soon as the webview is ready. */
  private pendingEditorial = false;

  constructor(
    private readonly extensionUri: vscode.Uri,
    private readonly callbacks: PanelCallbacks
  ) {}

  get activeSlug(): string | undefined {
    return this.current?.slug;
  }

  show(problem: Problem, progress: ProblemProgress, language: Language, preserveFocus = true): void {
    const column = vscode.ViewColumn.Beside;
    if (!this.panel) {
      this.panel = vscode.window.createWebviewPanel('veetcode.description', problem.title, { viewColumn: column, preserveFocus }, {
        enableScripts: true,
        retainContextWhenHidden: true,
        localResourceRoots: [vscode.Uri.joinPath(this.extensionUri, 'media')],
      });
      this.panel.iconPath = vscode.Uri.joinPath(this.extensionUri, 'media', 'icon.svg');
      this.panel.onDidDispose(() => {
        this.panel = undefined;
        this.current = undefined;
      });
      this.panel.webview.onDidReceiveMessage((message) => this.handleMessage(message));
    }

    if (this.current?.slug !== problem.slug) {
      this.lastSummary = undefined;
    }
    this.current = problem;
    this.currentLanguage = language;
    this.panel.title = `${problem.id}. ${problem.title}`;
    this.panel.webview.html = this.render(problem, progress);
    this.panel.reveal(column, preserveFocus);
  }

  /** Re-renders the results section for the problem currently on screen. */
  showResults(summary: RunSummary): void {
    this.lastSummary = summary;
    if (this.panel && this.current?.slug === summary.problemSlug) {
      this.panel.webview.postMessage({ type: 'results', html: this.renderResults(summary) });
    }
  }

  /**
   * Opens the editorial section. A freshly rendered webview may not be
   * listening yet, so the request is replayed when it announces itself.
   */
  revealEditorial(): void {
    this.pendingEditorial = true;
    void this.panel?.webview.postMessage({ type: 'editorial' });
  }

  setRunning(slug: string, running: boolean): void {
    if (this.panel && this.current?.slug === slug) {
      this.panel.webview.postMessage({ type: 'running', running });
    }
  }

  dispose(): void {
    this.panel?.dispose();
  }

  private handleMessage(message: { type: string; mode?: 'sample' | 'submit'; language?: Language }): void {
    const slug = this.current?.slug;
    if (!slug) {
      return;
    }
    if (message.type === 'ready') {
      if (this.lastSummary?.problemSlug === slug) {
        void this.panel?.webview.postMessage({ type: 'results', html: this.renderResults(this.lastSummary) });
      }
      if (this.pendingEditorial) {
        this.pendingEditorial = false;
        void this.panel?.webview.postMessage({ type: 'editorial' });
      }
      return;
    }
    if (message.type === 'run') {
      this.callbacks.onRun(slug, message.mode ?? 'sample');
    } else if (message.type === 'reset') {
      this.callbacks.onReset(slug);
    } else if (message.type === 'open') {
      this.callbacks.onOpenEditor(slug);
    } else if (message.type === 'language' && message.language) {
      this.callbacks.onChangeLanguage(slug, message.language);
    } else if (message.type === 'support') {
      this.callbacks.onOpenSupport();
    }
  }

  private render(problem: Problem, progress: ProblemProgress): string {
    const webview = this.panel!.webview;
    const cssUri = webview.asWebviewUri(vscode.Uri.joinPath(this.extensionUri, 'media', 'panel.css'));
    const jsUri = webview.asWebviewUri(vscode.Uri.joinPath(this.extensionUri, 'media', 'panel.js'));
    const nonce = makeNonce();

    const samples = problem.tests.filter((t) => t.sample);
    const examples = samples
      .map(
        (test, i) => `
        <div class="example">
          <div class="example-title">Example ${i + 1}</div>
          <div class="kv"><span>Input</span><code>${escapeHtml(formatInput(problem, test.input))}</code></div>
          <div class="kv"><span>Output</span><code>${escapeHtml(json(test.output))}</code></div>
          ${test.explanation ? `<div class="kv"><span>Why</span><span>${escapeHtml(test.explanation)}</span></div>` : ''}
        </div>`
      )
      .join('');

    const hints = (problem.hints ?? [])
      .map((hint, i) => `<details class="hint"><summary>Hint ${i + 1}</summary><div>${renderMarkdown(hint)}</div></details>`)
      .join('');

    const statusLabel =
      progress.status === 'solved'
        ? `Solved${progress.attempts ? ` in ${progress.attempts} attempt(s)` : ''}`
        : progress.status === 'attempted'
          ? `Attempted ${progress.attempts}x`
          : 'Not started';

    return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src ${webview.cspSource}; script-src 'nonce-${nonce}';" />
<link rel="stylesheet" href="${cssUri}" />
<title>${escapeHtml(problem.title)}</title>
</head>
<body class="difficulty-${problem.difficulty.toLowerCase()}">
  <header>
    <h1>${problem.id}. ${escapeHtml(problem.title)}</h1>
    <div class="meta">
      <span class="badge difficulty">${problem.difficulty}</span>
      ${problem.tags.map((t) => `<span class="badge tag">${escapeHtml(t)}</span>`).join('')}
      <span class="badge status status-${progress.status}">${escapeHtml(statusLabel)}</span>
    </div>
  </header>

  <div class="toolbar">
    <button id="run" class="primary">Run Samples</button>
    <button id="submit">Submit</button>
    <button id="open">Open Editor</button>
    <button id="reset" class="ghost">Reset Code</button>
    <label class="lang" for="language">Language
      <select id="language">
        ${LANGUAGES.map(
          (l) => `<option value="${l.id}"${l.id === this.currentLanguage ? ' selected' : ''}>${l.label}</option>`
        ).join('')}
      </select>
    </label>
  </div>

  <section class="statement">${renderMarkdown(problem.description)}</section>

  <section class="examples">${examples}</section>

  <section class="signature">
    <div class="kv"><span>Function</span><code>${escapeHtml(problem.functionName)}(${escapeHtml(problem.params.join(', '))})</code></div>
    <div class="kv"><span>Language</span><span>${escapeHtml(LANGUAGES.find((l) => l.id === this.currentLanguage)?.label ?? this.currentLanguage)}</span></div>
    ${problem.complexity ? `<div class="kv"><span>Target</span><code>${escapeHtml(problem.complexity)}</code></div>` : ''}
    <div class="kv"><span>Tests</span><span>${samples.length} sample, ${problem.tests.length} total</span></div>
  </section>

  ${hints ? `<section class="hints"><h3>Hints</h3>${hints}</section>` : ''}

  ${this.renderEditorial(problem, progress)}

  <section id="results">${this.lastSummary ? this.renderResults(this.lastSummary) : '<div class="empty">Run the samples to see results here. No tab switching required.</div>'}</section>

  <footer class="support">
    <span>Offline, ad-free, and nobody is selling your submissions.</span>
    <button id="support" class="ghost">Buy me a coffee ☕</button>
  </footer>

  <script nonce="${nonce}" src="${jsUri}"></script>
</body>
</html>`;
  }

  /**
   * Locked until the problem has actually been fought with. Reaching for the
   * answer on the first failure is the habit this whole extension exists to break.
   */
  private renderEditorial(problem: Problem, progress: ProblemProgress): string {
    if (!problem.editorial) {
      return '';
    }
    const failed = progress.failedSubmits ?? 0;
    const unlocked = progress.status === 'solved' || failed >= EDITORIAL_UNLOCK_AT;

    if (!unlocked) {
      const left = EDITORIAL_UNLOCK_AT - failed;
      return `<section class="editorial locked">
        <h3>Editorial 🔒</h3>
        <p>Unlocks after <strong>${EDITORIAL_UNLOCK_AT} failed submits</strong> — or the moment you solve it.
        You are at <strong>${failed}/${EDITORIAL_UNLOCK_AT}</strong>, so ${left} more honest attempt${left === 1 ? '' : 's'} to go.</p>
        <p class="muted">No tab to open, no chatbot to ask. The struggle is the feature.</p>
      </section>`;
    }

    const editorial = problem.editorial;
    const language = editorial.code[this.currentLanguage] ? this.currentLanguage : 'python';
    const code = editorial.code[language];
    const label = LANGUAGES.find((l) => l.id === language)?.label ?? language;

    return `<section class="editorial">
      <details id="editorial-details"${progress.status === 'solved' ? '' : ' open'}>
        <summary>Editorial — how it is meant to be done</summary>
        <div class="editorial-body">
          ${renderMarkdown(editorial.explanation)}
          ${editorial.complexity ? `<div class="kv"><span>Complexity</span><code>${escapeHtml(editorial.complexity)}</code></div>` : ''}
          ${code ? `<div class="kv"><span>Reference</span><span>${escapeHtml(label)}</span></div>
          <pre class="code"><code>${escapeHtml(code)}</code></pre>` : ''}
        </div>
      </details>
    </section>`;
  }

  private renderResults(summary: RunSummary): string {
    if (summary.compileError) {
      return `<div class="verdict fail">Error before any test ran</div>
        <pre class="trace">${escapeHtml(summary.compileError)}</pre>`;
    }

    const allPassed = summary.passed === summary.total && summary.total > 0;
    const header = `<div class="verdict ${allPassed ? 'pass' : 'fail'}">
        ${allPassed ? 'Accepted' : 'Wrong Answer'} — ${summary.passed}/${summary.total} ${summary.mode === 'sample' ? 'sample' : 'hidden'} tests passed
        <span class="timing">${summary.totalMs} ms</span>
      </div>`;

    const cases = summary.results
      .map((r) => this.renderCase(r))
      .join('');

    return header + `<div class="cases">${cases}</div>`;
  }

  private renderCase(result: TestResult): string {
    const open = result.passed ? '' : ' open';
    const status = result.passed ? 'pass' : 'fail';
    const label = result.error ? 'Runtime error' : result.passed ? 'Passed' : 'Failed';
    return `<details class="case ${status}"${open}>
      <summary><span class="dot"></span>Case ${result.index + 1} — ${label}<span class="timing">${result.runtimeMs} ms</span></summary>
      <div class="kv"><span>Input</span><code>${escapeHtml(this.current ? formatInput(this.current, result.input) : json(result.input))}</code></div>
      <div class="kv"><span>Expected</span><code>${escapeHtml(json(result.expected))}</code></div>
      ${result.error ? '' : `<div class="kv"><span>Actual</span><code>${escapeHtml(json(result.actual))}</code></div>`}
      ${result.stdout ? `<div class="kv"><span>Stdout</span><pre class="trace">${escapeHtml(result.stdout)}</pre></div>` : ''}
      ${result.error ? `<pre class="trace">${escapeHtml(result.error)}</pre>` : ''}
    </details>`;
  }
}

/** Languages offered in the panel picker; must stay in sync with the runners. */
const LANGUAGES: { id: Language; label: string }[] = [
  { id: 'python', label: 'Python' },
  { id: 'javascript', label: 'JavaScript' },
];

/**
 * Design problems are driven by an operation log rather than one call, so they
 * read far better as `LRUCache(2); put(1, 1); get(1)` than as two raw arrays.
 */
function formatInput(problem: Problem, input: unknown[]): string {
  if (problem.design && Array.isArray(input[0]) && Array.isArray(input[1])) {
    const ops = input[0] as string[];
    const args = input[1] as unknown[][];
    const calls = ops.map((op, i) => `${op}(${(args[i] ?? []).map((a) => json(a)).join(', ')})`);
    const shown = calls.slice(0, 12).join('; ');
    return calls.length > 12 ? `${shown}; … (${calls.length} calls)` : shown;
  }
  return input.map((value, i) => `${problem.params[i] ? `${problem.params[i]} = ` : ''}${json(value)}`).join(', ');
}

function json(value: unknown): string {
  return describe(value);
}

function makeNonce(): string {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let out = '';
  for (let i = 0; i < 32; i++) {
    out += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return out;
}
