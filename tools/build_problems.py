#!/usr/bin/env python3
"""Authoring script: turns the compact problem definitions in tools/data_*.py
into one JSON file per problem under problems/.

Run:  python3 tools/build_problems.py
"""

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "problems")

sys.path.insert(0, HERE)

import data_easy      # noqa: E402
import data_medium    # noqa: E402
import data_advanced  # noqa: E402
import data_sheet_arrays  # noqa: E402
import data_sheet_lists   # noqa: E402
import data_sheet_trees   # noqa: E402
import data_sheet_bst     # noqa: E402
import data_sheet_search  # noqa: E402
import data_sheet_dp      # noqa: E402
import data_sheet_graphs  # noqa: E402
import data_sheet_stacks  # noqa: E402
import data_sheet_backtracking  # noqa: E402
import data_sheet_strings # noqa: E402
import cases          # noqa: E402
import editorials     # noqa: E402
import cases_sheets   # noqa: E402  (registers into cases.REGISTRY)
import oracle         # noqa: E402

# Total cases kept per problem: the hand-written ones first, then generated
# cases spread evenly across the sizes tools/cases.py produces.
MAX_TESTS = int(os.environ.get("VEETCODE_MAX_TESTS", "35"))
# A whole submit runs in one process under veetcode.testTimeoutMs, so the
# reference suite has to stay comfortably inside that budget.
SLOW_SUITE_SECONDS = 3.0
# Inputs compress to a generator spec, but expected outputs are stored
# literally, so a case whose answer is itself a huge array is dropped rather
# than shipped inside the extension.
MAX_OUTPUT_CHARS = 60000

JS_TYPE_COMMENT = {
    "tree": "TreeNode",
    "list": "ListNode",
    "list[]": "ListNode[]",
}


def design_python_starter(p):
    design = p["design"]
    lines = ["class {}:".format(design["className"])]
    for method in design["methods"]:
        name = "__init__" if method["name"] == design["className"] else method["name"]
        params = ", ".join(["self"] + method["params"])
        lines.append("    def {}({}):".format(name, params))
        lines.append("        # TODO: implement")
        lines.append("        pass")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def design_js_starter(p):
    design = p["design"]
    cls = design["className"]
    out = []
    for method in design["methods"]:
        params = ", ".join(method["params"])
        doc = ["/**"] + [" * @param {*} " + name for name in method["params"]] + [" */"]
        out.append("\n".join(doc))
        if method["name"] == cls:
            out.append("var {} = function ({}) {{\n  // TODO: implement\n}};\n".format(cls, params))
        else:
            out.append("{}.prototype.{} = function ({}) {{\n  // TODO: implement\n}};\n".format(
                cls, method["name"], params))
    return "\n".join(out)


def python_starter(p):
    if p.get("design"):
        return design_python_starter(p)
    lines = []
    for i, kind in enumerate(p.get("paramTypes", [])):
        if kind in ("tree", "list", "list[]"):
            lines.append(
                "# {} is a {} built for you; the class is already defined.".format(
                    p["params"][i], JS_TYPE_COMMENT[kind]
                )
            )
    if p.get("returnType") in ("tree", "list", "list[]"):
        lines.append("# Return a {} - it is serialised back for you.".format(JS_TYPE_COMMENT[p["returnType"]]))
    header = "\n".join(lines)
    body = p.get("pyBody", "    # TODO: implement\n    pass")
    sig = "def {}({}):".format(p["functionName"], ", ".join(p["params"]))
    return ("{}\n{}\n{}\n".format(header, sig, body) if header else "{}\n{}\n".format(sig, body))


def js_starter(p):
    if p.get("design"):
        return design_js_starter(p)
    doc = ["/**"]
    for i, name in enumerate(p["params"]):
        kind = (p.get("paramTypes") or [None] * len(p["params"]))[i] if p.get("paramTypes") else None
        doc.append(" * @param {{{}}} {}".format(JS_TYPE_COMMENT.get(kind, "*"), name))
    doc.append(" * @return {{{}}}".format(JS_TYPE_COMMENT.get(p.get("returnType"), "*")))
    doc.append(" */")
    body = p.get("jsBody", "  // TODO: implement")
    return "{}\nvar {} = function ({}) {{\n{}\n}};\n".format(
        "\n".join(doc), p["functionName"], ", ".join(p["params"]), body
    )


def spread(items, count):
    """Evenly sample `count` items, keeping the first and the last."""
    if count >= len(items):
        return items
    if count <= 1:
        return items[:count]
    step = (len(items) - 1) / (count - 1)
    return [items[int(round(i * step))] for i in range(count)]


def generated_tests(problem, budget, report):
    """Runs the reference solution over tools/cases.py inputs for this problem."""
    entry = cases.REGISTRY.get(problem["slug"])
    if entry is None or budget <= 0:
        return []

    seen = {json.dumps(t["input"], sort_keys=True) for t in problem["tests"]}
    built = []
    total = 0.0
    for raw in entry["make"]():
        key = json.dumps(raw, sort_keys=True)
        if key in seen:
            continue
        try:
            expected, args, elapsed = oracle.solve(problem, raw)
        except Exception as err:  # a generator that violates the problem's own constraints
            report.append("  ! {}: case dropped ({}: {})".format(problem["slug"], type(err).__name__, err))
            continue
        if entry["validate"] and not entry["validate"](args, expected):
            continue
        if entry["expected"]:
            expected = entry["expected"](args)
        if len(json.dumps(expected)) > MAX_OUTPUT_CHARS:
            continue
        seen.add(key)
        total += elapsed
        built.append({"input": raw, "output": expected})

    kept = spread(built, budget)
    if total > SLOW_SUITE_SECONDS:
        report.append("  ! {}: reference needs {:.1f}s for {} generated cases".format(
            problem["slug"], total, len(built)))
    return kept


def editorial_for(problem):
    """Explanation from tools/editorials.py, code from the verified reference."""
    slug = problem["slug"]
    explanation = editorials.EDITORIALS.get(slug)
    if not explanation:
        return None
    code = {}
    for language, extension in (("python", "py"), ("javascript", "js")):
        path = os.path.join(HERE, "reference", "{}.{}".format(slug, extension))
        if os.path.exists(path):
            with open(path, encoding="utf8") as fh:
                code[language] = fh.read().rstrip() + "\n"
    out = {"explanation": explanation.strip(), "code": code}
    if problem.get("complexity"):
        out["complexity"] = problem["complexity"]
    return out


def build(p):
    out = {
        "id": p["id"],
        "slug": p["slug"],
        "title": p["title"],
        "difficulty": p["difficulty"],
        "tags": p["tags"],
        "description": p["description"].strip(),
        "functionName": p["functionName"],
        "params": p["params"],
        "tests": p["tests"],
    }
    for key in ("hints", "paramTypes", "returnType", "checkArg", "compare", "complexity", "design", "prepare"):
        if p.get(key) is not None:
            out[key] = p[key]
    out["starter"] = {"python": python_starter(p), "javascript": js_starter(p)}
    editorial = editorial_for(out)
    if editorial:
        out["editorial"] = editorial
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    problems = (data_easy.PROBLEMS + data_medium.PROBLEMS + data_advanced.PROBLEMS
                + data_sheet_arrays.PROBLEMS + data_sheet_lists.PROBLEMS
                + data_sheet_trees.PROBLEMS + data_sheet_bst.PROBLEMS
                + data_sheet_search.PROBLEMS + data_sheet_dp.PROBLEMS
                + data_sheet_graphs.PROBLEMS + data_sheet_stacks.PROBLEMS
                + data_sheet_backtracking.PROBLEMS + data_sheet_strings.PROBLEMS)
    seen = set()
    report = []
    counts = []
    started = time.perf_counter()

    for p in problems:
        if p["slug"] in seen:
            raise SystemExit("duplicate slug: " + p["slug"])
        seen.add(p["slug"])
        built = build(p)
        built["tests"].extend(generated_tests(built, MAX_TESTS - len(built["tests"]), report))
        counts.append((len(built["tests"]), p["slug"]))
        path = os.path.join(OUT, "{:03d}-{}.json".format(p["id"], p["slug"]))
        with open(path, "w", encoding="utf8") as fh:
            # Compact: these files are generated, and indenting 100k-element
            # arrays one number per line multiplies the shipped size by five.
            json.dump(built, fh, ensure_ascii=False, separators=(",", ":"))
            fh.write("\n")

    without_editorial = sorted(p["slug"] for p in problems if p["slug"] not in editorials.EDITORIALS)
    if without_editorial:
        print("no editorial for {} problem(s): {}".format(
            len(without_editorial), ", ".join(without_editorial[:12]) + ("..." if len(without_editorial) > 12 else "")))

    thin = [c for c in counts if c[0] < MAX_TESTS]
    print("wrote {} problems to {} in {:.1f}s ({} tests total)".format(
        len(problems), OUT, time.perf_counter() - started, sum(c[0] for c in counts)))
    if thin:
        print("below {} tests: {}".format(MAX_TESTS, ", ".join("{} ({})".format(s, n) for n, s in sorted(thin))))
    for line in report:
        print(line)


if __name__ == "__main__":
    main()
