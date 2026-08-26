import * as vscode from 'vscode';

/** One day's activity. Runs count sample runs and submits alike. */
export interface DayRecord {
  runs: number;
  submits: number;
  solved: number;
  /** Milliseconds between the first and last activity of the day. */
  firstAt?: number;
  lastAt?: number;
}

export interface DailySummary {
  today: DayRecord;
  streak: number;
  longestStreak: number;
  activeDays: number;
  last7: { key: string; label: string; record: DayRecord }[];
  weekSolved: number;
  weekRuns: number;
  totalRuns: number;
  totalSubmits: number;
  totalSolved: number;
}

const KEY = 'veetcode.daily.v1';
const DAY_MS = 24 * 60 * 60 * 1000;
const EMPTY: DayRecord = { runs: 0, submits: 0, solved: 0 };

/** Local calendar day, so a solve at 1am counts for the day it felt like. */
export function dayKey(at: number): string {
  const date = new Date(at);
  const month = `${date.getMonth() + 1}`.padStart(2, '0');
  const day = `${date.getDate()}`.padStart(2, '0');
  return `${date.getFullYear()}-${month}-${day}`;
}

/**
 * Per-day activity, kept next to the per-problem progress. The problem store
 * only knows *that* something was solved; this knows when you showed up.
 */
export class DailyStore {
  private readonly onChangeEmitter = new vscode.EventEmitter<void>();
  readonly onDidChange = this.onChangeEmitter.event;

  constructor(private readonly memento: vscode.Memento, private readonly now: () => number = Date.now) {}

  all(): Record<string, DayRecord> {
    return this.memento.get<Record<string, DayRecord>>(KEY, {});
  }

  get(key: string): DayRecord {
    return this.all()[key] ?? { ...EMPTY };
  }

  async record(kind: 'sample' | 'submit', solved: boolean): Promise<void> {
    const at = this.now();
    const key = dayKey(at);
    const days = { ...this.all() };
    const current = { ...(days[key] ?? { ...EMPTY }) };
    current.runs += 1;
    if (kind === 'submit') {
      current.submits += 1;
    }
    if (solved) {
      current.solved += 1;
    }
    current.firstAt = current.firstAt ?? at;
    current.lastAt = at;
    days[key] = current;
    await this.memento.update(KEY, days);
    this.onChangeEmitter.fire();
  }

  async reset(): Promise<void> {
    await this.memento.update(KEY, {});
    this.onChangeEmitter.fire();
  }

  summary(): DailySummary {
    const days = this.all();
    const now = this.now();
    const todayKey = dayKey(now);

    const last7: DailySummary['last7'] = [];
    for (let back = 6; back >= 0; back--) {
      const at = now - back * DAY_MS;
      const key = dayKey(at);
      last7.push({
        key,
        label: back === 0 ? 'Today' : new Date(at).toLocaleDateString(undefined, { weekday: 'short' }),
        record: days[key] ?? { ...EMPTY },
      });
    }

    const solvedDays = new Set(Object.keys(days).filter((key) => (days[key]?.solved ?? 0) > 0));

    // Today counts once it has a solve, but an empty today does not break a
    // streak that is still alive from yesterday.
    let cursor = solvedDays.has(todayKey) ? now : now - DAY_MS;
    let current = 0;
    while (solvedDays.has(dayKey(cursor))) {
      current++;
      cursor -= DAY_MS;
    }

    let longest = 0;
    for (const key of solvedDays) {
      const previous = dayKey(new Date(`${key}T12:00:00`).getTime() - DAY_MS);
      if (solvedDays.has(previous)) {
        continue; // not the start of a run
      }
      let run = 0;
      let at = new Date(`${key}T12:00:00`).getTime();
      while (solvedDays.has(dayKey(at))) {
        run++;
        at += DAY_MS;
      }
      longest = Math.max(longest, run);
    }

    const totals = Object.values(days).reduce(
      (acc, day) => ({
        runs: acc.runs + day.runs,
        submits: acc.submits + day.submits,
        solved: acc.solved + day.solved,
      }),
      { runs: 0, submits: 0, solved: 0 }
    );

    return {
      today: days[todayKey] ?? { ...EMPTY },
      streak: current,
      longestStreak: Math.max(longest, current),
      activeDays: Object.keys(days).length,
      last7,
      weekSolved: last7.reduce((sum, day) => sum + day.record.solved, 0),
      weekRuns: last7.reduce((sum, day) => sum + day.record.runs, 0),
      totalRuns: totals.runs,
      totalSubmits: totals.submits,
      totalSolved: totals.solved,
    };
  }

  dispose(): void {
    this.onChangeEmitter.dispose();
  }
}
