# VeetCode: LeetCode Offline

DSA practice that lives inside VS Code and never touches the internet.

Here is how the usual session goes. You open LeetCode. A notification slides in. You check it
"for one second". Forty minutes later you are watching a video about someone restoring a canoe.
You come back, fail the first submit, feel the sting, open a new tab, and ask a chatbot to just
tell you. It does. You nod along, mark it solved, and learn nothing. The next interview asks the
same pattern and you blank.

VeetCode removes every one of those exits. No browser tab, no feed, no autocomplete-shaped safety
net, no ChatGPT sitting one keystroke away — 223 problems, hidden tests and a local judge, all
running on your own machine. **So turn off the wifi and lock in toward that shiny SDE job
paycheck.**

Editorials exist, but they stay locked until you have failed a problem three times. Struggling is
not the obstacle; it is the entire product.

## What it does

- **223 problems** across arrays, strings, hash tables, two pointers, sliding window, binary
  search, linked lists, trees, graphs, tries, backtracking, DP, greedy, heaps and design.
- **21 DSA sheets to pick from** — Blind 75, the Striver SDE Sheet, a starter sheet and 18
  company lists (Google, Amazon, Meta, Microsoft, Apple, Flipkart, Zomato, Swiggy, Razorpay,
  Atlassian, Jane Street, Citadel, Tower Research, Optiver, Uber, Airbnb, Stripe, Databricks).
  Progress is stored per problem, so a question solved in one sheet shows as solved in every
  other sheet that lists it.
- **Deep test suites** — 5,900 cases across the bank, a median of 26 per problem and up to 35,
  mixing hand-written edge cases, randomised cases and large stress cases that time out a
  brute-force solution.
- **Sidebar problem browser** grouped by sheet section, difficulty, topic or status, with
  filters, search, favorites and a "pick a random unsolved problem" button.
- **Description panel** — statement, examples, constraints, progressive hints, target complexity
  and the (locked) editorial, rendered next to your code.
- **Local judge** — `Run Samples` executes the visible cases, `Submit` runs the full hidden
  suite. Failures show input, expected, actual, your `print`/`console.log` output and the
  stack trace.
- **Progress tracking** — solved / attempted / untouched per problem, stored per machine, with
  a progress view that breaks the count down by difficulty.
- **Daily stats** — solves today, current streak, best streak, runs and submits, time between
  your first and last run of the day, and a seven-day bar. Nobody else's numbers, because nobody
  else is here.
- **Locked editorials** — every problem ships a written walkthrough plus the reference solution,
  sealed until three failed submits (or a solve). Fail properly first.
- **Python and JavaScript** solutions, switched from the description panel, the status bar or the
  command palette. Switching reopens the current problem in the new language; the old solution
  file is left untouched, so switching back finds your work where you left it.

## Getting started

```bash
npm install
npm run compile
```

Press <kbd>F5</kbd> in VS Code (or run the "Run VeetCode Extension" launch configuration) to open
an Extension Development Host with VeetCode loaded. Click the VeetCode icon in the activity bar
and pick a problem.

To install it properly instead:

```bash
npm run package       # produces veetcode-0.4.0.vsix
code --install-extension veetcode-0.4.0.vsix
```

## Using it

| Action | How |
| --- | --- |
| Open a problem | Click it in the VeetCode sidebar |
| Run sample tests | <kbd>Cmd/Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>R</kbd>, the editor title ▶ button, or the panel button |
| Submit (all hidden tests) | <kbd>Cmd/Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Enter</kbd> |
| Pick a DSA sheet | The list button in the Problems view title bar, or `VeetCode: Select DSA Sheet` |
| Back to every problem | `VeetCode: Show All Problems (Clear Sheet)` |
| Search / filter / group | Buttons in the Problems view title bar |
| Switch language | The picker in the description panel toolbar, the language in the status bar, or `VeetCode: Change Solution Language` |
| See today's numbers | `VeetCode: Show Today's Stats`, or the Daily Stats view in the sidebar |
| Read the editorial | `VeetCode: Show Editorial` (after 3 failed submits) |
| Reset to starter code | `VeetCode: Reset Solution to Starter Code` |

Solutions are written to `<workspace>/veetcode/<id>-<slug>/solution.<ext>` — ordinary files you
can commit, diff and revisit. If no folder is open, they go to the extension's global storage.

### Settings

| Setting | Default | Meaning |
| --- | --- | --- |
| `veetcode.language` | `python` | Language used when scaffolding new solutions |
| `veetcode.workspaceFolder` | `veetcode` | Where solution files are written |
| `veetcode.pythonPath` | `python3` | Interpreter for Python solutions |
| `veetcode.nodePath` | `node` | Runtime for JavaScript solutions |
| `veetcode.testTimeoutMs` | `15000` | Budget for a whole test batch before it is killed |
| `veetcode.runTestsOnSave` | `false` | Run sample tests on every save |
| `veetcode.openDescriptionOnOpen` | `true` | Open the description panel beside the editor |

## Sheets

A sheet is an ordered, sectioned list of problems. Pick one from the Problems view title bar and
the tree narrows to it, grouped by the sheet's own sections (Blind 75 by topic, the SDE sheet by
day). The view title shows how far through it you are, and the Progress view has a line per sheet.

Sheets share one progress store, keyed by problem slug. Two Sum sits in Blind 75, the SDE sheet
and five company lists; solving it once ticks it off in all of them, and the tooltip on a problem
lists the other sheets it appears in.

A sheet may list problems this build does not bundle yet — those are reported as `+N soon` next
to the section rather than hidden. All 223 bundled problems are reachable from a sheet, and the
starter sheet contains only bundled ones.

To add your own, drop a JSON file into `<workspace>/veetcode/playlists/`:

```json
{
  "id": "my-sheet",
  "name": "My Sheet",
  "kind": "curated",
  "description": "What this sheet is for",
  "sections": [{ "name": "Week 1", "slugs": ["two-sum", "valid-parentheses"] }]
}
```

`VeetCode: Refresh Problem List` picks it up. A file that reuses a bundled id shadows it.

## Daily stats

There is no leaderboard. Ranking yourself against strangers is a way to feel busy, and inventing
fake rivals to rank against is worse. The Daily Stats view tracks the only thing that moves the
needle — whether you showed up today:

- **Solved today** and **runs today**, submits counted separately from sample runs.
- **Streak** — consecutive days with at least one solve, plus your best ever. An empty today does
  not break the streak until the day is actually over, so there is still time.
- **Time at the desk** — first run to last run today. Thinking time is invisible to it; that is
  fine, it is a nudge, not a timesheet.
- **Last 7 days** — one row per day with a small bar, so a bad week is obvious without a dashboard.
- **All time** — solves, submits, runs and your accepted rate. That number is yours alone and no
  recruiter will ever see it.

The view title carries today's solves and the streak, so it is visible without expanding anything.

## Editorials, locked on purpose

Every problem ships an editorial: a written explanation of the approach and the verified reference
solution in Python (and JavaScript where one exists). It is **locked until three submits have
failed**, or until you solve the problem.

The panel shows the counter (`1/3`, `2/3`) so the deal is never a mystery. Three honest failures is
the point where a hint teaches something instead of replacing the thinking. And because the
explanation is bundled, unlocking it does not involve opening a browser and losing the next hour.

The code inside an editorial is pulled from `tools/reference/`, the same solutions `npm run verify`
runs through the real judge — so an editorial can never show you something the judge would reject.

## How the judge works

Your solution file is never modified. On a run the extension writes a payload (solution path,
function name, test cases, comparison mode) to a temp file and spawns
`runners/harness.py` or `runners/harness.js`, which:

1. loads your file — a top-level function, an exported function, or a `class Solution` method
   all work;
2. marshals each test input (arrays stay arrays; `tree` inputs become a real `TreeNode`,
   `list` inputs a real `ListNode` — both classes are predefined, no imports needed);
3. calls your function with stdout redirected to a buffer, so stray prints are captured and
   shown per test case instead of corrupting the protocol;
4. serialises the result back to JSON and compares it.

Test inputs that would be megabytes as literal JSON — 100k-element arrays, 300x300 grids — are
stored as a compact generator spec (`{"__gen__": "ints", "n": 100000, ...}`) and expanded inside
the harness. `runners/gen.py` and `runners/gen.js` implement the same 32-bit PRNG, so both
languages see byte-identical inputs; `npm run verify:gen` checks that they still agree.

Comparison modes per problem: `exact`, `unordered` (top-level order irrelevant),
`unordered2d` (groups and their contents in any order), `approx` (float tolerance) and
`anyOf` (several accepted answers, e.g. Longest Palindromic Substring). Problems that mutate
their input in place (Move Zeroes, Rotate Image, Merge Sorted Array) declare `checkArg`, and the
judge inspects the argument instead of the return value.

Design problems (LRU Cache, Min Stack, Trie, Median Finder, ...) declare a `design` block; the
harness instantiates your class and replays an operation log, returning one result per call.
Shapes a plain array cannot express — a linked list with a cycle, two lists sharing a tail,
random pointers, a graph of `Node`s — are built by a named `prepare` step before your function
is called.

A hung solution is killed after `testTimeoutMs` and reported as a timeout rather than hanging
the editor.

## Adding your own problems

Drop a JSON file into `<workspace>/veetcode/problems/` and hit `VeetCode: Refresh Problem List`.
A file that shadows a bundled slug wins, so you can edit the built-in tests too.

```json
{
  "id": 100,
  "slug": "my-problem",
  "title": "My Problem",
  "difficulty": "Medium",
  "tags": ["Array"],
  "description": "Markdown statement.",
  "functionName": "solve",
  "params": ["nums"],
  "compare": "exact",
  "starter": { "python": "def solve(nums):\n    pass\n", "javascript": "var solve = function (nums) {};\n" },
  "tests": [{ "input": [[1, 2]], "output": 3, "sample": true }]
}
```

Optional fields: `hints`, `complexity`, `paramTypes` (`json` | `tree` | `list` | `list[]`),
`returnType`, `checkArg`, and per-test `explanation`.

The bundled bank is generated from compact definitions:

```bash
npm run problems     # tools/data_*.py + tools/cases*.py -> problems/*.json
npm run playlists    # tools/data_playlists.py -> playlists/*.json
```

Hand-written samples live in `tools/data_*.py`. The rest of each suite comes from
`tools/cases.py` and `tools/cases_sheets.py`, which produce *inputs only* — expected outputs are
computed at build time by running `tools/reference/<slug>.py`, so an answer can never drift from
the reference implementation. A case whose answer would be ambiguous (Two Sum with two valid
pairs, an alien alphabet with several valid orders) is dropped by a per-problem validator.

## Development

```bash
npm test             # compile + smoke tests + reference-solution verification
npm run verify       # run every reference solution through the real harness
npm run verify:gen   # check the Python and JavaScript input generators agree
```

`tools/reference/` holds a working solution for every bundled problem. `npm run verify` runs all
of them through the actual judge, which is what keeps the expected outputs honest — a bad test
case fails the build. `tools/smoke.js` exercises the extension modules outside the extension host
with a stubbed `vscode` API, covering scaffolding, filtering, sheets, daily stats and streaks,
editorial locking,
Markdown rendering, syntax errors, missing functions, timeouts and a missing interpreter.

## Layout

```
src/          extension host code (tree views, webview panel, runner, storage, sheets, daily stats)
runners/      harness.py / harness.js — the judge, one process per run; gen.* — input expanders
problems/     generated problem bank, one JSON file per problem
playlists/    generated DSA sheets, one JSON file per sheet
tools/        authoring + verification scripts, reference solutions, case generators, editorials
media/        panel styles, panel script, activity bar icon
```

## Why offline is the whole point

Every feature here is downstream of one decision: nothing may require a network.

- No account, no sync, no telemetry. Your solutions are files on your disk.
- The judge is `runners/harness.py` and `runners/harness.js` running as local subprocesses.
- Problem statements, hidden tests, hints and editorials all ship inside the extension.
- Aeroplane mode, a train tunnel or a hotel captive portal changes nothing about the experience.

The distraction machine only works if it can reach you. Cut the connection and the only thing left
in the window is the problem.

## Support

If this replaced a browser tab that was quietly eating your evenings, you can
[buy me a coffee](https://buymeacoffee.com/suyash2702). There is a button in the description panel
and a `VeetCode: Buy the Author a Coffee` command; that link is the only outbound URL in the whole
extension, and nothing opens it but you.
