import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';
import { DescriptionPanel } from './panel/descriptionPanel';
import { PlaylistBank } from './playlists/loader';
import { describe } from './problems/generated';
import { ProblemBank } from './problems/loader';
import { Difficulty, Language, Problem, RunSummary } from './problems/types';
import { TestRunner } from './runner/runner';
import { DailyStore } from './storage/daily';
import { EDITORIAL_UNLOCK_AT, ProgressStore, Status } from './storage/progress';
import { SolutionWorkspace } from './storage/workspace';
import { DailyTreeProvider } from './tree/dailyTree';
import { GroupBy, ProblemTreeProvider } from './tree/problemTree';
import { StatsTreeProvider } from './tree/statsTree';

const LANGUAGE_LABELS: Record<Language, string> = { python: 'Python', javascript: 'JavaScript' };

/** Tip jar, opened from the description panel and the command palette. */
const SUPPORT_URL = 'https://buymeacoffee.com/suyash2702';

export function activate(context: vscode.ExtensionContext): void {
  const output = vscode.window.createOutputChannel('VeetCode');
  const bundledProblems = path.join(context.extensionPath, 'problems');
  const bundledPlaylists = path.join(context.extensionPath, 'playlists');
  const runnersDir = path.join(context.extensionPath, 'runners');

  const workspace = new SolutionWorkspace(context.globalStorageUri.fsPath);
  const bank = new ProblemBank([bundledProblems, path.join(workspace.root(), 'problems')]);
  const playlists = new PlaylistBank([bundledPlaylists, path.join(workspace.root(), 'playlists')]);
  const progress = new ProgressStore(context.globalState);
  const daily = new DailyStore(context.globalState);
  const runner = new TestRunner(runnersDir);

  if (bank.errors().length) {
    output.appendLine(`Skipped ${bank.errors().length} problem file(s):`);
    bank.errors().forEach((e) => output.appendLine(`  ${e}`));
  }
  if (playlists.errors().length) {
    output.appendLine(`Skipped ${playlists.errors().length} playlist file(s):`);
    playlists.errors().forEach((e) => output.appendLine(`  ${e}`));
  }

  const tree = new ProblemTreeProvider(bank, progress, playlists);
  const stats = new StatsTreeProvider(bank, progress, playlists, () => tree.activePlaylist());
  const dailyStats = new DailyTreeProvider(daily);
  const panel = new DescriptionPanel(context.extensionUri, {
    onRun: (slug, mode) => void runProblem(slug, mode),
    onReset: (slug) => void resetSolution(slug),
    onOpenEditor: (slug) => void openProblem(slug, false),
    onChangeLanguage: (slug, language) => void switchLanguage(language, slug),
    onOpenSupport: () => void vscode.env.openExternal(vscode.Uri.parse(SUPPORT_URL)),
  });

  const treeView = vscode.window.createTreeView('veetcode.problems', { treeDataProvider: tree, showCollapseAll: true });
  const statsView = vscode.window.createTreeView('veetcode.stats', { treeDataProvider: stats });
  const dailyView = vscode.window.createTreeView('veetcode.daily', { treeDataProvider: dailyStats });

  const ACTIVE_PLAYLIST_KEY = 'veetcode.activePlaylist';

  /** Puts the selected sheet and its completion in the Problems view title. */
  function updatePlaylistTitle(): void {
    const active = tree.activePlaylist();
    if (!active) {
      treeView.description = `${bank.all().length} problems`;
      return;
    }
    const solved = active.problems.filter((p) => progress.get(p.slug).status === 'solved').length;
    treeView.description =
      `${active.playlist.name} · ${solved}/${active.problems.length}` +
      (active.missing ? ` (+${active.missing} soon)` : '');
  }

  async function selectPlaylist(id: string | undefined): Promise<void> {
    tree.setPlaylist(id);
    await context.globalState.update(ACTIVE_PLAYLIST_KEY, id);
    stats.refresh();
    updatePlaylistTitle();
  }

  function updateDailyTitle(): void {
    const summary = daily.summary();
    dailyView.description = summary.streak
      ? `${summary.today.solved} today · ${summary.streak}d streak`
      : `${summary.today.solved} today`;
  }
  progress.onDidChange(() => {
    updatePlaylistTitle();
  });
  daily.onDidChange(() => updateDailyTitle());

  const statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
  statusBar.command = 'veetcode.runTests';

  const languageBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 99);
  languageBar.command = 'veetcode.changeLanguage';
  languageBar.tooltip = 'VeetCode: change solution language';

  progress.onDidChange(() => tree.refresh());

  // ---------------------------------------------------------------- helpers

  function currentLanguage(): Language {
    return vscode.workspace.getConfiguration('veetcode').get<Language>('language', 'python');
  }

  /** Problem implied by the active editor, falling back to the open panel. */
  function activeProblem(): { problem: Problem; language: Language } | undefined {
    const editor = vscode.window.activeTextEditor;
    if (editor) {
      const identified = workspace.identify(editor.document.uri.fsPath);
      const problem = identified && bank.get(identified.slug);
      if (identified && problem) {
        return { problem, language: identified.language };
      }
    }
    const slug = panel.activeSlug;
    const fallback = slug ? bank.get(slug) : undefined;
    return fallback ? { problem: fallback, language: currentLanguage() } : undefined;
  }

  function updateContext(): void {
    const editor = vscode.window.activeTextEditor;
    const identified = editor ? workspace.identify(editor.document.uri.fsPath) : undefined;
    const problem = identified ? bank.get(identified.slug) : undefined;
    void vscode.commands.executeCommand('setContext', 'veetcode.isSolutionFile', Boolean(problem));
    if (problem) {
      const entry = progress.get(problem.slug);
      statusBar.text = `$(${entry.status === 'solved' ? 'pass-filled' : 'beaker'}) VeetCode: ${problem.title}`;
      statusBar.tooltip = 'Run sample tests';
      statusBar.show();
      languageBar.text = `$(code) ${LANGUAGE_LABELS[identified?.language ?? currentLanguage()]}`;
      languageBar.show();
    } else {
      statusBar.hide();
      languageBar.hide();
    }
  }

  /**
   * Makes `language` the active one and reopens `slug` in it. The old solution
   * file is left alone — switching back finds it untouched.
   */
  async function switchLanguage(language: Language, slug?: string): Promise<void> {
    await vscode.workspace.getConfiguration('veetcode').update('language', language, vscode.ConfigurationTarget.Global);
    const target = slug ?? activeProblem()?.problem.slug;
    if (!target) {
      void vscode.window.showInformationMessage(`VeetCode: new solutions will be scaffolded in ${LANGUAGE_LABELS[language]}.`);
      updateContext();
      return;
    }
    const problem = bank.get(target);
    if (!problem) {
      return;
    }
    const file = workspace.ensureSolutionFile(problem, language);
    const document = await vscode.workspace.openTextDocument(file);
    await vscode.window.showTextDocument(document, { viewColumn: vscode.ViewColumn.One, preview: false });
    if (panel.activeSlug === target) {
      panel.show(problem, progress.get(target), language);
    }
    updateContext();
  }

  async function openProblem(slug: string, revealPanel = true): Promise<void> {
    const problem = bank.get(slug);
    if (!problem) {
      void vscode.window.showErrorMessage(`VeetCode: unknown problem "${slug}".`);
      return;
    }
    const language = currentLanguage();
    const file = workspace.ensureSolutionFile(problem, language);
    const document = await vscode.workspace.openTextDocument(file);
    await vscode.window.showTextDocument(document, { viewColumn: vscode.ViewColumn.One, preview: false });
    await progress.markOpened(slug);

    const openPanel = vscode.workspace.getConfiguration('veetcode').get<boolean>('openDescriptionOnOpen', true);
    if (revealPanel && openPanel) {
      panel.show(problem, progress.get(slug), language);
    }
    tree.refresh();
  }

  async function resetSolution(slug: string): Promise<void> {
    const problem = bank.get(slug);
    if (!problem) {
      return;
    }
    const language = currentLanguage();
    const file = workspace.solutionPath(problem, language);
    const choice = await vscode.window.showWarningMessage(
      `Overwrite ${path.basename(file)} with the starter code for "${problem.title}"? Your current solution will be lost.`,
      { modal: true },
      'Reset'
    );
    if (choice !== 'Reset') {
      return;
    }
    workspace.ensureSolutionFile(problem, language, true);
    const document = await vscode.workspace.openTextDocument(file);
    await vscode.window.showTextDocument(document, { viewColumn: vscode.ViewColumn.One, preview: false });
  }

  async function runProblem(slug: string, mode: 'sample' | 'submit'): Promise<void> {
    const problem = bank.get(slug);
    if (!problem) {
      return;
    }
    const language = activeProblem()?.problem.slug === slug ? activeProblem()!.language : currentLanguage();
    const file = workspace.solutionPath(problem, language);

    if (!fs.existsSync(file)) {
      workspace.ensureSolutionFile(problem, language);
    }
    // Tests read from disk, so flush the buffer first.
    const open = vscode.workspace.textDocuments.find((d) => d.uri.fsPath === file);
    if (open?.isDirty) {
      await open.save();
    }

    panel.setRunning(slug, true);
    statusBar.text = `$(sync~spin) VeetCode: running ${problem.title}`;

    let summary: RunSummary;
    try {
      summary = await vscode.window.withProgress(
        { location: vscode.ProgressLocation.Window, title: `VeetCode: ${mode === 'sample' ? 'running samples' : 'submitting'}`, cancellable: true },
        (_p, token) => runner.run(problem, language, file, mode, token)
      );
    } catch (err) {
      panel.setRunning(slug, false);
      updateContext();
      void vscode.window.showErrorMessage(`VeetCode: ${(err as Error).message}`);
      return;
    }

    panel.setRunning(slug, false);
    panel.show(problem, progress.get(slug), language);
    panel.showResults(summary);
    logSummary(output, problem, summary);

    const solved = mode === 'submit' && summary.passed === summary.total && summary.total > 0 && !summary.compileError;
    const wasSolved = progress.get(slug).status === 'solved';
    const lockedBefore = !progress.editorialUnlocked(slug);
    if (!summary.compileError) {
      const slowest = Math.max(0, ...summary.results.map((r) => r.runtimeMs));
      await progress.recordAttempt(slug, solved, solved ? slowest : undefined, mode);
    }
    await daily.record(mode, solved && !wasSolved);
    if (lockedBefore && progress.editorialUnlocked(slug) && problem.editorial) {
      void vscode.window.showInformationMessage(
        `VeetCode: editorial unlocked for ${problem.title}. Read it in the description panel — no browser required.`
      );
    }

    updateContext();
    tree.refresh();

    if (summary.compileError) {
      void vscode.window.showErrorMessage('VeetCode: solution failed to load — see the description panel.');
    } else if (solved) {
      void vscode.window.showInformationMessage(
        `VeetCode: Accepted — ${problem.title} (${summary.total}/${summary.total} hidden tests). No tabs were opened in the making of this solve.`
      );
    } else if (summary.passed === summary.total) {
      void vscode.window.showInformationMessage(
        `VeetCode: ${summary.passed}/${summary.total} sample tests passed. Submit to face the hidden ones.`
      );
    } else {
      const firstFail = summary.results.find((r) => !r.passed);
      void vscode.window.showWarningMessage(
        `VeetCode: ${summary.passed}/${summary.total} passed — case ${(firstFail?.index ?? 0) + 1} failed.`
      );
    }
  }

  async function runActive(mode: 'sample' | 'submit'): Promise<void> {
    const active = activeProblem();
    if (!active) {
      void vscode.window.showWarningMessage('VeetCode: open a problem first — pick one from the sidebar. Nothing to run in an empty editor.');
      return;
    }
    await runProblem(active.problem.slug, mode);
  }

  // --------------------------------------------------------------- commands

  context.subscriptions.push(
    output,
    treeView,
    statsView,
    dailyView,
    statusBar,
    languageBar,
    tree,
    stats,
    dailyStats,
    progress,
    daily,
    { dispose: () => panel.dispose() },

    vscode.commands.registerCommand('veetcode.openProblem', (slug: string) => openProblem(slug)),
    vscode.commands.registerCommand('veetcode.runTests', () => runActive('sample')),
    vscode.commands.registerCommand('veetcode.submit', () => runActive('submit')),

    vscode.commands.registerCommand('veetcode.selectPlaylist', async () => {
      const active = tree.activePlaylist();
      const items: (vscode.QuickPickItem & { id?: string })[] = [
        {
          label: 'All problems',
          description: `${bank.all().length} problems`,
          detail: 'Clear the sheet and browse the whole bank',
          id: undefined,
        },
      ];
      let lastKind = '';
      for (const playlist of playlists.all()) {
        const resolved = playlists.resolve(playlist, bank);
        const solved = resolved.problems.filter((p) => progress.get(p.slug).status === 'solved').length;
        if (playlist.kind !== lastKind) {
          lastKind = playlist.kind;
          items.push({ label: playlist.kind === 'company' ? 'Company sheets' : 'Curated sheets', kind: vscode.QuickPickItemKind.Separator });
        }
        items.push({
          label: playlist.name,
          description: `${solved}/${resolved.problems.length} solved` + (resolved.missing ? ` · ${resolved.missing} not bundled yet` : ''),
          detail: [playlist.author ? `by ${playlist.author}` : '', playlist.description].filter(Boolean).join(' — '),
          id: playlist.id,
          picked: active?.playlist.id === playlist.id,
        });
      }
      const pick = await vscode.window.showQuickPick(items, {
        placeHolder: active ? `Current sheet: ${active.playlist.name}` : 'Pick a DSA sheet',
        matchOnDescription: true,
        matchOnDetail: true,
      });
      if (!pick || pick.kind === vscode.QuickPickItemKind.Separator) {
        return;
      }
      await selectPlaylist(pick.id);
      const chosen = tree.activePlaylist();
      if (chosen) {
        const solved = chosen.problems.filter((p) => progress.get(p.slug).status === 'solved').length;
        void vscode.window.showInformationMessage(
          `VeetCode: ${chosen.playlist.name} — ${solved}/${chosen.problems.length} already solved` +
            (solved ? ' (progress carries over from other sheets).' : '.')
        );
      }
    }),

    vscode.commands.registerCommand('veetcode.clearPlaylist', () => void selectPlaylist(undefined)),

    // Fired by clicking a sheet row in the Progress view: make it the active
    // sheet and put its problems on screen. `undefined` clears back to all.
    vscode.commands.registerCommand('veetcode.setPlaylist', async (id?: string) => {
      tree.clearFilters();
      await selectPlaylist(id);
      await vscode.commands.executeCommand('veetcode.problems.focus');
      const chosen = tree.activePlaylist();
      if (!chosen) {
        void vscode.window.showInformationMessage(`VeetCode: showing all ${bank.all().length} problems.`);
        return;
      }
      const solved = chosen.problems.filter((p) => progress.get(p.slug).status === 'solved').length;
      void vscode.window.showInformationMessage(
        `VeetCode: ${chosen.playlist.name} — ${solved}/${chosen.problems.length} already solved` +
          (solved ? ' (progress carries over from other sheets).' : '.')
      );
    }),

    vscode.commands.registerCommand('veetcode.refresh', () => {
      bank.reload();
      playlists.reload();
      tree.refresh();
      stats.refresh();
      dailyStats.refresh();
      updateDailyTitle();
      updatePlaylistTitle();
      void vscode.window.showInformationMessage(
        `VeetCode: ${bank.all().length} problems and ${playlists.all().length} sheets loaded.`
      );
    }),

    vscode.commands.registerCommand('veetcode.randomProblem', async () => {
      const pool = tree.visibleProblems().filter((p) => progress.get(p.slug).status !== 'solved');
      const candidates = pool.length ? pool : tree.visibleProblems();
      if (!candidates.length) {
        void vscode.window.showInformationMessage('VeetCode: nothing matches the current filters. Even the excuses ran out.');
        return;
      }
      const pick = candidates[Math.floor(Math.random() * candidates.length)];
      await openProblem(pick.slug);
    }),

    vscode.commands.registerCommand('veetcode.searchProblems', async () => {
      const pick = await vscode.window.showQuickPick(
        bank.all().map((p) => ({
          label: `${p.id}. ${p.title}`,
          description: `${p.difficulty}${progress.get(p.slug).status === 'solved' ? ' · solved' : ''}`,
          detail: p.tags.join(', '),
          slug: p.slug,
        })),
        { placeHolder: 'Search problems by name, number or topic', matchOnDescription: true, matchOnDetail: true }
      );
      if (pick) {
        await openProblem(pick.slug);
      }
    }),

    vscode.commands.registerCommand('veetcode.filterDifficulty', async () => {
      const pick = await vscode.window.showQuickPick(['All', 'Easy', 'Medium', 'Hard'], { placeHolder: 'Filter by difficulty' });
      if (pick) {
        tree.setFilter('difficulty', pick === 'All' ? undefined : (pick as Difficulty));
      }
    }),

    vscode.commands.registerCommand('veetcode.filterTag', async () => {
      const pick = await vscode.window.showQuickPick(['All', ...bank.tags()], { placeHolder: 'Filter by topic' });
      if (pick) {
        tree.setFilter('tag', pick === 'All' ? undefined : pick);
      }
    }),

    vscode.commands.registerCommand('veetcode.filterStatus', async () => {
      const pick = await vscode.window.showQuickPick(['All', 'todo', 'attempted', 'solved', 'favorites'], {
        placeHolder: 'Filter by status',
      });
      if (pick) {
        tree.setFilter('status', pick === 'All' ? undefined : (pick as Status | 'favorites'));
      }
    }),

    vscode.commands.registerCommand('veetcode.clearFilters', () => tree.clearFilters()),

    vscode.commands.registerCommand('veetcode.setGroupBy', async () => {
      const choices = tree.activePlaylist() ? ['section', 'difficulty', 'topic', 'status', 'none'] : ['difficulty', 'topic', 'status', 'none'];
      const pick = await vscode.window.showQuickPick(choices, {
        placeHolder: `Group problems by (current: ${tree.getGroupBy()})`,
      });
      if (pick) {
        tree.setGroupBy(pick as GroupBy);
      }
    }),

    vscode.commands.registerCommand('veetcode.changeLanguage', async () => {
      const current = activeProblem()?.language ?? currentLanguage();
      const pick = await vscode.window.showQuickPick(
        (Object.keys(LANGUAGE_LABELS) as Language[]).map((id) => ({
          label: LANGUAGE_LABELS[id],
          description: id === current ? 'current' : undefined,
          id,
        })),
        { placeHolder: 'Solution language' }
      );
      if (pick) {
        await switchLanguage(pick.id);
      }
    }),

    vscode.commands.registerCommand('veetcode.showDescription', () => {
      const active = activeProblem();
      if (active) {
        panel.show(active.problem, progress.get(active.problem.slug), active.language, false);
      }
    }),

    vscode.commands.registerCommand('veetcode.resetSolution', () => {
      const active = activeProblem();
      if (active) {
        void resetSolution(active.problem.slug);
      }
    }),

    vscode.commands.registerCommand('veetcode.toggleFavorite', async (node?: { problem?: Problem }) => {
      const slug = node?.problem?.slug ?? activeProblem()?.problem.slug;
      if (slug) {
        await progress.toggleFavorite(slug);
      }
    }),

    vscode.commands.registerCommand('veetcode.resetProgress', async () => {
      const choice = await vscode.window.showWarningMessage(
        'Reset all VeetCode progress? Solved/attempted status, favorites, daily stats and your streak are cleared. ' +
          'Solution files on disk are kept.',
        { modal: true },
        'Reset'
      );
      if (choice === 'Reset') {
        await progress.reset();
        await daily.reset();
        void vscode.window.showInformationMessage('VeetCode: progress cleared. Streak back to zero.');
      }
    }),

    vscode.commands.registerCommand('veetcode.showDailyStats', async () => {
      await vscode.commands.executeCommand('veetcode.daily.focus');
      const summary = daily.summary();
      void vscode.window.showInformationMessage(
        `VeetCode today: ${summary.today.solved} solved, ${summary.today.runs} runs, ` +
          `${summary.today.submits} submits · ${summary.streak}-day streak (best ${summary.longestStreak}).`
      );
    }),

    vscode.commands.registerCommand('veetcode.buyMeACoffee', () =>
      vscode.env.openExternal(vscode.Uri.parse(SUPPORT_URL))
    ),

    vscode.commands.registerCommand('veetcode.showEditorial', async () => {
      const active = activeProblem();
      if (!active) {
        void vscode.window.showWarningMessage('VeetCode: open a problem first.');
        return;
      }
      const entry = progress.get(active.problem.slug);
      if (!active.problem.editorial) {
        void vscode.window.showInformationMessage(`VeetCode: no editorial bundled for ${active.problem.title}.`);
        return;
      }
      if (!progress.editorialUnlocked(active.problem.slug)) {
        const left = EDITORIAL_UNLOCK_AT - (entry.failedSubmits ?? 0);
        void vscode.window.showInformationMessage(
          `VeetCode: editorial locked. ${left} more failed submit${left === 1 ? '' : 's'} (or a solve) and it opens. ` +
            'Struggling is the part that teaches.'
        );
        return;
      }
      panel.show(active.problem, entry, active.language);
      panel.revealEditorial();
    }),

    vscode.commands.registerCommand('veetcode.showStats', () => {
      const summary = progress.summary(bank.all().map((p) => p.slug));
      void vscode.window.showInformationMessage(
        `VeetCode: ${summary.solved} solved, ${summary.attempted} in progress, ${summary.todo} untouched (${bank.all().length} total).`
      );
    }),

    vscode.window.onDidChangeActiveTextEditor(() => updateContext()),

    vscode.workspace.onDidSaveTextDocument(async (document) => {
      if (!vscode.workspace.getConfiguration('veetcode').get<boolean>('runTestsOnSave', false)) {
        return;
      }
      const identified = workspace.identify(document.uri.fsPath);
      if (identified && bank.get(identified.slug)) {
        await runProblem(identified.slug, 'sample');
      }
    })
  );

  tree.setPlaylist(context.globalState.get<string | undefined>(ACTIVE_PLAYLIST_KEY));
  updateContext();
  updateDailyTitle();
  updatePlaylistTitle();
  output.appendLine(
    `VeetCode ready: ${bank.all().length} problems, ${playlists.all().length} sheets, solutions in ${workspace.root()}`
  );
}

function logSummary(output: vscode.OutputChannel, problem: Problem, summary: RunSummary): void {
  output.appendLine('');
  output.appendLine(`[${new Date().toLocaleTimeString()}] ${problem.title} — ${summary.mode} (${summary.language})`);
  if (summary.compileError) {
    output.appendLine(summary.compileError);
    return;
  }
  for (const result of summary.results) {
    const mark = result.passed ? 'PASS' : 'FAIL';
    output.appendLine(`  ${mark} case ${result.index + 1} (${result.runtimeMs} ms)`);
    if (!result.passed) {
      output.appendLine(`       input:    ${describe(result.input, 200)}`);
      output.appendLine(`       expected: ${describe(result.expected, 200)}`);
      if (result.error) {
        output.appendLine(`       error:    ${result.error.split('\n').slice(-3).join(' | ')}`);
      } else {
        output.appendLine(`       actual:   ${describe(result.actual, 200)}`);
      }
    }
  }
  output.appendLine(`  => ${summary.passed}/${summary.total} passed in ${summary.totalMs} ms`);
}

export function deactivate(): void {
  // Nothing to clean up beyond the disposables registered in activate().
}
