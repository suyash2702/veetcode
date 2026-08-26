"""Extra test cases for every problem.

Each entry produces *inputs only* — expected outputs are computed at build
time by running tools/reference/<slug>.py, so the answers can never drift
from the reference implementation.

Large inputs are stored as compact generator specs (see runners/gen.py) and
expanded identically by the Python and JavaScript harnesses, which keeps
100k-element stress cases from bloating problems/*.json.

Register with @cases(slug); optional hooks:
  validate(args, expected) -> bool   drop cases whose answer is ambiguous
  expected(args) -> value            override the oracle (e.g. anyOf lists)
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "runners"))

from gen import Rng, expand  # noqa: E402

REGISTRY = {}


def cases(slug, validate=None, expected=None):
    def register(fn):
        REGISTRY[slug] = {"make": fn, "validate": validate, "expected": expected}
        return fn
    return register


def G(kind, **kw):
    return dict(__gen__=kind, **kw)


def ints(n, lo, hi, seed):
    return G("ints", n=n, lo=lo, hi=hi, seed=seed)


def text(n, seed, alphabet="abcdefghijklmnopqrstuvwxyz"):
    return G("string", n=n, alphabet=alphabet, seed=seed)


LOWER = "abcdefghijklmnopqrstuvwxyz"


# ------------------------------------------------------------------ helpers


def level_order(n, seed, sorted_bst=False, null_rate=0, values=(-100, 100)):
    """A level-order array (LeetCode encoding) for a random tree of n nodes."""
    rng = Rng(seed)
    if sorted_bst:
        # Insert distinct values into a BST, then serialise it.
        chosen = []
        seen = set()
        while len(chosen) < n:
            v = rng.between(values[0], values[1])
            if v not in seen:
                seen.add(v)
                chosen.append(v)
        root = None
        nodes = {}

        def insert(v):
            nonlocal root
            if root is None:
                root = v
                nodes[v] = [None, None]
                return
            cur = root
            while True:
                side = 0 if v < cur else 1
                nxt = nodes[cur][side]
                if nxt is None:
                    nodes[cur][side] = v
                    nodes[v] = [None, None]
                    return
                cur = nxt

        for v in chosen:
            insert(v)
        out = []
        queue = [root]
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            if node is None:
                out.append(None)
                continue
            out.append(node)
            queue.append(nodes[node][0])
            queue.append(nodes[node][1])
        while out and out[-1] is None:
            out.pop()
        return out

    out = []
    placed = 0
    slots = 1
    while placed < n and slots > 0:
        next_slots = 0
        for _ in range(slots):
            if placed >= n:
                out.append(None)
                continue
            if null_rate and rng.below(100) < null_rate and out:
                out.append(None)
                continue
            out.append(rng.between(values[0], values[1]))
            placed += 1
            next_slots += 2
        slots = next_slots
    while out and out[-1] is None:
        out.pop()
    return out


def chain(n, right=True):
    """Level-order encoding of a single-branch tree (a path of n nodes)."""
    if n <= 0:
        return []
    out = [1]
    for value in range(2, n + 1):
        out.extend([None, value] if right else [value, None])
    while out and out[-1] is None:
        out.pop()
    return out


# ------------------------------------------------------------------- easy


def _two_sum_unique(args, _expected):
    """LeetCode guarantees exactly one valid pair; drop generated arrays that
    happen to contain a second one."""
    nums, target = args
    seen = {}
    hits = 0
    for value in nums:
        hits += seen.get(target - value, 0)
        seen[value] = seen.get(value, 0) + 1
    return hits == 1


@cases("two-sum", validate=_two_sum_unique)
def _two_sum():
    out = []
    for i, n in enumerate([2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 50, 80]):
        spec = ints(n, -10 ** 7, 10 ** 7, 400 + i)
        values = expand(spec)
        out.append([spec, values[0] + values[-1]])
    # Two far-out values are the only pair that can reach their own sum, so the
    # answer stays unique no matter how large the array gets.
    for i, n in enumerate([100, 500, 2000, 10000, 50000, 100000]):
        for sign in (1, -1):
            big = sign * 10 ** 8
            base = ints(n - 2, -10 ** 6, 10 ** 6, 900 + i * 3 + (0 if sign > 0 else 1))
            arr = G("shuffle", of=G("concat", parts=[base, [big + sign, big + sign * 7]]),
                    seed=31 * i + 7 + (0 if sign > 0 else 5))
            out.append([arr, 2 * big + sign * 8])
    return out


@cases("valid-parentheses")
def _valid_parentheses():
    out = [[text(n, 500 + i, "()[]{}")] for i, n in enumerate([1, 2, 3, 5, 8, 12, 20, 50, 200, 1000, 20000, 200000])]
    out += [
        [G("strrepeat", value="()", n=50000)],
        [G("strrepeat", value="([{}])", n=30000)],
        [G("strrepeat", value="{[]}", n=25000)],
        [G("concat", parts=[G("strrepeat", value="(", n=50000), G("strrepeat", value=")", n=50000)])],
        [G("concat", parts=[G("strrepeat", value="[", n=50000), G("strrepeat", value="]", n=49999)])],
        [G("concat", parts=[G("strrepeat", value="{", n=100000), G("strrepeat", value="}", n=100000)])],
        [G("concat", parts=[G("strrepeat", value="(", n=99999), ")"])],
        [G("concat", parts=[G("strrepeat", value="()", n=99999), "("])],
        [G("concat", parts=[")", G("strrepeat", value="()", n=99999)])],
        [G("strrepeat", value="(]", n=1000)],
        [G("strrepeat", value="([)]", n=1000)],
        [G("strrepeat", value="((", n=50000)],
        [G("strrepeat", value="))", n=50000)],
        ["("], [")"], ["[]"], ["{"], ["([{}])"], ["(()"], ["())"], ["{[}]"],
    ]
    return out


@cases("best-time-to-buy-and-sell-stock")
def _best_time():
    out = [[ints(n, 0, 10 ** 4, 600 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 25, 100, 1000, 20000, 200000])]
    out += [
        [G("arange", n=100000, start=0, step=1)],                 # strictly rising
        [G("arange", n=100000, start=100000, step=-1)],           # strictly falling
        [G("repeat", value=7, n=100000)],                         # flat
        [G("concat", parts=[G("arange", n=50000, start=50000, step=-1), G("arange", n=50000, start=0, step=2)])],
        [G("concat", parts=[[10000], G("repeat", value=0, n=99999)])],
        [G("concat", parts=[G("repeat", value=0, n=99999), [10000]])],
        [ints(50000, 0, 3, 611)],                                 # heavy ties
        [ints(50000, 5000, 5010, 612)],                           # narrow band
        [[2, 1]], [[1, 2]], [[3, 3]], [[0]], [[10000, 0, 10000]],
        [[7, 6, 4, 3, 1]], [[1, 2, 3, 4, 5]], [[2, 4, 1]],
    ]
    return out


@cases("contains-duplicate")
def _contains_duplicate():
    out = [[ints(n, -50, 50, 700 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 30, 100, 1000])]
    out += [
        [G("perm", n=50)], [G("perm", n=1000)], [G("perm", n=100000)], [G("perm", n=200000)],
        [G("shuffle", of=G("concat", parts=[G("perm", n=99999), [0]]), seed=41)],
        [G("shuffle", of=G("concat", parts=[G("perm", n=199999), [199998]]), seed=42)],
        [ints(100000, 0, 10 ** 9, 720)],
        [ints(100000, 0, 100, 721)],
        [G("repeat", value=5, n=100000)],
        [G("arange", n=100000, start=-50000)],
        [[1]], [[1, 1]], [[1, 2]], [[0, 0, 0]], [[-1, 1]],
        [G("concat", parts=[G("arange", n=99999), [99998]])],
    ]
    return out


@cases("valid-anagram")
def _valid_anagram():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 12, 40, 200, 2000, 50000]):
        base = text(n, 800 + i)
        out.append([base, G("shuffle", of=base, seed=900 + i)])              # true
        out.append([base, text(n, 850 + i)])                                 # almost surely false
    out += [
        [G("strrepeat", value="a", n=50000), G("strrepeat", value="a", n=50000)],
        [G("concat", parts=[G("strrepeat", value="a", n=49999), "b"]),
         G("concat", parts=[G("strrepeat", value="a", n=49999), "c"])],
        [G("concat", parts=[G("strrepeat", value="ab", n=25000)]),
         G("concat", parts=[G("strrepeat", value="ba", n=25000)])],
        [text(1000, 861, "ab"), G("shuffle", of=text(1000, 861, "ab"), seed=99)],
        [text(1000, 862, "ab"), text(1001, 862, "ab")],
        ["a", "a"], ["a", "b"], ["ab", "ba"], ["ab", "ab"], ["a", "aa"],
        ["aacc", "ccac"], ["rat", "tar"], ["anagram", "nagaram"],
    ]
    return out


@cases("binary-search")
def _binary_search():
    out = []
    for i, n in enumerate([1, 2, 3, 4, 7, 15, 100, 1000, 20000, 100000]):
        spec = G("sorted", n=n, lo=-10 ** 6, hi=10 ** 6, seed=1000 + i, unique=True, step=5)
        values = expand(spec)
        out.append([spec, values[0]])                    # first
        out.append([spec, values[-1]])                   # last
        out.append([spec, values[len(values) // 2]])     # middle
        out.append([spec, values[0] - 1])                # below range
        out.append([spec, values[-1] + 1])               # above range
    out += [[[5], 5], [[5], -5], [[-1, 0, 3, 5, 9, 12], 9], [[-1, 0, 3, 5, 9, 12], 2]]
    return out


@cases("maximum-subarray")
def _maximum_subarray():
    out = [[ints(n, -100, 100, 1100 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 50, 500, 5000, 200000])]
    out += [
        [ints(100000, -10 ** 4, -1, 1120)],              # all negative
        [ints(100000, 1, 10 ** 4, 1121)],                # all positive
        [ints(100000, -10 ** 4, 10 ** 4, 1122)],
        [G("repeat", value=-1, n=100000)],
        [G("repeat", value=0, n=100000)],
        [G("concat", parts=[G("repeat", value=-10000, n=50000), G("repeat", value=1, n=50000)])],
        [G("concat", parts=[G("repeat", value=1, n=50000), G("repeat", value=-10000, n=50000)])],
        [[-1]], [[0]], [[-2, 1]], [[1, -2, 3]], [[5, 4, -1, 7, 8]], [[-2, -1]],
    ]
    return out


@cases("climbing-stairs")
def _climbing_stairs():
    return [[n] for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 23,
                          25, 28, 30, 32, 34, 36, 38, 40, 41, 42, 43, 44, 45]]


@cases("move-zeroes")
def _move_zeroes():
    out = [[ints(n, 0, 3, 1200 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 40, 500, 5000, 50000])]
    out += [[ints(n, 0, hi, 1230 + i)] for i, (n, hi) in enumerate(
        [(1200, 1), (1500, 2), (1800, 5), (2000, 1), (2400, 9), (2400, 1), (900, 0)])]
    out += [
        [G("repeat", value=0, n=10000)],
        [G("perm", n=10000, base=1)],
        [G("concat", parts=[G("repeat", value=0, n=5000), G("perm", n=5000, base=1)])],
        [G("concat", parts=[G("perm", n=5000, base=1), G("repeat", value=0, n=5000)])],
        [ints(10000, -3, 3, 1220)],
        [ints(10000, 0, 1, 1221)],
        [[0]], [[1]], [[0, 1]], [[1, 0]], [[0, 0, 1]], [[1, 0, 0]], [[0, 1, 0, 3, 12]],
    ]
    return out


@cases("merge-sorted-array")
def _merge_sorted_array():
    out = []
    for i, (m, n) in enumerate([(0, 1), (1, 0), (1, 1), (3, 3), (5, 2), (2, 5), (50, 50),
                                (500, 500), (2000, 3000), (10000, 10000)]):
        first = G("sorted", n=m, lo=-10 ** 6, hi=10 ** 6, seed=1300 + i) if m else []
        second = G("sorted", n=n, lo=-10 ** 6, hi=10 ** 6, seed=1400 + i) if n else []
        nums1 = G("concat", parts=[first, G("repeat", value=0, n=n)]) if n else first
        out.append([nums1, m, second, n])
    for i, (m, n) in enumerate([(1, 2), (2, 1), (4, 1), (1, 4), (7, 9), (13, 3), (30, 30),
                                (64, 64), (120, 80), (200, 200), (400, 100), (100, 400),
                                (1000, 200), (200, 1000), (1200, 1200)]):
        first = G("sorted", n=m, lo=-500, hi=500, seed=1310 + i)
        second = G("sorted", n=n, lo=-500, hi=500, seed=1410 + i)
        out.append([G("concat", parts=[first, G("repeat", value=0, n=n)]), m, second, n])
    out += [
        [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[1], 1, [], 0],
        [[0], 0, [1], 1],
        [[4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3],
        [[1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3],
        [[2, 2, 2, 0, 0, 0], 3, [2, 2, 2], 3],
        [G("concat", parts=[G("repeat", value=0, n=5000), G("repeat", value=0, n=5000)]), 5000,
         G("repeat", value=0, n=5000), 5000],
        [G("concat", parts=[G("arange", n=5000, start=0, step=2), G("repeat", value=0, n=5000)]), 5000,
         G("arange", n=5000, start=1, step=2), 5000],
    ]
    return out


@cases("reverse-linked-list")
def _reverse_linked_list():
    out = [[ints(n, -1000, 1000, 1500 + i)] for i, n in enumerate([0, 1, 2, 3, 5, 10, 100, 1000, 5000])]
    out += [[ints(n, -10 ** 4, 10 ** 4, 1530 + i)] for i, n in enumerate(
        [4, 6, 8, 15, 30, 60, 250, 700, 1500, 2400])]
    out += [
        [G("arange", n=5000)],
        [G("repeat", value=1, n=5000)],
        [G("perm", n=3000)],
        [[]], [[1]], [[1, 2]], [[1, 2, 3, 4, 5]], [[0, 0]], [[-1]],
    ]
    return out


@cases("merge-two-sorted-lists")
def _merge_two_sorted_lists():
    out = []
    for i, (a, b) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1), (2, 3), (10, 10), (100, 5),
                                (500, 500), (2000, 2000), (4000, 4000)]):
        first = G("sorted", n=a, lo=-100, hi=100, seed=1600 + i) if a else []
        second = G("sorted", n=b, lo=-100, hi=100, seed=1700 + i) if b else []
        out.append([first, second])
    for i, (a, b) in enumerate([(1, 2), (2, 2), (3, 1), (5, 5), (20, 20), (50, 7), (7, 50),
                                (200, 200), (600, 400), (1200, 1200)]):
        out.append([G("sorted", n=a, lo=-10 ** 4, hi=10 ** 4, seed=1610 + i),
                    G("sorted", n=b, lo=-10 ** 4, hi=10 ** 4, seed=1710 + i)])
    out += [
        [G("arange", n=4000, start=0, step=2), G("arange", n=4000, start=1, step=2)],
        [G("arange", n=4000), G("arange", n=4000, start=4000)],
        [G("repeat", value=0, n=4000), G("repeat", value=0, n=4000)],
        [[], []], [[1], []], [[], [1]], [[1, 2, 4], [1, 3, 4]], [[5], [1, 2, 4]],
    ]
    return out


@cases("invert-binary-tree")
def _invert_binary_tree():
    out = [[level_order(n, 1800 + i)] for i, n in enumerate([0, 1, 2, 3, 5, 8, 15, 31, 100, 500, 1500])]
    out += [[level_order(n, 1900 + i, null_rate=35)] for i, n in enumerate([10, 40, 200, 800])]
    out += [[level_order(n, 1950 + i, values=(-9, 9))] for i, n in enumerate([4, 6, 12, 60, 300, 900])]
    out += [
        [chain(200)], [chain(200, right=False)], [chain(1)], [chain(2)],
        [[]], [[1]], [[1, 2]], [[1, None, 2]], [[4, 2, 7, 1, 3, 6, 9]], [[2, 1, 3]],
    ]
    return out


@cases("maximum-depth-of-binary-tree")
def _maximum_depth():
    out = [[level_order(n, 2000 + i)] for i, n in enumerate([0, 1, 2, 3, 7, 15, 63, 255, 1023, 2047])]
    out += [[level_order(n, 2100 + i, null_rate=40)] for i, n in enumerate([10, 50, 300, 1000])]
    out += [[level_order(n, 2150 + i, null_rate=60)] for i, n in enumerate([5, 25, 120, 600, 2000])]
    out += [
        [chain(500)], [chain(500, right=False)], [chain(1000)], [chain(1)],
        [[]], [[1]], [[1, None, 2]], [[3, 9, 20, None, None, 15, 7]], [[1, 2, 3, 4, None, None, 5]],
    ]
    return out


@cases("majority-element")
def _majority_element():
    out = []
    for i, n in enumerate([1, 3, 5, 9, 25, 101, 1001, 10001, 99999]):
        major = n // 2 + 1
        rest = ints(n - major, -10 ** 6, 10 ** 6, 2200 + i) if n - major else []
        out.append([G("shuffle", of=G("concat", parts=[G("repeat", value=7 + i, n=major), rest]), seed=2300 + i)])
    for i, n in enumerate([15, 999, 50001]):
        major = n // 2 + 1
        out.append([G("concat", parts=[G("repeat", value=-3, n=major), ints(n - major, 0, 5, 2400 + i)])])
        out.append([G("concat", parts=[ints(n - major, 0, 5, 2500 + i), G("repeat", value=-3, n=major)])])
    out += [
        [G("repeat", value=2, n=100000)],
        [G("shuffle", of=G("concat", parts=[G("repeat", value=1, n=50001), G("arange", n=49999, start=100)]), seed=77)],
        [[1]], [[2, 2, 1]], [[3, 2, 3]], [[2, 2, 1, 1, 1, 2, 2]], [[1, 1, 2]],
    ]
    return out


# ----------------------------------------------------------------- medium


@cases("group-anagrams")
def _group_anagrams():
    out = [[G("words", n=n, minLen=1, maxLen=4, alphabet="abc", seed=3000 + i)]
           for i, n in enumerate([1, 2, 3, 5, 10, 40, 200, 1000, 2000])]
    out += [[G("words", n=n, minLen=3, maxLen=6, alphabet="abcde", seed=3100 + i)]
            for i, n in enumerate([20, 100, 800])]
    out += [
        [G("words", n=500, minLen=1, maxLen=2, alphabet="ab", seed=3200)],
        [G("repeat", value="abc", n=500)],
        [G("words", n=300, minLen=8, maxLen=8, alphabet="abcdefghijklmnopqrstuvwxyz", seed=3201)],
        [G("concat", parts=[G("repeat", value="ab", n=250), G("repeat", value="ba", n=250)])],
        [[""]], [["a"]], [["a", "a"]], [["a", "b"]], [["ab", "ba", "abc"]],
        [["eat", "tea", "tan", "ate", "nat", "bat"]], [["", ""]], [["abc", "cba", "bac", "xyz"]],
    ]
    return out


@cases("longest-substring-without-repeating-characters")
def _longest_substring():
    out = [[text(n, 3300 + i)] for i, n in enumerate([0, 1, 2, 3, 5, 10, 50, 500, 5000, 50000])]
    out += [
        [text(50000, 3320, "ab")],
        [text(50000, 3321, "abcde")],
        [text(50000, 3322, "abcdefghijklmnopqrstuvwxyz")],
        [G("strrepeat", value="a", n=50000)],
        [G("strrepeat", value="ab", n=25000)],
        [G("strrepeat", value="abcdefghijklmnopqrstuvwxyz", n=1923)],
        [G("concat", parts=[G("strrepeat", value="a", n=25000), "abcdefghijklmnopqrstuvwxyz"])],
        [G("concat", parts=["abcdefghijklmnopqrstuvwxyz", G("strrepeat", value="a", n=25000)])],
        [""], ["a"], ["aa"], ["ab"], ["abcabcbb"], ["bbbbb"], ["pwwkew"], ["dvdf"], ["tmmzuxt"],
    ]
    return out


@cases("product-of-array-except-self")
def _product_except_self():
    # Values stay in {-1, 0, 1} for the long arrays so every prefix product
    # keeps fitting in 32 bits, exactly as the problem promises.
    out = [[ints(n, -1, 1, 3400 + i)] for i, n in enumerate([2, 3, 5, 10, 50, 500, 2000])]
    out += [[ints(n, -9, 9, 3410 + i)] for i, n in enumerate([2, 3, 4, 5, 6, 7, 8])]
    out += [
        [G("repeat", value=1, n=2000)],
        [G("repeat", value=-1, n=2000)],
        [G("concat", parts=[[0], G("repeat", value=1, n=1999)])],
        [G("concat", parts=[G("repeat", value=1, n=1998), [0, 0]])],
        [ints(2000, 0, 1, 3420)],
        [ints(2000, -1, 0, 3421)],
        [[1, 2]], [[0, 0]], [[-1, 1]], [[1, 2, 3, 4]], [[-1, 1, 0, -3, 3]], [[0, 1]], [[1, 0]],
    ]
    return out


def _top_k_unambiguous(args, _expected):
    """Only keep inputs where the k-th and (k+1)-th frequencies differ, so the
    set of answers is unique."""
    nums, k = args
    counts = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    ordered = sorted(counts.values(), reverse=True)
    if k > len(ordered):
        return False
    return k == len(ordered) or ordered[k - 1] != ordered[k]


@cases("top-k-frequent-elements", validate=_top_k_unambiguous)
def _top_k_frequent():
    out = []
    for i, (n, hi, k) in enumerate([(5, 3, 1), (10, 4, 2), (20, 5, 3), (50, 7, 4), (200, 10, 5),
                                    (1000, 20, 6), (5000, 30, 10), (20000, 50, 12),
                                    (100000, 100, 20), (100000, 1000, 50)]):
        out.append([ints(n, 0, hi, 3500 + i), k])
    # Geometric frequencies make the boundary unambiguous by construction.
    for i, levels in enumerate([3, 5, 8, 12]):
        parts = [G("repeat", value=v, n=2 ** (levels - v)) for v in range(levels)]
        arr = G("shuffle", of=G("concat", parts=parts), seed=3600 + i)
        for k in (1, 2, levels // 2, levels):
            out.append([arr, k])
    out += [
        [[1], 1], [[1, 2], 2], [[1, 1, 2], 1], [[1, 1, 1, 2, 2, 3], 2],
        [[4, 4, 4, 1, 1, 2], 2], [[5, 5, 4], 1],
    ]
    return out


@cases("coin-change")
def _coin_change():
    out = []
    for i, (coins, amount) in enumerate([([1], 0), ([2], 3), ([1, 2, 5], 11), ([1, 3, 4], 6),
                                         ([186, 419, 83, 408], 6249), ([2, 5, 10, 1], 27),
                                         ([1, 5, 10, 25], 9999), ([7, 11], 100),
                                         ([3, 7, 405, 436], 8839), ([2], 10001),
                                         ([1, 2, 5, 10, 20, 50, 100, 200, 500], 10000),
                                         ([9, 6, 5, 1], 10000), ([389, 46, 222, 352, 4, 250], 5343),
                                         ([2, 4, 6, 8], 9999), ([2, 4, 6, 8], 10000)]):
        out.append([coins, amount])
    for i, amount in enumerate([1, 2, 7, 63, 511, 2047, 4095, 8191, 10000]):
        out.append([G("sorted", n=10, lo=1, hi=200, seed=3700 + i, unique=True), amount])
    for i, amount in enumerate([9997, 9998, 9999, 10000]):
        out.append([G("sorted", n=12, lo=2, hi=500, seed=3800 + i, unique=True), amount])
    out += [[[1], 10000], [[10000], 10000], [[9999], 10000], [[1, 10000], 10000]]
    return out


@cases("number-of-islands")
def _number_of_islands():
    out = []
    for i, (rows, cols, density) in enumerate([(1, 1, "1"), (1, 1, "0"), (1, 5, "01"), (5, 1, "01"),
                                               (3, 3, "01"), (8, 8, "01"), (20, 20, "01"),
                                               (60, 60, "01"), (150, 150, "01"), (300, 300, "01")]):
        out.append([G("grid", rows=rows, cols=cols, alphabet=density, asString=False, seed=3900 + i)])
    for i, (rows, cols, alphabet) in enumerate([(200, 200, "0001"), (60, 60, "0111"),
                                                (200, 200, "01"), (80, 80, "011")]):
        out.append([G("grid", rows=rows, cols=cols, alphabet=alphabet, asString=False, seed=4000 + i)])
    out += [
        [G("grid", rows=60, cols=60, alphabet="1", asString=False, seed=4010)],     # one solid island
        [G("grid", rows=300, cols=300, alphabet="0", asString=False, seed=4011)],   # water only
        [G("grid", rows=100, cols=100, alphabet="10", asString=False, seed=4012)],
        [[["1"]]], [[["0"]]], [[["1", "0", "1"]]], [[["1"], ["0"], ["1"]]],
        [[["1", "1"], ["1", "1"]]], [[["1", "0"], ["0", "1"]]],
    ]
    return out


@cases("course-schedule")
def _course_schedule():
    out = []
    for i, (nodes, edge_count) in enumerate([(1, 0), (2, 1), (2, 2), (5, 4), (10, 15), (50, 80),
                                             (200, 400), (1000, 2000), (2000, 5000)]):
        out.append([nodes, G("edges", n=edge_count, nodes=nodes, seed=4100 + i)])            # may cycle
        out.append([nodes, G("edges", n=edge_count, nodes=nodes, seed=4200 + i, dag=True)])  # acyclic
    out += [
        [2000, G("edges", n=5000, nodes=2000, seed=4300, dag=True)],
        [2000, G("edges", n=5000, nodes=2000, seed=4301)],
        [5000, G("edges", n=5000, nodes=5000, seed=4302, dag=True)],
        [1, []], [2, []], [2, [[1, 0]]], [2, [[1, 0], [0, 1]]],
        [3, [[1, 0], [2, 1]]], [3, [[1, 0], [2, 1], [0, 2]]],
        [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
    ]
    return out


@cases("3sum")
def _three_sum():
    out = [[ints(n, -10, 10, 4400 + i)] for i, n in enumerate([0, 1, 2, 3, 4, 6, 10, 25, 60])]
    out += [[ints(n, -10 ** 5, 10 ** 5, 4500 + i)] for i, n in enumerate([50, 200, 800, 1500])]
    out += [[ints(n, lo, hi, 4520 + i)] for i, (n, lo, hi) in enumerate(
        [(12, -5, 5), (30, -8, 8), (80, -20, 20), (150, -40, 40), (300, -200, 200),
         (600, -2000, 2000), (900, -10 ** 4, 10 ** 4), (1200, -10 ** 4, 10 ** 4)])]
    out += [
        [G("repeat", value=0, n=300)],
        [G("concat", parts=[G("repeat", value=0, n=150), G("repeat", value=1, n=150)])],
        [ints(400, -3, 3, 4510)],
        [ints(1000, -50, 50, 4511)],
        [G("arange", n=600, start=-300)],
        [ints(1500, 1, 10 ** 5, 4512)],          # all positive: no triplet
        [ints(1500, -10 ** 5, -1, 4513)],        # all negative: no triplet
        [[-1, 0, 1, 2, -1, -4]], [[0, 1, 1]], [[0, 0, 0]], [[0, 0, 0, 0]], [[-2, 0, 1, 1, 2]],
    ]
    return out


@cases("search-in-rotated-sorted-array")
def _search_rotated():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 8, 20, 100, 1000, 5000]):
        base = G("sorted", n=n, lo=-10 ** 4, hi=10 ** 4, seed=4600 + i, unique=True, step=3)
        values = expand(base)
        for by in {0, 1, len(values) // 3, len(values) // 2, len(values) - 1}:
            spec = G("rotate", of=base, by=by)
            rotated = expand(spec)
            out.append([spec, rotated[0]])
            out.append([spec, rotated[-1]])
            out.append([spec, rotated[len(rotated) // 2]])
            out.append([spec, values[-1] + 1])
    out += [[[4, 5, 6, 7, 0, 1, 2], 0], [[4, 5, 6, 7, 0, 1, 2], 3], [[1], 0], [[1], 1], [[3, 1], 1]]
    return out


@cases("validate-binary-search-tree")
def _validate_bst():
    out = [[level_order(n, 4700 + i, sorted_bst=True, values=(-10 ** 5, 10 ** 5))]
           for i, n in enumerate([1, 2, 3, 5, 10, 40, 200, 1000, 2000])]
    # Same shapes, but with the values scrambled — almost never a BST.
    for i, n in enumerate([3, 7, 20, 100, 800]):
        tree = level_order(n, 4700 + i, sorted_bst=True, values=(-10 ** 5, 10 ** 5))
        rotated = [v for v in tree if v is not None]
        rotated = rotated[1:] + rotated[:1]
        it = iter(rotated)
        out.append([[None if v is None else next(it) for v in tree]])
    out += [
        [level_order(500, 4800, values=(-50, 50))],
        [level_order(200, 4801, null_rate=30, values=(-50, 50))],
        [chain(300)], [chain(300, right=False)],
        [[]], [[1]], [[2, 1, 3]], [[5, 1, 4, None, None, 3, 6]], [[1, 1]],
        [[10, 5, 15, None, None, 6, 20]], [[2, 2, 2]], [[0, -1]],
    ]
    return out


@cases("binary-tree-level-order-traversal")
def _level_order_traversal():
    out = [[level_order(n, 4900 + i)] for i, n in enumerate([0, 1, 2, 3, 7, 15, 63, 255, 1000, 2000])]
    out += [[level_order(n, 5000 + i, null_rate=35)] for i, n in enumerate([10, 60, 400, 1500])]
    out += [[level_order(n, 5050 + i, values=(-9, 9))] for i, n in enumerate([4, 9, 30, 120, 700])]
    out += [
        [chain(500)], [chain(500, right=False)],
        [[]], [[1]], [[1, 2, 3]], [[3, 9, 20, None, None, 15, 7]], [[1, None, 2, None, 3]],
    ]
    return out


@cases("house-robber")
def _house_robber():
    out = [[ints(n, 0, 400, 5100 + i)] for i, n in enumerate([1, 2, 3, 4, 5, 10, 50, 500, 5000, 100000])]
    out += [
        [G("repeat", value=400, n=100000)],
        [G("repeat", value=0, n=100000)],
        [G("arange", n=100000, start=0, step=1)],
        [G("arange", n=100000, start=100000, step=-1)],
        [ints(100000, 0, 1, 5120)],
        [ints(100000, 395, 400, 5121)],
        [[0]], [[1]], [[1, 2]], [[2, 1]], [[2, 7, 9, 3, 1]], [[1, 2, 3, 1]], [[2, 1, 1, 2]],
    ]
    return out


@cases("longest-consecutive-sequence")
def _longest_consecutive():
    out = [[ints(n, -50, 50, 5200 + i)] for i, n in enumerate([0, 1, 2, 3, 6, 20, 100, 1000])]
    out += [
        [G("perm", n=100000)],                                   # one run of 100000
        [G("shuffle", of=G("arange", n=100000, start=-50000), seed=5210)],
        [ints(100000, -10 ** 9, 10 ** 9, 5211)],                 # sparse: mostly runs of 1
        [ints(100000, 0, 5000, 5212)],
        [G("repeat", value=3, n=100000)],
        [G("arange", n=100000, start=0, step=2)],                # no two consecutive
        [G("shuffle", of=G("concat", parts=[G("arange", n=50000), G("arange", n=50000, start=200000, step=2)]), seed=5213)],
        [[100, 4, 200, 1, 3, 2]], [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], [[1]], [[1, 2]], [[2, 1]], [[]],
    ]
    return out


# --------------------------------------------------------------- advanced


@cases("word-break")
def _word_break():
    out = []
    for i, n in enumerate([1, 2, 5, 20, 100, 300]):
        out.append([text(n, 5300 + i, "ab"), ["a", "b", "ab", "ba", "aab"]])
        out.append([text(n, 5310 + i, "abc"), ["ab", "bc", "ca", "abc", "cab"]])
    # The classic blow-up for memo-less recursion: one letter short of a match.
    for n in (40, 100, 200, 300):
        out.append([G("concat", parts=[G("strrepeat", value="a", n=n - 1), "b"]),
                    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"]])
        out.append([G("strrepeat", value="a", n=n),
                    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"]])
    out += [
        [G("strrepeat", value="cat", n=100), ["cat", "cats", "and", "sand", "dog"]],
        [G("strrepeat", value="leetcode", n=37), ["leet", "code"]],
        [G("concat", parts=[G("strrepeat", value="leetcode", n=37), "x"]), ["leet", "code"]],
        ["leetcode", ["leet", "code"]],
        ["applepenapple", ["apple", "pen"]],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
        ["a", ["a"]], ["a", ["b"]], ["ab", ["a", "b"]], ["aaaaaaa", ["aaaa", "aaa"]],
        ["bb", ["a", "b", "bbb", "bbbb"]], ["cars", ["car", "ca", "rs"]],
    ]
    return out


@cases("spiral-matrix")
def _spiral_matrix():
    out = []
    for i, (rows, cols) in enumerate([(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (3, 4), (4, 3),
                                      (1, 40), (40, 1), (10, 10), (17, 23), (40, 40), (55, 60)]):
        out.append([G("grid", rows=rows, cols=cols, lo=-100, hi=100, seed=5400 + i)])
    for i, (rows, cols) in enumerate([(2, 59), (59, 2), (60, 60), (7, 60), (60, 7)]):
        out.append([G("grid", rows=rows, cols=cols, lo=0, hi=9, seed=5500 + i)])
    out += [
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]],
        [[[1]]], [[[1, 2]]], [[[1], [2]]], [[[1, 2], [3, 4]]],
        [[[7, 9, 6], [2, 8, 4], [3, 5, 1]]],
    ]
    return out


@cases("rotate-image")
def _rotate_image():
    out = [[G("grid", rows=n, cols=n, lo=-1000, hi=1000, seed=5600 + i)]
           for i, n in enumerate([1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 45, 60])]
    out += [[G("grid", rows=n, cols=n, lo=0, hi=1, seed=5700 + i)] for i, n in enumerate([2, 7, 16, 33, 60])]
    out += [
        [[[1]]], [[[1, 2], [3, 4]]], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]],
        [[[0, 0], [0, 0]]], [[[-1, -2], [-3, -4]]],
    ]
    return out


@cases("kth-largest-element-in-an-array")
def _kth_largest():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 10, 50, 500, 5000, 50000, 100000]):
        spec = ints(n, -10 ** 4, 10 ** 4, 5800 + i)
        for k in {1, 2, n // 2 or 1, n}:
            out.append([spec, k])
    out += [
        [G("repeat", value=3, n=100000), 1],
        [G("repeat", value=3, n=100000), 100000],
        [G("perm", n=100000), 1],
        [G("perm", n=100000), 50000],
        [G("arange", n=100000, start=-50000), 99999],
        [ints(100000, 0, 1, 5820), 40000],
        [[1], 1], [[2, 1], 1], [[2, 1], 2], [[3, 2, 1, 5, 6, 4], 2],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
    ]
    return out


@cases("unique-paths")
def _unique_paths():
    grid_sizes = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 2), (3, 7), (7, 3), (5, 5), (10, 10),
                  (12, 17), (20, 20), (1, 100), (100, 1), (2, 100), (100, 2), (30, 40),
                  (50, 50), (60, 70), (80, 90), (99, 99), (100, 100), (100, 99), (17, 83),
                  (45, 61), (23, 100), (100, 23), (64, 64), (33, 77), (88, 12), (7, 96)]
    return [[m, n] for m, n in grid_sizes]


def _all_longest_palindromes(args):
    """Every distinct longest palindromic substring — the problem accepts any."""
    s = args[0]
    best = 0
    found = []
    for center in range(len(s)):
        for lo, hi in ((center, center), (center, center + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            candidate = s[lo + 1:hi]
            if len(candidate) > best:
                best = len(candidate)
                found = [candidate]
            elif len(candidate) == best and candidate not in found:
                found.append(candidate)
    return found or [""]


@cases("longest-palindromic-substring", expected=_all_longest_palindromes)
def _longest_palindrome():
    out = [[text(n, 5900 + i, "ab")] for i, n in enumerate([1, 2, 3, 5, 10, 50, 300, 1000])]
    out += [[text(n, 5910 + i, "abcdefghij")] for i, n in enumerate([10, 100, 1000])]
    out += [[text(n, 5920 + i)] for i, n in enumerate([20, 200, 1000])]
    out += [
        [G("strrepeat", value="a", n=1000)],
        [G("strrepeat", value="ab", n=500)],
        [G("concat", parts=[G("strrepeat", value="a", n=500), G("strrepeat", value="b", n=500)])],
        [G("concat", parts=[G("strrepeat", value="a", n=499), "b", G("strrepeat", value="a", n=500)])],
        [G("concat", parts=[text(400, 5930), G("strrepeat", value="z", n=200), text(400, 5931)])],
        [text(1000, 5940, "ab")],
        ["a"], ["ab"], ["aa"], ["aba"], ["abba"], ["babad"], ["cbbd"], ["racecarx"], ["abcda"],
    ]
    return out


def board_with_word(rows, cols, word, seed, fill="abcdefgh"):
    """A board with `word` laid along a self-avoiding walk, rest filled randomly."""
    rng = Rng(seed)
    board = [[fill[rng.below(len(fill))] for _ in range(cols)] for _ in range(rows)]
    r, c = rng.below(rows), rng.below(cols)
    used = {(r, c)}
    path = [(r, c)]
    for _ in range(len(word) - 1):
        options = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                   if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in used]
        if not options:
            return None
        r, c = options[rng.below(len(options))]
        used.add((r, c))
        path.append((r, c))
    for (y, x), ch in zip(path, word):
        board[y][x] = ch
    return board


@cases("word-search")
def _word_search():
    out = []
    for i, (rows, cols, length) in enumerate([(1, 1, 1), (1, 6, 3), (6, 1, 3), (3, 3, 4), (4, 4, 6),
                                              (6, 6, 8), (8, 8, 12), (10, 10, 15), (12, 12, 20),
                                              (6, 6, 10), (5, 5, 9)]):
        word = expand(text(length, 6000 + i, "abcd"))
        board = board_with_word(rows, cols, word, 6100 + i, fill="abcd")
        if board:
            out.append([board, word])                                   # present
            out.append([board, word + "z"])                             # absent: no 'z' anywhere
    for i, (rows, cols) in enumerate([(4, 4), (8, 8), (12, 12), (6, 6)]):
        board = [list(expand(text(cols, 6200 + i * 10 + r, "ab"))) for r in range(rows)]
        out.append([board, "ab" * 6])
        out.append([board, "a" * 5 + "c"])
    out += [
        # Backtracking bombs: every cell matches until the very last letter.
        [[list("aaaaa") for _ in range(5)], "aaaaaaaaab"],
        [[list("aaaaaa") for _ in range(6)], "aaaaaaaaaaab"],
        [[list("aaaa") for _ in range(4)], "aaaaaaaa"],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
        [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"],
        [[["a"]], "a"], [[["a"]], "b"], [[["a", "b"]], "ba"], [[["a"], ["b"]], "ab"],
    ]
    return out


@cases("longest-increasing-subsequence")
def _lis():
    out = [[ints(n, -10 ** 4, 10 ** 4, 6300 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 50, 500, 2500])]
    out += [
        [G("arange", n=2500)],                       # already increasing
        [G("arange", n=2500, start=2500, step=-1)],  # strictly decreasing
        [G("repeat", value=1, n=2500)],
        [G("perm", n=2500)],
        [ints(2500, 0, 10, 6320)],
        [ints(2500, -10 ** 4, 10 ** 4, 6321)],
        [G("concat", parts=[G("arange", n=1250), G("arange", n=1250, start=1250, step=-1)])],
        [G("shuffle", of=G("arange", n=2000), seed=6330)],
        [[10, 9, 2, 5, 3, 7, 101, 18]], [[0, 1, 0, 3, 2, 3]], [[7, 7, 7, 7]], [[1]], [[2, 1]], [[1, 2]],
    ]
    return out


@cases("edit-distance")
def _edit_distance():
    out = []
    for i, (a, b) in enumerate([(0, 0), (0, 3), (3, 0), (1, 1), (5, 5), (20, 25), (100, 100),
                                (300, 200), (500, 500), (500, 1)]):
        out.append([text(a, 6400 + i, "abc"), text(b, 6500 + i, "abc")])
    for i, n in enumerate([50, 200, 500]):
        same = text(n, 6600 + i)
        out.append([same, same])
        out.append([same, G("shuffle", of=same, seed=6700 + i)])
    out += [
        [G("strrepeat", value="a", n=500), G("strrepeat", value="b", n=500)],
        [G("strrepeat", value="a", n=500), G("strrepeat", value="a", n=499)],
        [G("strrepeat", value="ab", n=250), G("strrepeat", value="ba", n=250)],
        [text(500, 6710, "ab"), text(500, 6711, "ab")],
        ["horse", "ros"], ["intention", "execution"], ["", ""], ["a", ""], ["", "a"],
        ["a", "a"], ["ab", "ba"], ["abc", "abc"],
    ]
    return out


@cases("trapping-rain-water")
def _trapping_rain_water():
    out = [[ints(n, 0, 100, 6800 + i)] for i, n in enumerate([0, 1, 2, 3, 5, 20, 200, 2000, 20000])]
    out += [
        [ints(20000, 0, 3, 6820)],
        [ints(20000, 0, 10 ** 5, 6821)],
        [G("arange", n=20000)],                                  # monotone: traps nothing
        [G("arange", n=20000, start=20000, step=-1)],
        [G("repeat", value=5, n=20000)],
        [G("concat", parts=[[100000], G("repeat", value=0, n=19998), [100000]])],   # one huge basin
        [G("concat", parts=[G("arange", n=10000), G("arange", n=10000, start=10000, step=-1)])],
        [G("concat", parts=[G("arange", n=10000, start=10000, step=-1), G("arange", n=10000)])],
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], [[4, 2, 0, 3, 2, 5]], [[]], [[1]], [[1, 2]], [[2, 0, 2]],
    ]
    return out


@cases("median-of-two-sorted-arrays")
def _median_two_sorted():
    out = []
    for i, (a, b) in enumerate([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (5, 5), (10, 3),
                                (100, 100), (1000, 1), (1000, 1000)]):
        first = G("sorted", n=a, lo=-10 ** 5, hi=10 ** 5, seed=6900 + i) if a else []
        second = G("sorted", n=b, lo=-10 ** 5, hi=10 ** 5, seed=7000 + i) if b else []
        out.append([first, second])
    out += [
        [G("arange", n=1000), G("arange", n=1000, start=1000)],
        [G("arange", n=1000, start=0, step=2), G("arange", n=1000, start=1, step=2)],
        [G("repeat", value=1, n=1000), G("repeat", value=1, n=1000)],
        [G("repeat", value=0, n=1000), G("repeat", value=1, n=1)],
        [G("arange", n=999), G("arange", n=1000, start=-1000)],
        [[1, 3], [2]], [[1, 2], [3, 4]], [[], [1]], [[2], []], [[0, 0], [0, 0]],
        [[1, 2, 3], [4, 5, 6]], [[1], [2, 3, 4, 5]],
    ]
    return out


@cases("merge-k-sorted-lists")
def _merge_k_lists():
    out = []
    for i, (k, each) in enumerate([(0, 0), (1, 0), (1, 1), (2, 1), (3, 3), (5, 10), (10, 50),
                                   (25, 100), (100, 50), (500, 10)]):
        lists = [G("sorted", n=each, lo=-1000, hi=1000, seed=7100 + i * 37 + j) if each else []
                 for j in range(k)]
        out.append([lists])
    for i, (k, each) in enumerate([(2, 2), (3, 1), (4, 20), (6, 60), (8, 8), (12, 100),
                                   (30, 40), (60, 20), (200, 10), (1000, 2)]):
        out.append([[G("sorted", n=each, lo=-500, hi=500, seed=7300 + i * 53 + j) for j in range(k)]])
    out += [
        [[G("arange", n=1000), G("arange", n=1000, start=1000), G("arange", n=1000, start=2000)]],
        [[G("repeat", value=0, n=1000), G("repeat", value=0, n=1000)]],
        [[G("arange", n=2000, start=0, step=2), G("arange", n=2000, start=1, step=2)]],
        [[[] for _ in range(100)]],
        [[G("sorted", n=2500, lo=-10 ** 4, hi=10 ** 4, seed=7200),
          G("sorted", n=2500, lo=-10 ** 4, hi=10 ** 4, seed=7201)]],
        [[[1, 4, 5], [1, 3, 4], [2, 6]]], [[]], [[[]]], [[[1]]], [[[], [1]]], [[[2], [1]]],
    ]
    return out


def _min_window_unique(args, _expected):
    """Keep only inputs where every shortest valid window spells the same
    substring, which is what the problem promises."""
    s, t = args
    if not t or len(t) > len(s):
        return True
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    best = len(s) + 1
    texts = set()
    have = dict(need)
    left = 0
    for right, ch in enumerate(s):
        if have.get(ch, 0) > 0:
            missing -= 1
        have[ch] = have.get(ch, 0) - 1
        while missing == 0:
            width = right - left + 1
            if width < best:
                best = width
                texts = {s[left:right + 1]}
            elif width == best:
                texts.add(s[left:right + 1])
            have[s[left]] = have.get(s[left], 0) + 1
            if have[s[left]] > 0:
                missing += 1
            left += 1
    return len(texts) <= 1


@cases("minimum-window-substring", validate=_min_window_unique)
def _minimum_window():
    out = []
    for i, (n, m, alphabet) in enumerate([(1, 1, "ab"), (5, 2, "ab"), (20, 3, "abc"), (100, 5, "abcde"),
                                          (1000, 8, "abcdefgh"), (10000, 10, LOWER),
                                          (100000, 12, LOWER), (100000, 3, "abc"),
                                          (50000, 26, LOWER), (5000, 15, "abcdef")]):
        out.append([text(n, 7300 + i, alphabet), text(m, 7400 + i, alphabet)])
    for i, n in enumerate([500, 5000, 50000]):
        out.append([text(n, 7500 + i, "ab"), "ab"])
        out.append([text(n, 7510 + i, LOWER), "xyz"])
    for i in range(14):
        n = [8, 16, 32, 64, 128, 256, 512, 2000, 8000, 20000, 60000, 100000, 100000, 30000][i]
        alphabet = LOWER[: 2 + (i % 8) * 3]
        out.append([text(n, 7600 + i, alphabet), text(2 + i % 6, 7700 + i, alphabet)])
    out += [
        [G("concat", parts=[G("strrepeat", value="a", n=50000), "b"]), "ab"],
        [G("concat", parts=["b", G("strrepeat", value="a", n=50000)]), "ab"],
        [G("strrepeat", value="a", n=50000), "a"],
        [G("strrepeat", value="a", n=50000), "aa"],
        [G("concat", parts=[G("strrepeat", value="ab", n=25000), "c"]), "abc"],
        ["ADOBECODEBANC", "ABC"], ["a", "a"], ["a", "aa"], ["a", "b"], ["ab", "b"], ["bba", "ab"],
    ]
    return out


# ------------------------------------------------------------------ top-ups
#
# Problems whose earlier blocks came up short of the 35-case target once
# oversized answers were dropped at build time.


def add(slug, more):
    entry = REGISTRY[slug]
    make = entry["make"]
    entry["make"] = lambda: make() + more


def sweep(sizes, lo, hi, seed0):
    return [[ints(n, lo, hi, seed0 + i)] for i, n in enumerate(sizes)]


add("longest-consecutive-sequence", sweep([4, 9, 40, 300, 3000, 30000, 70000], -10 ** 5, 10 ** 5, 5300)
    + sweep([50000, 100000], -200, 200, 5320)
    + [[G("shuffle", of=G("arange", n=60000, start=-30000, step=3), seed=5330)],
       [G("concat", parts=[G("arange", n=40000), G("repeat", value=0, n=40000)])]])

add("move-zeroes", sweep([700, 1100, 1600, 2100, 2300, 2400], 0, 4, 1260)
    + [[G("shuffle", of=G("concat", parts=[G("repeat", value=0, n=1200), G("arange", n=1200, start=1)]), seed=1270)],
       [G("concat", parts=[G("repeat", value=0, n=1), G("perm", n=2399, base=1)])]])

add("longest-increasing-subsequence", sweep([4, 8, 20, 120, 700, 1500, 2000, 2400], -500, 500, 6340)
    + [[G("shuffle", of=G("arange", n=2400, start=-1200), seed=6350)],
       [G("concat", parts=[G("arange", n=1200, start=1200, step=-1), G("arange", n=1200)])]])

add("majority-element", [
    [G("shuffle", of=G("concat", parts=[G("repeat", value=v, n=n // 2 + 1), ints(n - n // 2 - 1, -20, 20, 2600 + i)]),
       seed=2700 + i)]
    for i, (n, v) in enumerate([(7, 4), (33, -1), (129, 0), (513, 9), (2049, -7), (8193, 3),
                                (32769, 11), (75001, -2), (99999, 6)])])

add("median-of-two-sorted-arrays", [
    [G("sorted", n=a, lo=-10 ** 4, hi=10 ** 4, seed=7010 + i),
     G("sorted", n=b, lo=-10 ** 4, hi=10 ** 4, seed=7060 + i)]
    for i, (a, b) in enumerate([(3, 3), (4, 4), (6, 2), (2, 6), (9, 11), (25, 25), (60, 40),
                                (250, 250), (700, 300), (1000, 999)])])

add("rotate-image", [[G("grid", rows=n, cols=n, lo=-9, hi=9, seed=5750 + i)]
                     for i, n in enumerate([7, 9, 11, 13, 18, 24, 36, 48, 55, 60])])

add("group-anagrams", [[G("words", n=n, minLen=lo, maxLen=hi, alphabet=alphabet, seed=3300 + i)]
                       for i, (n, lo, hi, alphabet) in enumerate(
                           [(6, 1, 3, "ab"), (30, 2, 4, "abc"), (120, 1, 5, "abcd"),
                            (400, 2, 6, "abcde"), (700, 3, 3, "abc"), (900, 1, 2, "abcdef"),
                            (1500, 2, 5, "abc"), (2000, 1, 3, "ab")])])

add("house-robber", sweep([6, 20, 200, 2000, 20000, 60000, 100000], 0, 1000, 5140)
    + [[G("shuffle", of=G("arange", n=80000), seed=5150)],
       [G("concat", parts=[G("repeat", value=1, n=50000), G("repeat", value=1000, n=50000)])]])

add("maximum-subarray", sweep([4, 12, 80, 800, 8000, 80000, 150000], -10 ** 4, 10 ** 4, 5160)
    + [[G("concat", parts=[ints(50000, -10, 10, 5170), [10 ** 4], ints(50000, -10, 10, 5171)])],
       [G("shuffle", of=G("arange", n=100000, start=-50000), seed=5172)]])

add("number-of-islands", [[G("grid", rows=r, cols=c, alphabet=a, asString=False, seed=4020 + i)]
                          for i, (r, c, a) in enumerate(
                              [(2, 2, "01"), (4, 9, "01"), (9, 4, "011"), (25, 25, "0011"),
                               (50, 50, "01"), (80, 120, "0001"), (60, 60, "0111"),
                               (250, 250, "01"), (300, 120, "0011"), (300, 300, "0001")])])

add("trapping-rain-water", sweep([4, 9, 40, 400, 4000, 12000, 20000], 0, 1000, 6830)
    + [[G("shuffle", of=G("arange", n=20000), seed=6840)],
       [G("concat", parts=[G("repeat", value=0, n=10000), G("repeat", value=1000, n=10000)])]])

add("spiral-matrix", [[G("grid", rows=r, cols=c, lo=-50, hi=50, seed=5550 + i)]
                      for i, (r, c) in enumerate([(1, 3), (3, 1), (2, 3), (3, 2), (5, 9), (9, 5),
                                                  (12, 12), (25, 30), (33, 33), (45, 50)])])

add("climbing-stairs", [[n] for n in [11, 13, 14, 16, 17, 19, 21, 22, 24, 26, 27, 29, 31, 33, 35, 37, 39]])

add("merge-two-sorted-lists", [
    [G("sorted", n=a, lo=-200, hi=200, seed=1750 + i), G("sorted", n=b, lo=-200, hi=200, seed=1790 + i)]
    for i, (a, b) in enumerate([(4, 4), (6, 3), (3, 6), (12, 12), (40, 40), (150, 90), (90, 150),
                                (400, 400), (800, 700), (1100, 1100)])])

add("merge-k-sorted-lists", [
    [[G("sorted", n=each, lo=-300, hi=300, seed=7400 + i * 31 + j) for j in range(k)]]
    for i, (k, each) in enumerate([(2, 5), (3, 8), (5, 5), (7, 30), (9, 90), (15, 60),
                                   (40, 30), (80, 15), (150, 8), (400, 5)])])

add("reverse-linked-list", sweep([12, 45, 90, 180, 360, 720, 1400, 2000, 2400], -500, 500, 1560))

add("3sum", [[ints(n, lo, hi, 4560 + i)] for i, (n, lo, hi) in enumerate(
    [(7, -4, 4), (18, -6, 6), (45, -12, 12), (120, -30, 30), (250, -120, 120),
     (500, -900, 900), (750, -5000, 5000), (1000, -10 ** 5, 10 ** 5)])])

add("binary-tree-level-order-traversal", [[level_order(n, 5080 + i, null_rate=45)]
                                          for i, n in enumerate([6, 18, 45, 130, 350, 900, 1800])])

add("invert-binary-tree", [[level_order(n, 1970 + i, null_rate=25)]
                           for i, n in enumerate([5, 14, 45, 130, 400, 1200])])

add("maximum-depth-of-binary-tree", [[level_order(n, 2170 + i, null_rate=20)]
                                     for i, n in enumerate([6, 20, 70, 250, 800, 2500])])

add("validate-binary-search-tree", [[level_order(n, 4820 + i, sorted_bst=True, values=(-10 ** 6, 10 ** 6))]
                                    for i, n in enumerate([4, 8, 25, 80, 260, 900, 1800])])

add("contains-duplicate", sweep([4, 25, 250, 2500, 25000, 150000], -10 ** 5, 10 ** 5, 740))

add("best-time-to-buy-and-sell-stock", sweep([4, 30, 300, 3000, 30000, 150000], 0, 10 ** 4, 630))

add("longest-substring-without-repeating-characters",
    [[text(n, 3340 + i, alphabet)] for i, (n, alphabet) in enumerate(
        [(4, "ab"), (30, "abc"), (300, "abcd"), (3000, "abcdef"), (30000, LOWER[:12]),
         (100000, LOWER), (100000, "abc")])])

add("top-k-frequent-elements", [[ints(n, 0, hi, 3650 + i), k] for i, (n, hi, k) in enumerate(
    [(8, 3, 2), (40, 6, 3), (400, 12, 4), (4000, 25, 8), (40000, 60, 15), (100000, 250, 30)])])

add("product-of-array-except-self", [[ints(n, -1, 1, 3430 + i)] for i, n in enumerate(
    [4, 9, 30, 120, 400, 900, 1500, 2000])])

add("unique-paths", [[m, n] for m, n in [(3, 3), (4, 9), (9, 4), (15, 15), (22, 8), (8, 22),
                                         (37, 52), (52, 37), (71, 71), (95, 40)]])

add("course-schedule", [[nodes, G("edges", n=count, nodes=nodes, seed=4320 + i, dag=bool(i % 2))]
                        for i, (nodes, count) in enumerate(
                            [(4, 3), (8, 12), (16, 24), (64, 100), (256, 500), (700, 1500),
                             (1500, 3000), (3000, 6000)])])

add("word-break", [[text(n, 5330 + i, "ab"), ["a", "aa", "ab", "b", "bb", "aab", "bba"]]
                   for i, n in enumerate([8, 24, 60, 140, 220, 300])])

add("coin-change", [[G("sorted", n=k, lo=1, hi=hi, seed=3850 + i, unique=True), amount]
                    for i, (k, hi, amount) in enumerate(
                        [(1, 3, 97), (2, 9, 253), (3, 25, 999), (5, 60, 3001), (8, 150, 7777),
                         (11, 400, 9541)])])

add("edit-distance", [[text(a, 6720 + i, "abcd"), text(b, 6760 + i, "abcd")]
                      for i, (a, b) in enumerate([(3, 4), (8, 6), (30, 35), (120, 90), (250, 250),
                                                  (400, 380), (500, 450)])])

add("longest-palindromic-substring", [[text(n, 5950 + i, alphabet)] for i, (n, alphabet) in enumerate(
    [(4, "ab"), (25, "ab"), (120, "abc"), (400, "abc"), (900, "abcd"), (1000, "ab")])])
