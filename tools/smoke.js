/**
 * Smoke test for the compiled extension modules, run outside VS Code.
 *
 * The `vscode` module only exists inside the extension host, so it is stubbed
 * with the small surface the modules under test actually touch. This exercises
 * the problem bank, the file layout, the Markdown renderer and a real end-to-end
 * test run through the Python harness.
 *
 * Usage: npm run compile && node tools/smoke.js
 */
'use strict';

const assert = require('assert');
const fs = require('fs');
const os = require('os');
const path = require('path');
const Module = require('module');

const ROOT = path.dirname(__dirname);
const OUT = path.join(ROOT, 'out');
const sandboxRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'veetcode-smoke-'));

// ------------------------------------------------------------------ vscode stub

const config = {
  language: 'python',
  workspaceFolder: 'veetcode',
  pythonPath: 'python3',
  nodePath: 'node',
  testTimeoutMs: 10000,
};

class EventEmitter {
  constructor() {
    this.handlers = [];
    this.event = (handler) => {
      this.handlers.push(handler);
      return { dispose: () => {} };
    };
  }
  fire(value) {
    this.handlers.forEach((h) => h(value));
  }
  dispose() {}
}

const vscodeStub = {
  EventEmitter,
  ThemeIcon: class ThemeIcon {
    constructor(id, color) {
      this.id = id;
      this.color = color;
    }
  },
  ThemeColor: class ThemeColor {
    constructor(id) {
      this.id = id;
    }
  },
  MarkdownString: class MarkdownString {
    constructor(value) {
      this.value = value;
    }
  },
  TreeItem: class TreeItem {
    constructor(label, collapsibleState) {
      this.label = label;
      this.collapsibleState = collapsibleState;
    }
  },
  TreeItemCollapsibleState: { None: 0, Collapsed: 1, Expanded: 2 },
  workspace: {
    workspaceFolders: [{ uri: { fsPath: sandboxRoot } }],
    getConfiguration: () => ({ get: (key, fallback) => (key in config ? config[key] : fallback) }),
  },
};

const originalLoad = Module._load;
Module._load = function (request, parent, isMain) {
  if (request === 'vscode') {
    return vscodeStub;
  }
  return originalLoad.call(this, request, parent, isMain);
};

// ------------------------------------------------------------------ under test

const { ProblemBank } = require(path.join(OUT, 'problems/loader'));
const { SolutionWorkspace } = require(path.join(OUT, 'storage/workspace'));
const { TestRunner } = require(path.join(OUT, 'runner/runner'));
const { ProblemTreeProvider } = require(path.join(OUT, 'tree/problemTree'));
const { PlaylistBank } = require(path.join(OUT, 'playlists/loader'));
const { renderMarkdown } = require(path.join(OUT, 'panel/markdown'));
const { DailyStore, dayKey } = require(path.join(OUT, 'storage/daily'));
const { ProgressStore } = require(path.join(OUT, 'storage/progress'));
const { DailyTreeProvider } = require(path.join(OUT, 'tree/dailyTree'));

const checks = [];
function check(name, fn) {
  checks.push({ name, fn });
}

check('problem bank loads every bundled problem', () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  assert.strictEqual(bank.errors().length, 0, bank.errors().join('; '));
  assert.ok(bank.all().length >= 220, `only ${bank.all().length} problems loaded`);
  assert.ok(bank.get('two-sum'), 'two-sum missing');
  assert.ok(bank.tags().includes('Dynamic Programming'));
  for (const problem of bank.all()) {
    const name = problem.design ? problem.design.className : problem.functionName;
    assert.ok(problem.starter.python.includes(name), `${problem.slug}: python starter`);
    assert.ok(problem.starter.javascript.includes(name), `${problem.slug}: js starter`);
    assert.ok(problem.tests.some((t) => t.sample), `${problem.slug}: no sample test`);
    // A handful of problems have only a few legal inputs (N-Queens tops out at
    // n = 9), so the floor is low and the bulk is checked separately below.
    assert.ok(problem.tests.length >= 8, `${problem.slug}: only ${problem.tests.length} tests`);
  }
  const deep = bank.all().filter((p) => p.tests.length >= 20).length;
  assert.ok(deep >= bank.all().length * 0.75, `only ${deep} problems have 20+ tests`);
});

check('scaffolding writes starter code and maps back to the problem', () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const workspace = new SolutionWorkspace(sandboxRoot);
  const problem = bank.get('two-sum');

  const file = workspace.ensureSolutionFile(problem, 'python');
  assert.ok(fs.existsSync(file));
  assert.match(path.relative(sandboxRoot, file), /^veetcode\/001-two-sum\/solution\.py$/);

  const identified = workspace.identify(file);
  assert.deepStrictEqual(identified, { slug: 'two-sum', language: 'python' });
  assert.strictEqual(workspace.identify(path.join(sandboxRoot, 'notes.py')), undefined);

  // An existing file is never clobbered unless overwrite is requested.
  fs.writeFileSync(file, '# mine\n');
  workspace.ensureSolutionFile(problem, 'python');
  assert.strictEqual(fs.readFileSync(file, 'utf8'), '# mine\n');
  workspace.ensureSolutionFile(problem, 'python', true);
  assert.ok(fs.readFileSync(file, 'utf8').includes('def twoSum'));
});

check('filters and grouping narrow the tree', () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const progress = {
    get: () => ({ status: 'todo', attempts: 0 }),
    onDidChange: () => ({ dispose: () => {} }),
  };
  const playlists = new PlaylistBank([path.join(ROOT, 'playlists')]);
  const tree = new ProblemTreeProvider(bank, progress, playlists);

  tree.setFilter('difficulty', 'Hard');
  assert.ok(tree.visibleProblems().every((p) => p.difficulty === 'Hard'));
  assert.ok(tree.visibleProblems().length > 0);

  tree.clearFilters();
  tree.setFilter('search', 'anagram');
  const slugs = tree.visibleProblems().map((p) => p.slug);
  assert.ok(slugs.includes('valid-anagram') && slugs.includes('group-anagrams'), slugs.join(','));

  tree.clearFilters();
  tree.setGroupBy('difficulty');
  const groups = tree.getChildren().map((g) => g.label);
  assert.deepStrictEqual(groups, ['Easy', 'Medium', 'Hard']);
  const item = tree.getTreeItem(tree.getChildren(tree.getChildren()[0])[0]);
  assert.ok(String(item.label).includes('.'), 'problem item label');
});

check('sheets load, resolve against the bank and share progress by slug', () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const playlists = new PlaylistBank([path.join(ROOT, 'playlists')]);
  assert.strictEqual(playlists.errors().length, 0, playlists.errors().join('; '));
  assert.ok(playlists.all().length >= 20, `only ${playlists.all().length} sheets loaded`);

  const starter = playlists.get('veetcode-starter');
  assert.ok(starter, 'starter sheet missing');
  const resolvedStarter = playlists.resolve(starter, bank);
  assert.strictEqual(resolvedStarter.missing, 0, 'starter sheet must be fully bundled');
  assert.ok(resolvedStarter.problems.length >= 40);

  const blind = playlists.resolve(playlists.get('blind-75'), bank);
  assert.strictEqual(blind.listed, 75);
  assert.strictEqual(blind.missing, 0, 'Blind 75 should be fully bundled');
  assert.strictEqual(blind.problems.length, 75);
  assert.ok(blind.problems.every((p) => bank.get(p.slug)));

  // Every sheet resolves against the bank, and every bundled problem is
  // reachable from at least one sheet.
  const reachable = new Set();
  for (const sheet of playlists.all()) {
    const resolved = playlists.resolve(sheet, bank);
    assert.strictEqual(resolved.missing, 0, `${sheet.id} lists ${resolved.missing} unbundled problems`);
    resolved.problems.forEach((p) => reachable.add(p.slug));
  }
  assert.strictEqual(reachable.size, bank.all().length, 'some bundled problems are on no sheet');

  // The same problem in two sheets is the same slug, which is what makes
  // progress carry across sheets.
  const shared = playlists.containing('two-sum').map((p) => p.id);
  assert.ok(shared.includes('blind-75') && shared.includes('striver-sde'), shared.join(','));
  assert.ok(shared.some((id) => id.startsWith('company-')), shared.join(','));

  const progress = {
    get: (slug) => ({ status: slug === 'two-sum' ? 'solved' : 'todo', attempts: 1 }),
    onDidChange: () => ({ dispose: () => {} }),
  };
  const tree = new ProblemTreeProvider(bank, progress, playlists);
  tree.setPlaylist('blind-75');
  assert.strictEqual(tree.getGroupBy(), 'section');
  const sections = tree.getChildren();
  assert.ok(sections.length > 0 && sections.every((s) => s.kind === 'group'));
  assert.ok(tree.visibleProblems().every((p) => blind.problems.includes(p)));

  // Solved in the starter sheet, still solved when reached through Blind 75.
  const arrays = sections.find((s) => s.label === 'Array');
  const twoSum = tree.getChildren(arrays).find((n) => n.problem.slug === 'two-sum');
  assert.ok(twoSum, 'two-sum missing from the Array section');
  const tooltip = String(tree.getTreeItem(twoSum).tooltip.value);
  assert.ok(tooltip.includes('Status: solved'), tooltip);
  assert.ok(tooltip.includes('Also in:'), tooltip);

  tree.setPlaylist(undefined);
  assert.strictEqual(tree.getGroupBy(), 'difficulty');
  assert.strictEqual(tree.visibleProblems().length, bank.all().length);
});

check('daily stats count runs, solves and the streak', () => {
  const DAY = 24 * 60 * 60 * 1000;
  let now = new Date('2026-03-10T09:00:00').getTime();
  const store = new Map();
  const memento = {
    get: (key, fallback) => (store.has(key) ? store.get(key) : fallback),
    update: (key, value) => {
      store.set(key, value);
      return Promise.resolve();
    },
  };
  const daily = new DailyStore(memento, () => now);

  assert.strictEqual(daily.summary().streak, 0);
  assert.strictEqual(daily.summary().today.runs, 0);

  daily.record('sample', false);
  daily.record('submit', false);
  daily.record('submit', true);
  let summary = daily.summary();
  assert.strictEqual(summary.today.runs, 3);
  assert.strictEqual(summary.today.submits, 2);
  assert.strictEqual(summary.today.solved, 1);
  assert.strictEqual(summary.streak, 1);
  assert.strictEqual(summary.totalSolved, 1);
  assert.strictEqual(summary.last7[6].label, 'Today');

  // Next day, another solve: the streak grows.
  now += DAY;
  daily.record('submit', true);
  summary = daily.summary();
  assert.strictEqual(summary.streak, 2);
  assert.strictEqual(summary.weekSolved, 2);

  // A day with runs but no solve does not extend the streak, and it survives
  // until that day is over.
  now += DAY;
  daily.record('sample', false);
  assert.strictEqual(daily.summary().streak, 2, 'today without a solve keeps yesterday alive');

  // Skip a day entirely: the streak is gone, the best is remembered.
  now += 2 * DAY;
  summary = daily.summary();
  assert.strictEqual(summary.streak, 0);
  assert.strictEqual(summary.longestStreak, 2);
  assert.strictEqual(summary.activeDays, 3);

  const view = new DailyTreeProvider(daily);
  const rows = view.getChildren();
  const labels = rows.map((r) => r.label);
  assert.ok(labels.includes('Solved today') && labels.includes('Streak') && labels.includes('Last 7 days'), labels.join(','));
  const week = rows.find((r) => r.label === 'Last 7 days');
  assert.strictEqual(view.getChildren(week).length, 7);
  assert.strictEqual(String(view.getTreeItem(rows[0]).label), 'Solved today');
  assert.strictEqual(dayKey(now).length, 10);
});

check('editorials stay locked until three submits have failed', () => {
  const store = new Map();
  const memento = {
    get: (key, fallback) => (store.has(key) ? store.get(key) : fallback),
    update: (key, value) => {
      store.set(key, value);
      return Promise.resolve();
    },
  };
  const progress = new ProgressStore(memento);

  assert.strictEqual(progress.editorialUnlocked('two-sum'), false);
  progress.recordAttempt('two-sum', false, undefined, 'sample');
  assert.strictEqual(progress.editorialUnlocked('two-sum'), false, 'sample runs must not unlock it');

  progress.recordAttempt('two-sum', false, undefined, 'submit');
  progress.recordAttempt('two-sum', false, undefined, 'submit');
  assert.strictEqual(progress.get('two-sum').failedSubmits, 2);
  assert.strictEqual(progress.editorialUnlocked('two-sum'), false);

  progress.recordAttempt('two-sum', false, undefined, 'submit');
  assert.strictEqual(progress.editorialUnlocked('two-sum'), true, 'three failed submits should unlock');

  // Solving unlocks it immediately, without failing first.
  progress.recordAttempt('3sum', true, 12, 'submit');
  assert.strictEqual(progress.editorialUnlocked('3sum'), true);

  // Every bundled problem ships one, with code for the language it was written in.
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  for (const problem of bank.all()) {
    assert.ok(problem.editorial, `${problem.slug}: no editorial`);
    assert.ok(problem.editorial.explanation.length > 40, `${problem.slug}: editorial too thin`);
    assert.ok(problem.editorial.code.python, `${problem.slug}: no python reference in the editorial`);
  }
});

check('markdown renderer handles the statement subset', () => {
  const html = renderMarkdown('# Title\n\nSome `code` and **bold**.\n\n- one\n- two\n\n```python\nx = 1 < 2\n```\n');
  assert.ok(html.includes('<h3>Title</h3>'));
  assert.ok(html.includes('<code>code</code>'));
  assert.ok(html.includes('<strong>bold</strong>'));
  assert.ok(html.includes('<li>one</li>'));
  assert.ok(html.includes('x = 1 &lt; 2'), 'code block should be escaped, not parsed');
  assert.ok(!html.includes('@@BLOCK'), 'code placeholder leaked');
  assert.ok(renderMarkdown('<img src=x onerror=alert(1)>').includes('&lt;img'), 'html not escaped');
});

check('a correct solution passes and a wrong one fails (python)', async () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const workspace = new SolutionWorkspace(sandboxRoot);
  const runner = new TestRunner(path.join(ROOT, 'runners'));
  const problem = bank.get('two-sum');
  const file = workspace.ensureSolutionFile(problem, 'python', true);

  const wrong = await runner.run(problem, 'python', file, 'sample');
  assert.strictEqual(wrong.compileError, undefined, wrong.compileError);
  assert.strictEqual(wrong.passed, 0, 'starter code should not pass');
  assert.strictEqual(wrong.total, problem.tests.filter((t) => t.sample).length);

  fs.copyFileSync(path.join(ROOT, 'tools/reference/two-sum.py'), file);
  const right = await runner.run(problem, 'python', file, 'submit');
  assert.strictEqual(right.passed, problem.tests.length, JSON.stringify(right.results));
  assert.ok(right.results.every((r) => typeof r.runtimeMs === 'number'));
});

check('broken solutions surface as errors, not crashes (javascript)', async () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const workspace = new SolutionWorkspace(sandboxRoot);
  const runner = new TestRunner(path.join(ROOT, 'runners'));
  const problem = bank.get('two-sum');
  const file = workspace.solutionPath(problem, 'javascript');
  fs.mkdirSync(path.dirname(file), { recursive: true });

  fs.writeFileSync(file, 'var twoSum = function (nums, target) {\n');
  const broken = await runner.run(problem, 'javascript', file, 'sample');
  assert.ok(broken.compileError, 'syntax error should be reported');

  fs.writeFileSync(file, 'var somethingElse = function () {};\n');
  const missing = await runner.run(problem, 'javascript', file, 'sample');
  assert.match(missing.compileError || '', /no function named "twoSum"/);

  fs.copyFileSync(path.join(ROOT, 'tools/reference/two-sum.js'), file);
  const ok = await runner.run(problem, 'javascript', file, 'submit');
  assert.strictEqual(ok.passed, problem.tests.length, JSON.stringify(ok.results));
});

check('an infinite loop is killed and reported', async () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const workspace = new SolutionWorkspace(sandboxRoot);
  const runner = new TestRunner(path.join(ROOT, 'runners'));
  const problem = bank.get('two-sum');
  const file = workspace.solutionPath(problem, 'python');
  fs.writeFileSync(file, 'def twoSum(nums, target):\n    while True:\n        pass\n');

  config.testTimeoutMs = 1000;
  try {
    const summary = await runner.run(problem, 'python', file, 'sample');
    assert.match(summary.compileError || '', /Timed out/);
  } finally {
    config.testTimeoutMs = 10000;
  }
});

check('a missing interpreter fails with a readable message', async () => {
  const bank = new ProblemBank([path.join(ROOT, 'problems')]);
  const workspace = new SolutionWorkspace(sandboxRoot);
  const runner = new TestRunner(path.join(ROOT, 'runners'));
  const problem = bank.get('two-sum');
  const file = workspace.ensureSolutionFile(problem, 'python');

  config.pythonPath = 'definitely-not-a-real-python';
  try {
    await runner.run(problem, 'python', file, 'sample');
    assert.fail('expected a spawn failure');
  } catch (err) {
    assert.match(err.message, /could not start "definitely-not-a-real-python"/);
  } finally {
    config.pythonPath = 'python3';
  }
});

(async () => {
  let failed = 0;
  for (const { name, fn } of checks) {
    try {
      await fn();
      console.log(`ok   ${name}`);
    } catch (err) {
      failed++;
      console.log(`FAIL ${name}\n     ${err.message.split('\n')[0]}`);
    }
  }
  fs.rmSync(sandboxRoot, { recursive: true, force: true });
  console.log(`\n${checks.length - failed}/${checks.length} smoke checks passed`);
  process.exit(failed ? 1 : 0);
})();
