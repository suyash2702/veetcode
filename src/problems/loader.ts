import * as fs from 'fs';
import * as path from 'path';
import { Problem } from './types';

/**
 * Loads problems from the bundled `problems/` directory plus, when present,
 * a `problems/` directory inside the user's VeetCode workspace folder so that
 * custom problems can be dropped in without touching the extension.
 */
export class ProblemBank {
  private problems: Problem[] = [];
  private bySlug = new Map<string, Problem>();
  private loadErrors: string[] = [];

  constructor(private readonly dirs: string[]) {
    this.reload();
  }

  reload(): void {
    this.problems = [];
    this.bySlug.clear();
    this.loadErrors = [];

    for (const dir of this.dirs) {
      if (!dir || !fs.existsSync(dir)) {
        continue;
      }
      for (const entry of fs.readdirSync(dir).sort()) {
        if (!entry.endsWith('.json')) {
          continue;
        }
        const full = path.join(dir, entry);
        try {
          const parsed = JSON.parse(fs.readFileSync(full, 'utf8')) as Problem;
          const problem = validate(parsed, full);
          // Later directories win, so a user copy can shadow a bundled problem.
          if (this.bySlug.has(problem.slug)) {
            this.problems = this.problems.filter((p) => p.slug !== problem.slug);
          }
          this.bySlug.set(problem.slug, problem);
          this.problems.push(problem);
        } catch (err) {
          this.loadErrors.push(`${entry}: ${(err as Error).message}`);
        }
      }
    }

    this.problems.sort((a, b) => a.id - b.id);
  }

  all(): Problem[] {
    return this.problems;
  }

  get(slug: string): Problem | undefined {
    return this.bySlug.get(slug);
  }

  tags(): string[] {
    const set = new Set<string>();
    for (const p of this.problems) {
      p.tags.forEach((t) => set.add(t));
    }
    return [...set].sort();
  }

  errors(): string[] {
    return this.loadErrors;
  }
}

function validate(p: Problem, file: string): Problem {
  const required: (keyof Problem)[] = ['id', 'slug', 'title', 'difficulty', 'functionName', 'tests', 'starter'];
  for (const key of required) {
    if (p[key] === undefined) {
      throw new Error(`missing "${key}" in ${path.basename(file)}`);
    }
  }
  if (!Array.isArray(p.tests) || p.tests.length === 0) {
    throw new Error('problem has no test cases');
  }
  p.tags = p.tags ?? [];
  p.params = p.params ?? [];
  p.compare = p.compare ?? 'exact';
  // Without an explicit sample flag, treat the first two cases as samples.
  if (!p.tests.some((t) => t.sample)) {
    p.tests.slice(0, 2).forEach((t) => (t.sample = true));
  }
  return p;
}
