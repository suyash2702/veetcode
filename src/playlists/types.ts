import { Problem } from '../problems/types';

/** Curated sheets (Striver, Blind 75) and company-tagged lists. */
export type PlaylistKind = 'curated' | 'company' | 'custom';

export interface PlaylistSection {
  name: string;
  slugs: string[];
}

export interface Playlist {
  id: string;
  name: string;
  kind: PlaylistKind;
  description?: string;
  author?: string;
  /** Ordering hint for the picker; lower sorts first. */
  order?: number;
  sections: PlaylistSection[];
}

export interface ResolvedSection {
  name: string;
  problems: Problem[];
  /** Slugs the sheet lists that this build does not bundle yet. */
  missing: string[];
}

export interface ResolvedPlaylist {
  playlist: Playlist;
  sections: ResolvedSection[];
  problems: Problem[];
  /** Total slugs the sheet lists, including ones not bundled. */
  listed: number;
  missing: number;
}
