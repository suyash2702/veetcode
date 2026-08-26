import * as vscode from 'vscode';
import { PlaylistBank } from '../playlists/loader';
import { ResolvedPlaylist } from '../playlists/types';
import { ProblemBank } from '../problems/loader';
import { Difficulty, Problem } from '../problems/types';
import { ProgressStore } from '../storage/progress';

interface Row {
  label: string;
  description: string;
  icon: vscode.ThemeIcon;
  tooltip?: string;
  command?: vscode.Command;
  children?: Row[];
}

const DIFFICULTIES: Difficulty[] = ['Easy', 'Medium', 'Hard'];

const DIFFICULTY_COLOR: Record<Difficulty, string> = {
  Easy: 'charts.green',
  Medium: 'charts.yellow',
  Hard: 'charts.red',
};

/**
 * Read-only summary view: how much of the bank — or of the selected sheet —
 * is solved, plus one line per sheet so shared problems are visible as the
 * progress they already are.
 */
export class StatsTreeProvider implements vscode.TreeDataProvider<Row> {
  private readonly changeEmitter = new vscode.EventEmitter<Row | undefined>();
  readonly onDidChangeTreeData = this.changeEmitter.event;

  constructor(
    private readonly bank: ProblemBank,
    private readonly progress: ProgressStore,
    private readonly playlists: PlaylistBank,
    private readonly active: () => ResolvedPlaylist | undefined
  ) {
    progress.onDidChange(() => this.refresh());
  }

  refresh(): void {
    this.changeEmitter.fire(undefined);
  }

  getChildren(element?: Row): Row[] {
    if (element) {
      return element.children ?? [];
    }

    const active = this.active();
    const scope: Problem[] = active ? active.problems : this.bank.all();
    const summary = this.progress.summary(scope.map((p) => p.slug));

    const rows: Row[] = [
      {
        label: active ? active.playlist.name : 'Solved',
        description: `${summary.solved} / ${scope.length}  ${bar(summary.solved, scope.length)}`,
        icon: new vscode.ThemeIcon('pass-filled', new vscode.ThemeColor('testing.iconPassed')),
        tooltip: active
          ? `${active.playlist.name}: ${summary.solved} of ${scope.length} bundled problems solved` +
            (active.missing ? `, ${active.missing} listed but not bundled yet` : '')
          : undefined,
      },
    ];

    for (const difficulty of DIFFICULTIES) {
      const subset = scope.filter((p) => p.difficulty === difficulty);
      if (!subset.length) {
        continue;
      }
      const solved = subset.filter((p) => this.progress.get(p.slug).status === 'solved').length;
      rows.push({
        label: difficulty,
        description: `${solved} / ${subset.length}  ${bar(solved, subset.length)}`,
        icon: new vscode.ThemeIcon('circle-filled', new vscode.ThemeColor(DIFFICULTY_COLOR[difficulty])),
      });
    }

    rows.push({
      label: 'In progress',
      description: String(summary.attempted),
      icon: new vscode.ThemeIcon('circle-large-outline'),
    });
    rows.push({
      label: 'Favorites',
      description: String(summary.favorites),
      icon: new vscode.ThemeIcon('star-full'),
    });

    const sheets = this.playlists.all();
    if (sheets.length) {
      rows.push({
        label: 'Sheets',
        description: `${sheets.length}`,
        icon: new vscode.ThemeIcon('list-unordered'),
        children: sheets.map((playlist) => {
          const resolved = this.playlists.resolve(playlist, this.bank);
          const solved = resolved.problems.filter((p) => this.progress.get(p.slug).status === 'solved').length;
          const isActive = active?.playlist.id === playlist.id;
          return {
            label: playlist.name,
            description: `${solved} / ${resolved.problems.length}  ${bar(solved, resolved.problems.length)}`,
            icon: isActive
              ? new vscode.ThemeIcon('check', new vscode.ThemeColor('testing.iconPassed'))
              : new vscode.ThemeIcon(playlist.kind === 'company' ? 'briefcase' : 'book'),
            tooltip:
              `${playlist.name}${playlist.author ? ` — by ${playlist.author}` : ''}\n` +
              (isActive ? 'Active sheet.\n' : 'Click to show this sheet in the Problems view.\n') +
              `Solving a problem counts here and in every other sheet that lists it.` +
              (resolved.missing ? `\n${resolved.missing} of ${resolved.listed} listed problems are not bundled yet.` : ''),
            command: {
              command: 'veetcode.setPlaylist',
              title: `Show ${playlist.name}`,
              arguments: [playlist.id],
            },
          };
        }),
      });
    }

    return rows;
  }

  getTreeItem(row: Row): vscode.TreeItem {
    const item = new vscode.TreeItem(
      row.label,
      row.children?.length ? vscode.TreeItemCollapsibleState.Collapsed : vscode.TreeItemCollapsibleState.None
    );
    item.description = row.description;
    item.iconPath = row.icon;
    if (row.tooltip) {
      item.tooltip = row.tooltip;
    }
    if (row.command) {
      item.command = row.command;
    }
    return item;
  }

  dispose(): void {
    this.changeEmitter.dispose();
  }
}

function bar(value: number, total: number, width = 10): string {
  if (total === 0) {
    return '';
  }
  const filled = Math.round((value / total) * width);
  return '█'.repeat(filled) + '░'.repeat(width - filled);
}
