import * as vscode from 'vscode';

export type Status = 'todo' | 'attempted' | 'solved';

export interface ProblemProgress {
  status: Status;
  attempts: number;
  /** Submits that did not pass. Three of them unlock the editorial. */
  failedSubmits?: number;
  solvedAt?: number;
  lastAttemptAt?: number;
  favorite?: boolean;
  bestRuntimeMs?: number;
}

const KEY = 'veetcode.progress.v1';

/** Failed submits needed before the editorial opens up. */
export const EDITORIAL_UNLOCK_AT = 3;

export class ProgressStore {
  private readonly onChangeEmitter = new vscode.EventEmitter<void>();
  readonly onDidChange = this.onChangeEmitter.event;

  constructor(private readonly memento: vscode.Memento) {}

  private all(): Record<string, ProblemProgress> {
    return this.memento.get<Record<string, ProblemProgress>>(KEY, {});
  }

  get(slug: string): ProblemProgress {
    return this.all()[slug] ?? { status: 'todo', attempts: 0 };
  }

  /** Every recorded entry, keyed by slug — for views that aggregate across problems. */
  entries(): Record<string, ProblemProgress> {
    return this.all();
  }

  private async write(slug: string, next: ProblemProgress): Promise<void> {
    const all = { ...this.all(), [slug]: next };
    await this.memento.update(KEY, all);
    this.onChangeEmitter.fire();
  }

  async recordAttempt(slug: string, solved: boolean, runtimeMs?: number, mode: 'sample' | 'submit' = 'submit'): Promise<void> {
    const current = this.get(slug);
    const next: ProblemProgress = {
      ...current,
      attempts: current.attempts + 1,
      lastAttemptAt: Date.now(),
      // A solved problem never regresses to "attempted".
      status: solved ? 'solved' : current.status === 'solved' ? 'solved' : 'attempted',
    };
    if (mode === 'submit' && !solved) {
      next.failedSubmits = (current.failedSubmits ?? 0) + 1;
    }
    if (solved) {
      next.solvedAt = next.solvedAt ?? Date.now();
      if (runtimeMs !== undefined) {
        next.bestRuntimeMs = Math.min(runtimeMs, current.bestRuntimeMs ?? Infinity);
      }
    }
    await this.write(slug, next);
  }

  async markOpened(slug: string): Promise<void> {
    const current = this.get(slug);
    if (current.status === 'todo' && current.attempts === 0) {
      // Opening alone is not an attempt; just make sure an entry exists.
      await this.write(slug, current);
    }
  }

  /** Editorials stay locked until three submits have failed, or you solve it. */
  editorialUnlocked(slug: string): boolean {
    const entry = this.get(slug);
    return entry.status === 'solved' || (entry.failedSubmits ?? 0) >= EDITORIAL_UNLOCK_AT;
  }

  async toggleFavorite(slug: string): Promise<boolean> {
    const current = this.get(slug);
    const favorite = !current.favorite;
    await this.write(slug, { ...current, favorite });
    return favorite;
  }

  async reset(): Promise<void> {
    await this.memento.update(KEY, {});
    this.onChangeEmitter.fire();
  }

  summary(slugs: string[]): { solved: number; attempted: number; todo: number; favorites: number } {
    let solved = 0;
    let attempted = 0;
    let favorites = 0;
    for (const slug of slugs) {
      const p = this.get(slug);
      if (p.status === 'solved') {
        solved++;
      } else if (p.status === 'attempted') {
        attempted++;
      }
      if (p.favorite) {
        favorites++;
      }
    }
    return { solved, attempted, todo: slugs.length - solved - attempted, favorites };
  }

  dispose(): void {
    this.onChangeEmitter.dispose();
  }
}
