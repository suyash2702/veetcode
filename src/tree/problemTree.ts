import * as vscode from 'vscode';
import { PlaylistBank } from '../playlists/loader';
import { ResolvedPlaylist } from '../playlists/types';
import { ProblemBank } from '../problems/loader';
import { Difficulty, Problem } from '../problems/types';
import { ProgressStore, Status } from '../storage/progress';

export type GroupBy = 'section' | 'difficulty' | 'topic' | 'status' | 'none';

export interface Filters {
  difficulty?: Difficulty;
  tag?: string;
  status?: Status | 'favorites';
  search?: string;
}

type Node = GroupNode | ProblemNode;

interface GroupNode {
  kind: 'group';
  label: string;
  problems: Problem[];
  /** Slugs the active sheet lists that this build does not bundle yet. */
  missing?: number;
}

interface ProblemNode {
  kind: 'problem';
  problem: Problem;
}

const DIFFICULTY_ORDER: Difficulty[] = ['Easy', 'Medium', 'Hard'];

const STATUS_ICON: Record<Status, vscode.ThemeIcon> = {
  solved: new vscode.ThemeIcon('pass-filled', new vscode.ThemeColor('testing.iconPassed')),
  attempted: new vscode.ThemeIcon('circle-large-outline', new vscode.ThemeColor('testing.iconQueued')),
  todo: new vscode.ThemeIcon('circle-outline'),
};

const DIFFICULTY_COLOR: Record<Difficulty, string> = {
  Easy: 'charts.green',
  Medium: 'charts.yellow',
  Hard: 'charts.red',
};

export class ProblemTreeProvider implements vscode.TreeDataProvider<Node> {
  private readonly changeEmitter = new vscode.EventEmitter<Node | undefined>();
  readonly onDidChangeTreeData = this.changeEmitter.event;

  private filters: Filters = {};
  private groupBy: GroupBy = 'difficulty';
  private activePlaylistId: string | undefined;

  constructor(
    private readonly bank: ProblemBank,
    private readonly progress: ProgressStore,
    private readonly playlists: PlaylistBank
  ) {}

  refresh(): void {
    this.changeEmitter.fire(undefined);
  }

  getFilters(): Filters {
    return this.filters;
  }

  setFilter<K extends keyof Filters>(key: K, value: Filters[K]): void {
    this.filters[key] = value;
    this.refresh();
  }

  clearFilters(): void {
    this.filters = {};
    this.refresh();
  }

  setGroupBy(groupBy: GroupBy): void {
    this.groupBy = groupBy;
    this.refresh();
  }

  getGroupBy(): GroupBy {
    return this.groupBy;
  }

  /**
   * Narrows the tree to one sheet. Sheets are ordered lists, so grouping
   * switches to the sheet's own sections — and back to difficulty when the
   * sheet is cleared.
   */
  setPlaylist(id: string | undefined): void {
    this.activePlaylistId = id;
    this.groupBy = id ? 'section' : 'difficulty';
    this.refresh();
  }

  activePlaylist(): ResolvedPlaylist | undefined {
    const playlist = this.playlists.get(this.activePlaylistId);
    return playlist ? this.playlists.resolve(playlist, this.bank) : undefined;
  }

  /** Problems left after the active sheet and filters, in list order. */
  visibleProblems(): Problem[] {
    const active = this.activePlaylist();
    const pool = active ? active.problems : this.bank.all();
    return pool.filter((p) => this.matches(p));
  }

  private matches(problem: Problem): boolean {
    const { difficulty, tag, status, search } = this.filters;
    if (difficulty && problem.difficulty !== difficulty) {
      return false;
    }
    if (tag && !problem.tags.includes(tag)) {
      return false;
    }
    if (status) {
      const entry = this.progress.get(problem.slug);
      if (status === 'favorites' ? !entry.favorite : entry.status !== status) {
        return false;
      }
    }
    if (search) {
      const haystack = `${problem.id} ${problem.title} ${problem.slug} ${problem.tags.join(' ')}`.toLowerCase();
      if (!haystack.includes(search.toLowerCase())) {
        return false;
      }
    }
    return true;
  }

  getChildren(element?: Node): Node[] {
    if (element?.kind === 'group') {
      return element.problems.map((problem) => ({ kind: 'problem', problem }));
    }
    if (element?.kind === 'problem') {
      return [];
    }

    const active = this.activePlaylist();
    if (this.groupBy === 'section') {
      if (!active) {
        // No sheet selected: fall back to the plain list.
        return this.visibleProblems().map((problem) => ({ kind: 'problem', problem }));
      }
      return active.sections
        .map((section) => ({
          kind: 'group' as const,
          label: section.name,
          problems: section.problems.filter((p) => this.matches(p)),
          missing: section.missing.length,
        }))
        .filter((group) => group.problems.length > 0 || group.missing > 0);
    }

    const problems = this.visibleProblems();
    if (this.groupBy === 'none') {
      return problems.map((problem) => ({ kind: 'problem', problem }));
    }
    return this.groups(problems);
  }

  private groups(problems: Problem[]): Node[] {
    const buckets = new Map<string, Problem[]>();
    const push = (key: string, p: Problem) => {
      const list = buckets.get(key) ?? [];
      list.push(p);
      buckets.set(key, list);
    };

    for (const p of problems) {
      if (this.groupBy === 'difficulty') {
        push(p.difficulty, p);
      } else if (this.groupBy === 'status') {
        push(this.progress.get(p.slug).status, p);
      } else {
        (p.tags.length ? p.tags : ['Untagged']).forEach((t) => push(t, p));
      }
    }

    const keys = [...buckets.keys()];
    if (this.groupBy === 'difficulty') {
      keys.sort((a, b) => DIFFICULTY_ORDER.indexOf(a as Difficulty) - DIFFICULTY_ORDER.indexOf(b as Difficulty));
    } else if (this.groupBy === 'status') {
      const order = ['todo', 'attempted', 'solved'];
      keys.sort((a, b) => order.indexOf(a) - order.indexOf(b));
    } else {
      keys.sort();
    }

    return keys.map((label) => ({ kind: 'group', label, problems: buckets.get(label)! }));
  }

  getTreeItem(node: Node): vscode.TreeItem {
    if (node.kind === 'group') {
      const solved = node.problems.filter((p) => this.progress.get(p.slug).status === 'solved').length;
      const item = new vscode.TreeItem(capitalize(node.label), vscode.TreeItemCollapsibleState.Expanded);
      item.description = `${solved}/${node.problems.length}` + (node.missing ? ` (+${node.missing} soon)` : '');
      item.contextValue = 'group';
      if (this.groupBy === 'difficulty') {
        item.iconPath = new vscode.ThemeIcon(
          'circle-filled',
          new vscode.ThemeColor(DIFFICULTY_COLOR[node.label as Difficulty] ?? 'foreground')
        );
      }
      if (node.missing) {
        item.tooltip = new vscode.MarkdownString(
          `${node.missing} problem(s) in this section are listed by the sheet but not bundled in this build yet.`
        );
      }
      return item;
    }

    const { problem } = node;
    const entry = this.progress.get(problem.slug);
    // No explicit id: grouping by topic puts the same problem under several
    // parents, and duplicate TreeItem ids are rejected by VS Code.
    const item = new vscode.TreeItem(`${problem.id}. ${problem.title}`, vscode.TreeItemCollapsibleState.None);
    item.iconPath = STATUS_ICON[entry.status];
    item.description = [entry.favorite ? '★' : '', problem.difficulty].filter(Boolean).join(' ');
    item.contextValue = entry.favorite ? 'problem.favorite' : 'problem';

    // Progress is keyed by problem, not by sheet: solving it once marks it
    // solved everywhere it appears, so say where else that lands.
    const alsoIn = this.playlists
      .containing(problem.slug)
      .filter((p) => p.id !== this.activePlaylistId)
      .map((p) => p.name);

    item.tooltip = new vscode.MarkdownString(
      [
        `**${problem.id}. ${problem.title}** — ${problem.difficulty}`,
        problem.tags.length ? `_${problem.tags.join(', ')}_` : '',
        '',
        `Status: ${entry.status}${entry.attempts ? ` · ${entry.attempts} attempt(s)` : ''}`,
        problem.complexity ? `Target: ${problem.complexity}` : '',
        alsoIn.length ? `Also in: ${alsoIn.join(', ')}` : '',
      ]
        .filter(Boolean)
        .join('\n\n')
    );
    item.command = {
      command: 'veetcode.openProblem',
      title: 'Open Problem',
      arguments: [problem.slug],
    };
    return item;
  }

  dispose(): void {
    this.changeEmitter.dispose();
  }
}

function capitalize(value: string): string {
  return value.charAt(0).toUpperCase() + value.slice(1);
}
