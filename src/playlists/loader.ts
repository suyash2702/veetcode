import * as fs from 'fs';
import * as path from 'path';
import { ProblemBank } from '../problems/loader';
import { Problem } from '../problems/types';
import { Playlist, ResolvedPlaylist, ResolvedSection } from './types';

/**
 * Loads playlists (DSA sheets and company lists) from the bundled
 * `playlists/` directory plus a `playlists/` folder inside the user's
 * VeetCode workspace, so custom sheets need no code change.
 *
 * A sheet may list problems this build does not bundle; those slugs are
 * reported as `missing` instead of failing the load, which lets a full
 * 191-problem sheet ship before every problem behind it exists.
 */
export class PlaylistBank {
  private playlists: Playlist[] = [];
  private byId = new Map<string, Playlist>();
  /** slug -> playlist ids, so a problem can show every sheet it appears in. */
  private membership = new Map<string, string[]>();
  private loadErrors: string[] = [];

  constructor(private readonly dirs: string[]) {
    this.reload();
  }

  reload(): void {
    this.playlists = [];
    this.byId.clear();
    this.membership.clear();
    this.loadErrors = [];

    for (const dir of this.dirs) {
      if (!dir || !fs.existsSync(dir)) {
        continue;
      }
      for (const entry of fs.readdirSync(dir).sort()) {
        if (!entry.endsWith('.json')) {
          continue;
        }
        try {
          const parsed = JSON.parse(fs.readFileSync(path.join(dir, entry), 'utf8')) as Playlist;
          const playlist = validate(parsed, entry);
          // Later directories win, so a user copy can shadow a bundled sheet.
          if (this.byId.has(playlist.id)) {
            this.playlists = this.playlists.filter((p) => p.id !== playlist.id);
          }
          this.byId.set(playlist.id, playlist);
          this.playlists.push(playlist);
        } catch (err) {
          this.loadErrors.push(`${entry}: ${(err as Error).message}`);
        }
      }
    }

    this.playlists.sort((a, b) => (a.order ?? 100) - (b.order ?? 100) || a.name.localeCompare(b.name));
    for (const playlist of this.playlists) {
      for (const slug of slugsOf(playlist)) {
        const ids = this.membership.get(slug) ?? [];
        if (!ids.includes(playlist.id)) {
          ids.push(playlist.id);
        }
        this.membership.set(slug, ids);
      }
    }
  }

  all(): Playlist[] {
    return this.playlists;
  }

  get(id: string | undefined): Playlist | undefined {
    return id ? this.byId.get(id) : undefined;
  }

  /** Every playlist containing `slug` — the basis for "also in ..." hints. */
  containing(slug: string): Playlist[] {
    return (this.membership.get(slug) ?? []).map((id) => this.byId.get(id)!).filter(Boolean);
  }

  errors(): string[] {
    return this.loadErrors;
  }

  /** Pairs a sheet with the problems this build actually has. */
  resolve(playlist: Playlist, bank: ProblemBank): ResolvedPlaylist {
    const sections: ResolvedSection[] = [];
    const problems: Problem[] = [];
    const seen = new Set<string>();
    let listed = 0;
    let missing = 0;

    for (const section of playlist.sections) {
      const found: Problem[] = [];
      const gaps: string[] = [];
      for (const slug of section.slugs) {
        listed++;
        const problem = bank.get(slug);
        if (!problem) {
          gaps.push(slug);
          missing++;
          continue;
        }
        found.push(problem);
        // A sheet may repeat a problem across sections; keep the first spot.
        if (!seen.has(slug)) {
          seen.add(slug);
          problems.push(problem);
        }
      }
      sections.push({ name: section.name, problems: found, missing: gaps });
    }

    return { playlist, sections, problems, listed, missing };
  }
}

function slugsOf(playlist: Playlist): string[] {
  return playlist.sections.flatMap((section) => section.slugs);
}

function validate(playlist: Playlist, file: string): Playlist {
  for (const key of ['id', 'name', 'sections'] as (keyof Playlist)[]) {
    if (playlist[key] === undefined) {
      throw new Error(`missing "${key}" in ${file}`);
    }
  }
  if (!Array.isArray(playlist.sections) || playlist.sections.length === 0) {
    throw new Error('playlist has no sections');
  }
  playlist.kind = playlist.kind ?? 'custom';
  playlist.sections = playlist.sections.map((section) => ({
    name: section.name ?? 'Problems',
    slugs: section.slugs ?? [],
  }));
  return playlist;
}
