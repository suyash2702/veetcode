"""VeetCode test harness (Python).

Usage: python3 harness.py <payload.json>

Reads a payload describing the user's solution file and the test cases,
runs every case in-process, and prints a single JSON line prefixed with
__VEETCODE_RESULT__ so that stray prints from user code cannot corrupt it.
"""

import builtins
import importlib.util
import io
import json
import math
import sys
import time
import os
import traceback
from contextlib import redirect_stdout, redirect_stderr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import expand  # noqa: E402  (compact stress-case specs -> real inputs)

RESULT_PREFIX = "__VEETCODE_RESULT__"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode({})".format(self.val)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode({})".format(self.val)


class Node:
    """The graph node LeetCode uses for clone-graph."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return "Node({})".format(self.val)


# Make the node classes visible to user code without any import ceremony.
builtins.TreeNode = TreeNode
builtins.ListNode = ListNode
builtins.Node = Node

# Recursive DFS over a 300x300 grid is a normal answer here, not a bug.
sys.setrecursionlimit(30000)


def build_tree(values):
    """Level-order array (LeetCode style, with nulls) -> TreeNode."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    head = 0
    while head < len(queue) and i < len(values):
        node = queue[head]
        head += 1
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def dump_tree(root):
    """TreeNode -> level-order array with trailing nulls trimmed."""
    if root is None:
        return []
    out = []
    queue = [root]
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def build_list(values):
    head = None
    for v in reversed(values or []):
        head = ListNode(v, head)
    return head


def dump_list(head, limit=10000):
    out = []
    while head is not None and len(out) < limit:
        out.append(head.val)
        head = head.next
    return out


# ---------------------------------------------------------------- prepares
#
# Some linked-list problems need a shape a plain array cannot express: a cycle,
# two lists sharing a tail, random pointers. A problem names one of these and
# the harness turns the raw test input into the arguments the solution sees.


def prepare_linked_cycle(raw):
    """[values, pos] -> one head whose tail links back to index pos (-1: none)."""
    values, pos = raw[0], raw[1]
    head = build_list(values)
    if pos is not None and pos >= 0 and head is not None:
        node = head
        for _ in range(pos):
            node = node.next
        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = node
    return [head]


def prepare_linked_intersection(raw):
    """[aPart, bPart, shared] -> two heads that share the same tail nodes."""
    a_part, b_part, shared = raw[0], raw[1], raw[2]
    tail = build_list(shared)

    def with_tail(values):
        head = build_list(values)
        if head is None:
            return tail
        node = head
        while node.next is not None:
            node = node.next
        node.next = tail
        return head

    return [with_tail(a_part), with_tail(b_part)]


def prepare_random_list(raw):
    """[[[val, randomIndex], ...]] -> one head whose nodes carry .random."""
    pairs = raw[0]
    nodes = [ListNode(value) for value, _ in pairs]
    for i, node in enumerate(nodes):
        node.next = nodes[i + 1] if i + 1 < len(nodes) else None
        target = pairs[i][1]
        node.random = None if target is None else nodes[target]
    return [nodes[0] if nodes else None]


def prepare_bottom_list(raw):
    """[[[column values], ...]] -> a list of heads linked by .next, each column by .bottom."""
    columns = raw[0]
    heads = []
    for values in columns:
        head = None
        for value in reversed(values):
            node = ListNode(value)
            node.bottom = head
            head = node
        heads.append(head)
    for i, head in enumerate(heads):
        if head is not None:
            head.next = heads[i + 1] if i + 1 < len(heads) else None
    return [heads[0] if heads else None]


def prepare_graph_nodes(raw):
    """[adjacency] -> the first node of an undirected graph whose nodes are
    numbered 1..n, matching LeetCode's clone-graph input."""
    adjacency = raw[0]
    nodes = [Node(i + 1) for i in range(len(adjacency))]
    for i, neighbours in enumerate(adjacency):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbours]
    return [nodes[0] if nodes else None]


def dump_graph(node):
    """A cloned graph read back as an adjacency list, numbered from 1."""
    if node is None:
        return []
    seen = {}
    order = []
    stack = [node]
    while stack:
        current = stack.pop()
        if id(current) in seen:
            continue
        seen[id(current)] = current
        order.append(current)
        for neighbour in current.neighbors:
            if id(neighbour) not in seen:
                stack.append(neighbour)
    by_value = {current.val: current for current in order}
    return [[n.val for n in by_value[v].neighbors] for v in sorted(by_value)]


PREPARES = {
    "graphNodes": prepare_graph_nodes,
    "linkedCycle": prepare_linked_cycle,
    "linkedIntersection": prepare_linked_intersection,
    "randomList": prepare_random_list,
    "bottomList": prepare_bottom_list,
}


def dump_random_list(head):
    nodes = []
    node = head
    while node is not None:
        nodes.append(node)
        node = node.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [[n.val, index.get(id(getattr(n, "random", None)))] for n in nodes]


def dump_bottom_list(head, limit=100000):
    out = []
    node = head
    while node is not None and len(out) < limit:
        out.append(node.val)
        node = getattr(node, "bottom", None)
    return out


def dump_dll(head, limit=100000):
    """A doubly linked list built out of tree nodes: walk `right` from the head."""
    out = []
    node = head
    while node is not None and len(out) < limit:
        out.append(node.val)
        node = node.right
    return out


def dump_next_levels(root):
    """Levels read through the `next` pointers a solution wired up."""
    out = []
    node = root
    while node is not None:
        level = []
        cursor = node
        while cursor is not None:
            level.append(cursor.val)
            cursor = getattr(cursor, "next", None)
        out.append(level)
        # Drop to the leftmost node of the level below.
        cursor = node
        node = None
        while cursor is not None and node is None:
            node = cursor.left or cursor.right
            cursor = getattr(cursor, "next", None)
    return out


def node_position(head, target, limit=1000000):
    """Index of `target` in the list starting at `head`, or -1. Works on cyclic
    lists because it stops after `limit` steps."""
    if target is None:
        return -1
    node = head
    for i in range(limit):
        if node is None:
            return -1
        if node is target:
            return i
        node = node.next
    return -1


def marshal_in(value, kind):
    if kind == "tree":
        return build_tree(value)
    if kind == "list":
        return build_list(value)
    if kind == "list[]":
        return [build_list(v) for v in value]
    return value


def marshal_out(value, kind, args=None):
    if kind == "graph":
        return dump_graph(value)
    if kind == "dllist":
        return dump_dll(value)
    if kind == "nextlevels":
        return dump_next_levels(value)
    if kind == "listpos":
        return node_position(args[0] if args else None, value)
    if kind == "randomlist":
        return dump_random_list(value)
    if kind == "bottomlist":
        return dump_bottom_list(value)
    if kind == "tree":
        return dump_tree(value)
    if kind == "list":
        return dump_list(value)
    if kind == "list[]":
        return [dump_list(v) for v in value]
    return value


def to_json(value):
    """Normalise arbitrary Python values into JSON-safe structures."""
    if isinstance(value, (str, bool)) or value is None:
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return str(value)
        return value
    if isinstance(value, (list, tuple)):
        return [to_json(v) for v in value]
    if isinstance(value, (set, frozenset)):
        return [to_json(v) for v in value]
    if isinstance(value, dict):
        return {str(k): to_json(v) for k, v in value.items()}
    if isinstance(value, TreeNode):
        return dump_tree(value)
    if isinstance(value, ListNode):
        return dump_list(value)
    return repr(value)


def sort_key(value):
    return json.dumps(value, sort_keys=True, default=str)


def equal(actual, expected, mode):
    if mode == "anyOf":
        return any(equal(actual, candidate, "exact") for candidate in expected)
    if mode == "approx":
        return approx_equal(actual, expected)
    if mode == "unordered":
        if not isinstance(actual, list) or not isinstance(expected, list):
            return actual == expected
        return sorted(map(sort_key, actual)) == sorted(map(sort_key, expected))
    if mode == "unordered2d":
        if not isinstance(actual, list) or not isinstance(expected, list):
            return actual == expected
        norm = lambda rows: sorted(
            sort_key(sorted(map(sort_key, row)) if isinstance(row, list) else row) for row in rows
        )
        return norm(actual) == norm(expected)
    return actual == expected


def approx_equal(a, b, tol=1e-5):
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(approx_equal(x, y, tol) for x, y in zip(a, b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) <= tol * max(1.0, abs(b))
    return a == b


def load_solution(path):
    spec = importlib.util.spec_from_file_location("veetcode_solution", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["veetcode_solution"] = module
    spec.loader.exec_module(module)
    return module


def resolve_callable(module, name):
    fn = getattr(module, name, None)
    if callable(fn):
        return fn
    # LeetCode-style `class Solution:` is also accepted.
    solution_cls = getattr(module, "Solution", None)
    if solution_cls is not None:
        method = getattr(solution_cls(), name, None)
        if callable(method):
            return method
    raise AttributeError(
        'no function named "{}" found in your solution (define it at module level or on a Solution class)'.format(name)
    )


def resolve_class(module, name):
    cls = getattr(module, name, None)
    if isinstance(cls, type):
        return cls
    raise AttributeError('no class named "{}" found in your solution'.format(name))


def run_design(cls, ops, op_args, ctor_types=None):
    """LeetCode-style design problems: ops[0] is the constructor, the rest are
    method calls, and the result list holds one entry per call (null for a
    method that returns nothing)."""
    out = []
    instance = None
    for index, op in enumerate(ops):
        args = op_args[index] if index < len(op_args) else []
        if index == 0:
            if ctor_types:
                args = [marshal_in(a, ctor_types[i] if i < len(ctor_types) else "json")
                        for i, a in enumerate(args)]
            instance = cls(*args)
            out.append(None)
            continue
        method = getattr(instance, op, None)
        if not callable(method):
            raise AttributeError('no method "{}" on {}'.format(op, cls.__name__))
        out.append(to_json(method(*args)))
    return out


def main():
    payload = json.load(open(sys.argv[1], "r", encoding="utf8"))
    param_types = payload.get("paramTypes") or []
    return_type = payload.get("returnType") or "json"
    check_arg = payload.get("checkArg")
    mode = payload.get("compare") or "exact"

    out = {"results": [], "compileError": None}

    design = payload.get("design")
    prepare = PREPARES.get(payload.get("prepare"))

    buffer = io.StringIO()
    try:
        with redirect_stdout(buffer), redirect_stderr(buffer):
            module = load_solution(payload["solutionPath"])
            fn = resolve_class(module, design["className"]) if design else resolve_callable(module, payload["functionName"])
    except BaseException:
        out["compileError"] = traceback.format_exc(limit=6).strip()
        emit(out)
        return

    for index, test in enumerate(payload["tests"]):
        try:
            raw_args = expand(test["input"])
        except Exception as err:  # a malformed generator spec is a data bug, not a user bug
            out["results"].append({"index": index, "passed": False, "runtimeMs": 0.0,
                                   "error": "bad test input: {}".format(err)})
            continue
        if prepare is not None:
            args = prepare(raw_args)
        elif design:
            args = raw_args
        else:
            args = [
                marshal_in(raw_args[i], param_types[i] if i < len(param_types) else "json")
                for i in range(len(raw_args))
            ]
        buffer = io.StringIO()
        record = {"index": index, "passed": False, "runtimeMs": 0.0, "stdout": ""}
        started = time.perf_counter()
        try:
            with redirect_stdout(buffer), redirect_stderr(buffer):
                returned = run_design(fn, args[0], args[1], design.get("constructorTypes")) if design else fn(*args)
            elapsed = (time.perf_counter() - started) * 1000.0
            if design:
                produced = to_json(returned)
            elif check_arg is not None:
                produced = to_json(marshal_out(args[check_arg], param_types[check_arg] if check_arg < len(param_types) else "json", args))
            else:
                produced = to_json(marshal_out(returned, return_type, args))
            record["actual"] = produced
            record["passed"] = equal(produced, test["output"], mode)
            record["runtimeMs"] = round(elapsed, 3)
        except BaseException:
            record["runtimeMs"] = round((time.perf_counter() - started) * 1000.0, 3)
            record["error"] = traceback.format_exc(limit=6).strip()
        record["stdout"] = buffer.getvalue()[:4000]
        out["results"].append(record)

    emit(out)


def emit(payload):
    sys.__stdout__.write(RESULT_PREFIX + json.dumps(payload, default=str) + "\n")
    sys.__stdout__.flush()


if __name__ == "__main__":
    main()
