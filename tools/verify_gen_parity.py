#!/usr/bin/env python3
"""Checks that runners/gen.py and runners/gen.js expand specs identically.

Expected outputs in problems/*.json are computed with the Python expander, so
any divergence would silently fail every generated case in JavaScript.

Usage: python3 tools/verify_gen_parity.py
"""

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "runners"))

from gen import expand  # noqa: E402

SPECS = [
    {"__gen__": "ints", "n": 50, "lo": -1000, "hi": 1000, "seed": 1},
    {"__gen__": "ints", "n": 5, "lo": 0, "hi": 0, "seed": 2},
    {"__gen__": "sorted", "n": 40, "lo": -50, "hi": 50, "seed": 3},
    {"__gen__": "sorted", "n": 40, "lo": 0, "hi": 10, "seed": 4, "unique": True, "step": 3},
    {"__gen__": "sorted", "n": 20, "lo": 0, "hi": 99, "seed": 5, "desc": True},
    {"__gen__": "perm", "n": 60, "seed": 6},
    {"__gen__": "perm", "n": 10, "base": 1, "seed": 7},
    {"__gen__": "string", "n": 80, "seed": 8},
    {"__gen__": "string", "n": 40, "alphabet": "()[]{}", "seed": 9},
    {"__gen__": "grid", "rows": 6, "cols": 7, "lo": -9, "hi": 9, "seed": 10},
    {"__gen__": "grid", "rows": 5, "cols": 5, "alphabet": "01", "asString": False, "seed": 11},
    {"__gen__": "pairs", "n": 12, "lo": -20, "hi": 20, "seed": 12},
    {"__gen__": "repeat", "value": 7, "n": 9},
    {"__gen__": "arange", "n": 15, "start": -7, "step": 3},
    {"__gen__": "words", "n": 20, "minLen": 1, "maxLen": 5, "alphabet": "abc", "seed": 13},
    {"__gen__": "edges", "n": 30, "nodes": 10, "seed": 14},
    {"__gen__": "edges", "n": 30, "nodes": 10, "seed": 15, "dag": True},
    {"__gen__": "intervals", "n": 12, "lo": 0, "hi": 40, "maxLen": 6, "seed": 16},
    {"__gen__": "disjoint", "n": 12, "gap": 4, "maxLen": 3, "seed": 17},
    {"__gen__": "sortedgrid", "rows": 4, "cols": 5, "start": -3, "step": 6, "seed": 18},
    {"__gen__": "strrepeat", "value": "ab", "n": 12},
    {"__gen__": "shuffle", "of": {"__gen__": "arange", "n": 30}, "seed": 19},
    {"__gen__": "rotate", "of": {"__gen__": "arange", "n": 25}, "by": 7},
    {"__gen__": "concat", "parts": [{"__gen__": "arange", "n": 5},
                                    {"__gen__": "repeat", "value": 0, "n": 3},
                                    [99]]},
    {"__gen__": "concat", "parts": [{"__gen__": "strrepeat", "value": "(", "n": 4},
                                    {"__gen__": "strrepeat", "value": ")", "n": 4}]},
    {"__gen__": "zipsum", "parts": [{"__gen__": "arange", "n": 8},
                                    {"__gen__": "ints", "n": 8, "lo": 1, "hi": 9, "seed": 21}]},
    {"__gen__": "duplicate", "of": {"__gen__": "arange", "n": 6}, "times": 3},
    {"__gen__": "sortof", "of": {"__gen__": "ints", "n": 12, "lo": -9, "hi": 9, "seed": 22}},
    {"__gen__": "without", "of": {"__gen__": "arange", "n": 10}, "value": 4},
    {"__gen__": "wedges", "n": 10, "nodes": 6, "seed": 23, "lo": 1, "hi": 50},
    {"__gen__": "wedges", "n": 4, "nodes": 6, "seed": 24, "connected": True},
    {"__gen__": "oplog", "cls": "MinStack", "n": 20, "seed": 29, "part": "ops",
     "methods": [{"name": "push", "args": [{"int": [-5, 5]}], "delta": 1, "weight": 3},
                 {"name": "pop", "delta": -1, "needs": 1},
                 {"name": "getMin", "needs": 1}]},
    {"__gen__": "oplog", "cls": "MinStack", "n": 20, "seed": 29, "part": "args",
     "methods": [{"name": "push", "args": [{"int": [-5, 5]}], "delta": 1, "weight": 3},
                 {"name": "pop", "delta": -1, "needs": 1},
                 {"name": "getMin", "needs": 1}]},
    {"__gen__": "oplog", "cls": "Trie", "n": 10, "seed": 30, "part": "ops",
     "methods": [{"name": "insert", "args": [{"word": {"minLen": 1, "maxLen": 4, "alphabet": "abc"}}]},
                 {"name": "search", "args": [{"word": {"minLen": 1, "maxLen": 4, "alphabet": "abc"}}]}]},
    {"__gen__": "adj", "n": 12, "nodes": 7, "seed": 27},
    {"__gen__": "adj", "n": 12, "nodes": 7, "seed": 28, "directed": True},
    {"__gen__": "knows", "n": 7, "seed": 25},
    {"__gen__": "knows", "n": 7, "seed": 26, "celebrity": 3},
    [1, {"__gen__": "ints", "n": 4, "lo": 1, "hi": 5, "seed": 20}, "x"],
]


def main():
    script = (
        "const {expand} = require(" + json.dumps(os.path.join(ROOT, "runners", "gen.js")) + ");"
        "const specs = JSON.parse(process.argv[1]);"
        "process.stdout.write(JSON.stringify(specs.map(expand)));"
    )
    proc = subprocess.run(["node", "-e", script, json.dumps(SPECS)], capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stderr.strip())
        return 1

    js = json.loads(proc.stdout)
    failures = 0
    for spec, produced in zip(SPECS, js):
        expected = expand(spec)
        if expected != produced:
            failures += 1
            name = spec.get("__gen__", "nested") if isinstance(spec, dict) else "nested"
            print("MISMATCH {}: python={} js={}".format(name, json.dumps(expected)[:120],
                                                        json.dumps(produced)[:120]))
    print("{} generator specs checked, {} mismatching".format(len(SPECS), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
