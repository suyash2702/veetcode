"""Computes expected outputs by running tools/reference/<slug>.py.

The reference solution is the single source of truth for every generated
test, and it is exercised through the same marshalling the real harness
uses, so a case that builds here behaves identically in the extension.
"""

import copy
import importlib.util
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "runners"))

import harness  # noqa: E402  (marshalling + JSON normalisation, and TreeNode/ListNode builtins)
from gen import expand  # noqa: E402

_loaded = {}


def reference(slug):
    """The reference module for `slug`, or None when there is no Python one."""
    if slug in _loaded:
        return _loaded[slug]
    path = os.path.join(HERE, "reference", "{}.py".format(slug))
    if not os.path.exists(path):
        _loaded[slug] = None
        return None
    spec = importlib.util.spec_from_file_location("veetcode_ref_" + slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _loaded[slug] = module
    return module


def solve(problem, raw_input):
    """(expected_output, expanded_args, seconds) for one test input."""
    module = reference(problem["slug"])
    if module is None:
        raise RuntimeError("no Python reference for " + problem["slug"])
    design = problem.get("design")
    param_types = problem.get("paramTypes") or []
    args_json = expand(copy.deepcopy(raw_input))

    if design:
        cls = harness.resolve_class(module, design["className"])
        started = time.perf_counter()
        produced = harness.to_json(harness.run_design(cls, args_json[0], args_json[1], design.get("constructorTypes")))
        return produced, args_json, time.perf_counter() - started

    fn = harness.resolve_callable(module, problem["functionName"])
    prepare = harness.PREPARES.get(problem.get("prepare"))
    if prepare is not None:
        args = prepare(copy.deepcopy(args_json))
        started = time.perf_counter()
        returned = fn(*args)
        elapsed = time.perf_counter() - started
        produced = harness.to_json(harness.marshal_out(returned, problem.get("returnType") or "json", args))
        return produced, args_json, elapsed

    args = [
        harness.marshal_in(copy.deepcopy(args_json[i]), param_types[i] if i < len(param_types) else "json")
        for i in range(len(args_json))
    ]

    started = time.perf_counter()
    returned = fn(*args)
    elapsed = time.perf_counter() - started

    check_arg = problem.get("checkArg")
    if check_arg is not None:
        kind = param_types[check_arg] if check_arg < len(param_types) else "json"
        produced = harness.to_json(harness.marshal_out(args[check_arg], kind, args))
    else:
        produced = harness.to_json(harness.marshal_out(returned, problem.get("returnType") or "json", args))
    return produced, args_json, elapsed
