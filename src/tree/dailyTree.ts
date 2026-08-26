import * as vscode from 'vscode';
import { DailyStore, DayRecord } from '../storage/daily';

interface Row {
  label: string;
  description: string;
  icon: vscode.ThemeIcon;
  tooltip?: string;
  children?: Row[];
}

/**
 * What you actually did today, instead of a rank against imaginary rivals:
 * solves, runs, and whether the streak survives.
 */
export class DailyTreeProvider implements vscode.TreeDataProvider<Row> {
  private readonly changeEmitter = new vscode.EventEmitter<Row | undefined>();
  readonly onDidChangeTreeData = this.changeEmitter.event;

  constructor(private readonly daily: DailyStore) {
    daily.onDidChange(() => this.refresh());
  }

  refresh(): void {
    this.changeEmitter.fire(undefined);
  }

  getChildren(element?: Row): Row[] {
    if (element) {
      return element.children ?? [];
    }
    const summary = this.daily.summary();
    const today = summary.today;

    return [
      {
        label: 'Solved today',
        description: `${today.solved}${today.solved ? '' : ' — the day is young'}`,
        icon: new vscode.ThemeIcon('pass-filled', new vscode.ThemeColor('testing.iconPassed')),
        tooltip: 'Problems that went from unsolved to solved today.',
      },
      {
        label: 'Streak',
        description: summary.streak
          ? `${summary.streak} day${summary.streak === 1 ? '' : 's'}${summary.streak >= 3 ? ' 🔥' : ''}`
          : '0 days — start one',
        icon: new vscode.ThemeIcon('flame', new vscode.ThemeColor('charts.orange')),
        tooltip:
          'Consecutive days with at least one solve. Today only breaks it once the day is over, ' +
          'so there is still time.',
      },
      {
        label: 'Best streak',
        description: `${summary.longestStreak} day${summary.longestStreak === 1 ? '' : 's'}`,
        icon: new vscode.ThemeIcon('star-full', new vscode.ThemeColor('charts.yellow')),
      },
      {
        label: 'Runs today',
        description: `${today.runs} run${today.runs === 1 ? '' : 's'} · ${today.submits} submit${
          today.submits === 1 ? '' : 's'
        }`,
        icon: new vscode.ThemeIcon('play-circle'),
        tooltip: 'Sample runs and submits, counted separately.',
      },
      {
        label: 'Time at the desk',
        description: session(today),
        icon: new vscode.ThemeIcon('watch'),
        tooltip: 'First run to last run today. Staring at the problem counts too, this just cannot see it.',
      },
      {
        label: 'Last 7 days',
        description: `${summary.weekSolved} solved · ${summary.weekRuns} runs`,
        icon: new vscode.ThemeIcon('graph'),
        children: summary.last7.map((day) => ({
          label: day.label,
          description: `${bar(day.record.solved)} ${day.record.solved} solved · ${day.record.runs} runs`,
          icon: new vscode.ThemeIcon(day.record.solved ? 'circle-filled' : 'circle-outline'),
          tooltip: day.key,
        })),
      },
      {
        label: 'All time',
        description: `${summary.totalSolved} solved · ${summary.activeDays} active day${
          summary.activeDays === 1 ? '' : 's'
        }`,
        icon: new vscode.ThemeIcon('history'),
        children: [
          {
            label: 'Submits',
            description: String(summary.totalSubmits),
            icon: new vscode.ThemeIcon('cloud-upload'),
          },
          {
            label: 'Runs',
            description: String(summary.totalRuns),
            icon: new vscode.ThemeIcon('play'),
          },
          {
            label: 'Accepted rate',
            description: summary.totalSubmits
              ? `${Math.round((summary.totalSolved / summary.totalSubmits) * 100)}%`
              : 'no submits yet',
            icon: new vscode.ThemeIcon('percentage'),
            tooltip: 'Solves divided by submits. Nobody else is looking at this number.',
          },
        ],
      },
    ];
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
    return item;
  }

  dispose(): void {
    this.changeEmitter.dispose();
  }
}

function bar(value: number, width = 6): string {
  const filled = Math.min(width, value);
  return '▇'.repeat(filled) + '·'.repeat(width - filled);
}

function session(day: DayRecord): string {
  if (day.firstAt === undefined || day.lastAt === undefined) {
    return 'not yet';
  }
  const minutes = Math.round((day.lastAt - day.firstAt) / 60000);
  if (minutes < 1) {
    return 'just started';
  }
  if (minutes < 60) {
    return `${minutes} min`;
  }
  return `${Math.floor(minutes / 60)}h ${minutes % 60}m`;
}
