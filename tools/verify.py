#!/usr/bin/env python3
"""Runs every reference solution through the real harness and reports failures.

Usage: python3 tools/verify.py [python|javascript]
"""

import glob
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PREFIX = "__VEETCODE_RESULT__"


def run(problem, language):
    ext = "py" if language == "python" else "js"
    solution = os.path.join(HERE, "reference", "{}.{}".format(problem["slug"], ext))
    if not os.path.exists(solution):
        return None
    payload = {
        "solutionPath": solution,
        "functionName": problem["functionName"],
        "paramTypes": problem.get("paramTypes", []),
        "returnType": problem.get("returnType", "json"),
        "checkArg": problem.get("checkArg"),
        "compare": problem.get("compare", "exact"),
        "design": problem.get("design"),
        "prepare": problem.get("prepare"),
        "timeoutMs": 10000,
        "tests": [{"input": t["input"], "output": t["output"]} for t in problem["tests"]],
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        json.dump(payload, fh)
        payload_path = fh.name
    try:
        harness = os.path.join(ROOT, "runners", "harness.py" if language == "python" else "harness.js")
        cmd = ["python3", harness, payload_path] if language == "python" else ["node", harness, payload_path]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    finally:
        os.unlink(payload_path)

    line = next((l for l in proc.stdout.splitlines() if l.startswith(PREFIX)), None)
    if not line:
        return {"compileError": (proc.stderr or proc.stdout).strip() or "no harness output", "results": []}
    return json.loads(line[len(PREFIX):])


def main():
    language = sys.argv[1] if len(sys.argv) > 1 else "python"
    failures = 0
    checked = 0
    skipped = []

    for path in sorted(glob.glob(os.path.join(ROOT, "problems", "*.json"))):
        problem = json.load(open(path, encoding="utf8"))
        out = run(problem, language)
        if out is None:
            skipped.append(problem["slug"])
            continue
        checked += 1
        if out.get("compileError"):
            failures += 1
            print("LOAD FAIL {}: {}".format(problem["slug"], out["compileError"].splitlines()[-1]))
            continue
        bad = [r for r in out["results"] if not r["passed"]]
        if bad:
            failures += 1
            print("FAIL {} ({}/{} passed)".format(problem["slug"], len(out["results"]) - len(bad), len(out["results"])))
            for r in bad[:3]:
                test = problem["tests"][r["index"]]
                print("   case {} input={}".format(r["index"] + 1, json.dumps(test["input"])[:120]))
                print("     expected={}".format(json.dumps(test["output"])[:120]))
                if r.get("error"):
                    print("     error={}".format(r["error"].splitlines()[-1]))
                else:
                    print("     actual  ={}".format(json.dumps(r.get("actual"))[:120]))
        else:
            spent = sum(r.get("runtimeMs", 0) for r in out["results"])
            flag = "  <-- slow" if spent > 4000 else ""
            print("ok   {} ({} tests, {:.0f} ms){}".format(problem["slug"], len(out["results"]), spent, flag))

    print("\n{}: {} problems checked, {} failing, {} without a {} reference".format(
        language, checked, failures, len(skipped), language))
    if skipped:
        print("   skipped: " + ", ".join(skipped))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
