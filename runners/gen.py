"""Deterministic expansion of generated test inputs.

Large stress cases are stored in problem JSON as a compact spec, e.g.

    {"__gen__": "ints", "n": 100000, "lo": -1000, "hi": 1000, "seed": 7}

and expanded here at run time. The same algorithm is implemented in
runners/gen.js, so Python and JavaScript see byte-identical inputs, and
tools/build_problems.py uses this module to compute expected outputs.

Never change the PRNG or a kind's semantics without rebuilding problems/ —
the stored expected outputs are tied to the exact sequence produced here.
"""

MASK = 0xFFFFFFFF
LOWER = "abcdefghijklmnopqrstuvwxyz"


class Rng:
    """mulberry32. Every step is a 32-bit operation, so the JavaScript port in
    runners/gen.js (using Math.imul) produces an identical stream."""

    def __init__(self, seed):
        self.state = seed & MASK

    def next(self):
        self.state = (self.state + 0x6D2B79F5) & MASK
        t = self.state
        t = ((t ^ (t >> 15)) * (t | 1)) & MASK
        t = (t ^ ((t + (((t ^ (t >> 7)) * (t | 61)) & MASK)) & MASK)) & MASK
        return (t ^ (t >> 14)) & MASK

    def below(self, n):
        return self.next() % n if n > 0 else 0

    def between(self, lo, hi):
        return lo + self.below(hi - lo + 1)

    def pick(self, seq):
        return seq[self.below(len(seq))]


def _shuffle(rng, items):
    for i in range(len(items) - 1, 0, -1):
        j = rng.below(i + 1)
        items[i], items[j] = items[j], items[i]
    return items


def _ints(spec, rng):
    lo = spec.get("lo", 0)
    hi = spec.get("hi", 100)
    return [rng.between(lo, hi) for _ in range(spec["n"])]


def _sorted_ints(spec, rng):
    values = _ints(spec, rng)
    if spec.get("unique"):
        values = sorted(set(values))
        # Refill so the requested length survives de-duplication.
        step = max(1, spec.get("step", 1))
        while len(values) < spec["n"]:
            values.append((values[-1] if values else spec.get("lo", 0)) + rng.between(1, step))
    values.sort(reverse=bool(spec.get("desc")))
    return values


def _perm(spec, rng):
    base = spec.get("base", 0)
    return _shuffle(rng, [base + i for i in range(spec["n"])])


def _string(spec, rng):
    alphabet = spec.get("alphabet", LOWER)
    return "".join(rng.pick(alphabet) for _ in range(spec["n"]))


def _grid(spec, rng):
    rows, cols = spec["rows"], spec["cols"]
    alphabet = spec.get("alphabet")
    out = []
    for _ in range(rows):
        if alphabet is not None:
            row = "".join(rng.pick(alphabet) for _ in range(cols))
            out.append(row if spec.get("asString", True) else list(row))
        else:
            out.append([rng.between(spec.get("lo", 0), spec.get("hi", 1)) for _ in range(cols)])
    return out


def _pairs(spec, rng):
    lo = spec.get("lo", 0)
    hi = spec.get("hi", 100)
    return [[rng.between(lo, hi), rng.between(lo, hi)] for _ in range(spec["n"])]


def _repeat(spec, _rng):
    return [spec.get("value", 0)] * spec["n"]


def _arange(spec, _rng):
    start = spec.get("start", 0)
    step = spec.get("step", 1)
    return [start + i * step for i in range(spec["n"])]


def _words(spec, rng):
    alphabet = spec.get("alphabet", LOWER)
    lo = spec.get("minLen", 1)
    hi = spec.get("maxLen", 8)
    return ["".join(rng.pick(alphabet) for _ in range(rng.between(lo, hi))) for _ in range(spec["n"])]


def _edges(spec, rng):
    """n directed edges over `nodes` vertices; acyclic when spec['dag']."""
    nodes = spec["nodes"]
    out = []
    for _ in range(spec["n"]):
        a = rng.below(nodes)
        b = rng.below(nodes)
        if spec.get("dag") and a == b:
            continue
        if spec.get("dag") and a < b:
            a, b = b, a
        out.append([a, b])
    return out


def _concat(spec, _rng):
    parts = [expand(part) for part in spec["parts"]]
    if parts and all(isinstance(part, str) for part in parts):
        return "".join(parts)
    out = []
    for part in parts:
        out.extend(part if isinstance(part, list) else [part])
    return out


def _strrepeat(spec, _rng):
    return spec.get("value", "a") * spec["n"]


def _shuffle_spec(spec, rng):
    value = expand(spec["of"])
    if isinstance(value, str):
        return "".join(_shuffle(rng, list(value)))
    return _shuffle(rng, list(value))


def _rotate(spec, _rng):
    value = expand(spec["of"])
    by = spec.get("by", 0) % (len(value) or 1)
    return value[by:] + value[:by]


def _intervals(spec, rng):
    """n intervals [start, start + length], possibly overlapping."""
    lo = spec.get("lo", 0)
    hi = spec.get("hi", 1000)
    max_len = spec.get("maxLen", 10)
    out = []
    for _ in range(spec["n"]):
        start = rng.between(lo, hi)
        out.append([start, start + rng.below(max_len + 1)])
    return out


def _disjoint(spec, rng):
    """n sorted, non-overlapping intervals — the shape "insert interval" expects."""
    out = []
    cursor = spec.get("start", 0)
    for _ in range(spec["n"]):
        cursor += rng.between(1, spec.get("gap", 5))
        end = cursor + rng.below(spec.get("maxLen", 5) + 1)
        out.append([cursor, end])
        cursor = end
    return out


def _sorted_grid(spec, rng):
    """A matrix whose rows ascend and whose rows ascend against each other."""
    value = spec.get("start", 0)
    out = []
    for _ in range(spec["rows"]):
        row = []
        for _ in range(spec["cols"]):
            value += rng.between(1, spec.get("step", 5))
            row.append(value)
        out.append(row)
    return out


def _zipsum(spec, _rng):
    """Element-wise sum of two generated lists — start times plus durations, say."""
    parts = [expand(part) for part in spec["parts"]]
    return [sum(values) for values in zip(*parts)]


def _duplicate(spec, _rng):
    times = spec.get("times", 2)
    return [value for value in expand(spec["of"]) for _ in range(times)]


def _sort_of(spec, _rng):
    return sorted(expand(spec["of"]), reverse=bool(spec.get("desc")))


def _without(spec, _rng):
    return [value for value in expand(spec["of"]) if value != spec["value"]]


def _weighted_edges(spec, rng):
    """n weighted edges over `nodes` vertices; a spanning path first when connected."""
    lo = spec.get("lo", 0)
    hi = spec.get("hi", 10000)
    nodes = spec["nodes"]
    out = []
    if spec.get("connected"):
        for i in range(nodes - 1):
            out.append([i, i + 1, rng.between(lo, hi)])
    for _ in range(spec.get("n", 0)):
        out.append([rng.below(nodes), rng.below(nodes), rng.between(lo, hi)])
    return out


def _knows(spec, rng):
    """The "who knows whom" matrix of the celebrity problem."""
    n = spec["n"]
    density = spec.get("density", 50)
    celebrity = spec.get("celebrity")
    matrix = [[1 if i == j else (1 if rng.below(100) < density else 0) for j in range(n)]
              for i in range(n)]
    if celebrity is not None:
        for i in range(n):
            matrix[celebrity][i] = 1 if i == celebrity else 0
            matrix[i][celebrity] = 1
    return matrix


def _adjacency(spec, rng):
    """Adjacency list for `nodes` vertices and `n` random edges."""
    nodes = spec["nodes"]
    out = [[] for _ in range(nodes)]
    for _ in range(spec.get("n", 0)):
        a = rng.below(nodes)
        b = rng.below(nodes)
        out[a].append(b)
        if not spec.get("directed"):
            out[b].append(a)
    return out


def _oplog_arg(spec, rng):
    if "int" in spec:
        lo, hi = spec["int"]
        return rng.between(lo, hi)
    if "choice" in spec:
        return rng.pick(spec["choice"])
    if "word" in spec:
        word = spec["word"]
        alphabet = word.get("alphabet", LOWER)
        length = rng.between(word.get("minLen", 1), word.get("maxLen", 6))
        return "".join(rng.pick(alphabet) for _ in range(length))
    raise ValueError("unknown oplog argument: {}".format(spec))


def _oplog(spec, rng):
    """An operation log for a design problem.

    Emits `[className, op, op, ...]` or the matching argument lists, chosen by
    `part`, so a single 5000-call log costs a few hundred bytes of JSON.

    A method may declare `delta` (how it changes the container's size) and
    `needs` (the minimum size it may be called at); when the log would call a
    method on too small a container, the first growing method is used instead.
    """
    methods = spec["methods"]
    pool = []
    for index, method in enumerate(methods):
        pool.extend([index] * method.get("weight", 1))
    grower = next((i for i, m in enumerate(methods) if m.get("delta", 0) > 0), 0)

    ops = [spec["cls"]]
    args = [spec.get("ctor", [])]
    size = 0
    for _ in range(spec["n"]):
        index = pool[rng.below(len(pool))]
        if size < methods[index].get("needs", 0):
            index = grower
        method = methods[index]
        ops.append(method["name"])
        args.append([_oplog_arg(arg, rng) for arg in method.get("args", [])])
        size = max(0, size + method.get("delta", 0))
    return ops if spec.get("part", "ops") == "ops" else args


KINDS = {
    "oplog": _oplog,
    "adj": _adjacency,
    "zipsum": _zipsum,
    "duplicate": _duplicate,
    "sortof": _sort_of,
    "without": _without,
    "wedges": _weighted_edges,
    "knows": _knows,
    "intervals": _intervals,
    "disjoint": _disjoint,
    "sortedgrid": _sorted_grid,
    "concat": _concat,
    "strrepeat": _strrepeat,
    "shuffle": _shuffle_spec,
    "rotate": _rotate,
    "ints": _ints,
    "sorted": _sorted_ints,
    "perm": _perm,
    "string": _string,
    "grid": _grid,
    "pairs": _pairs,
    "repeat": _repeat,
    "arange": _arange,
    "words": _words,
    "edges": _edges,
}


def expand(value):
    """Recursively replaces every {"__gen__": ...} node with its materialised value."""
    if isinstance(value, dict):
        kind = value.get("__gen__")
        if kind is None:
            return {k: expand(v) for k, v in value.items()}
        if kind not in KINDS:
            raise ValueError("unknown generator kind: {}".format(kind))
        return KINDS[kind](value, Rng(value.get("seed", 1)))
    if isinstance(value, list):
        return [expand(v) for v in value]
    return value
