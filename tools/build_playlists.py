#!/usr/bin/env python3
"""Authoring script: writes playlists/*.json from tools/data_playlists.py.

Run:  python3 tools/build_playlists.py

Reports slugs a sheet lists that problems/ does not contain yet — that is
expected while the bank is still growing, and the extension shows them as
"not bundled" rather than hiding the gap.
"""

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "playlists")

sys.path.insert(0, HERE)

import data_playlists  # noqa: E402


def bundled_slugs():
    slugs = set()
    for path in glob.glob(os.path.join(ROOT, "problems", "*.json")):
        with open(path, encoding="utf8") as fh:
            slugs.add(json.load(fh)["slug"])
    return slugs


def main():
    os.makedirs(OUT, exist_ok=True)
    have = bundled_slugs()
    listed = set()
    seen_ids = set()

    for sheet in data_playlists.PLAYLISTS:
        if sheet["id"] in seen_ids:
            raise SystemExit("duplicate playlist id: " + sheet["id"])
        seen_ids.add(sheet["id"])
        for section in sheet["sections"]:
            listed.update(section["slugs"])
        path = os.path.join(OUT, "{}.json".format(sheet["id"]))
        with open(path, "w", encoding="utf8") as fh:
            json.dump(sheet, fh, indent=2, ensure_ascii=False)
            fh.write("\n")

    missing = sorted(listed - have)
    unlisted = sorted(have - listed)
    print("wrote {} sheets to {}".format(len(data_playlists.PLAYLISTS), OUT))
    print("{} distinct problems listed, {} bundled, {} still to author".format(
        len(listed), len(listed & have), len(missing)))
    if unlisted:
        print("bundled but on no sheet: {}".format(", ".join(unlisted)))
    if missing:
        print("\nnot bundled yet:")
        for slug in missing:
            print("  " + slug)


if __name__ == "__main__":
    main()
