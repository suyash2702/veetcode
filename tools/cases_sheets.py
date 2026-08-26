"""Extra test cases for the sheet problems (see tools/cases.py for the rules)."""

from cases import G, LOWER, add, cases, expand, ints, sweep, text  # noqa: F401

# --------------------------------------------------------- arrays and matrix


@cases("set-matrix-zeroes")
def _set_matrix_zeroes():
    out = []
    for i, (rows, cols, hi) in enumerate([(1, 1, 1), (1, 5, 2), (5, 1, 2), (2, 2, 1), (3, 4, 3),
                                          (8, 8, 5), (15, 15, 8), (25, 25, 12), (40, 40, 20),
                                          (55, 55, 40), (60, 60, 60), (12, 47, 9), (47, 12, 9)]):
        out.append([G("grid", rows=rows, cols=cols, lo=0, hi=hi, seed=8000 + i)])
    for i, (rows, cols) in enumerate([(3, 3), (6, 6), (20, 20), (45, 45), (60, 60)]):
        out.append([G("grid", rows=rows, cols=cols, lo=1, hi=9, seed=8020 + i)])       # no zeros at all
        out.append([G("grid", rows=rows, cols=cols, lo=0, hi=1, seed=8030 + i)])       # zeros everywhere
    out += [
        [[[1]]], [[[0]]], [[[1, 0]]], [[[0], [1]]], [[[1, 1], [1, 1]]], [[[0, 0], [0, 0]]],
        [[[1, 2, 3], [4, 0, 6], [7, 8, 9]]], [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]],
    ]
    return out


@cases("pascals-triangle")
def _pascals_triangle():
    return [[n] for n in range(1, 35)]


@cases("next-permutation")
def _next_permutation():
    out = [[ints(n, 0, 100, 8100 + i)] for i, n in enumerate([1, 2, 3, 4, 5, 8, 20, 100, 1000, 2400])]
    out += [
        [G("perm", n=2400)], [G("arange", n=2400)], [G("arange", n=2400, start=2400, step=-1)],
        [G("repeat", value=5, n=2400)], [ints(2400, 0, 1, 8120)], [ints(2400, 0, 3, 8121)],
        [G("concat", parts=[G("arange", n=1200), G("arange", n=1200, start=1200, step=-1)])],
        [[1, 2, 3]], [[3, 2, 1]], [[1, 1, 5]], [[1]], [[1, 3, 2]], [[2, 3, 1]], [[5, 1, 1]],
        [[1, 5, 1]], [[2, 2, 7, 5, 4, 3, 2, 2, 1]],
    ]
    return out


@cases("sort-colors")
def _sort_colors():
    out = [[ints(n, 0, 2, 8200 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 40, 200, 900, 1800, 2400])]
    out += [
        [G("repeat", value=0, n=2400)], [G("repeat", value=1, n=2400)], [G("repeat", value=2, n=2400)],
        [G("concat", parts=[G("repeat", value=2, n=800), G("repeat", value=1, n=800), G("repeat", value=0, n=800)])],
        [G("concat", parts=[G("repeat", value=0, n=1200), G("repeat", value=2, n=1200)])],
        [ints(2400, 0, 1, 8220)], [ints(2400, 1, 2, 8221)],
        [[0]], [[1]], [[2]], [[1, 0]], [[2, 0, 1]], [[2, 0, 2, 1, 1, 0]], [[0, 1, 2]], [[2, 1, 0]],
    ]
    return out


@cases("merge-intervals")
def _merge_intervals():
    out = [[G("intervals", n=n, lo=0, hi=hi, maxLen=span, seed=8300 + i)]
           for i, (n, hi, span) in enumerate([(1, 10, 3), (2, 10, 3), (3, 20, 5), (8, 30, 6),
                                              (30, 100, 8), (150, 500, 10), (600, 2000, 12),
                                              (1500, 5000, 15), (1500, 200, 5), (1200, 10 ** 6, 20)])]
    out += [[G("disjoint", n=n, gap=gap, maxLen=span, seed=8320 + i)]
            for i, (n, gap, span) in enumerate([(5, 3, 2), (50, 4, 3), (500, 6, 4), (1500, 5, 5)])]
    out += [
        [G("intervals", n=2000, lo=0, hi=5, maxLen=3, seed=8340)],       # nearly everything merges
        [G("intervals", n=2000, lo=0, hi=10 ** 6, maxLen=1, seed=8341)],  # nearly nothing merges
        [G("repeat", value=[3, 7], n=1500)],
        [[[1, 3], [2, 6], [8, 10], [15, 18]]], [[[1, 4], [4, 5]]], [[[1, 4], [0, 4]]],
        [[[1, 4], [2, 3]]], [[[1, 1]]], [[[0, 0], [0, 0]]], [[[2, 3], [4, 5], [6, 7], [1, 10]]],
    ]
    return out


@cases("insert-interval")
def _insert_interval():
    out = []
    for i, (n, gap, span) in enumerate([(0, 3, 2), (1, 3, 2), (2, 4, 3), (10, 4, 3), (60, 5, 4),
                                        (300, 6, 5), (1200, 5, 5), (3000, 4, 4)]):
        spec = G("disjoint", n=n, gap=gap, maxLen=span, seed=8400 + i) if n else []
        values = expand(spec) if n else []
        span_end = values[-1][1] if values else 10
        out.append([spec, [0, span_end + 5]])                       # swallows everything
        out.append([spec, [span_end + 10, span_end + 12]])          # lands after the end
        out.append([spec, [-5, -1]])                                # lands before the start
        if values:
            mid = values[len(values) // 2]
            out.append([spec, [mid[0] - 1, mid[1] + 1]])            # overlaps one
            out.append([spec, [values[0][1] + 1, mid[1]]])          # overlaps a run
    out += [
        [[[1, 3], [6, 9]], [2, 5]],
        [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]],
        [[], [5, 7]], [[[1, 5]], [2, 3]], [[[1, 5]], [6, 8]], [[[1, 5]], [0, 0]],
    ]
    return out


@cases("non-overlapping-intervals")
def _non_overlapping_intervals():
    out = [[G("intervals", n=n, lo=0, hi=hi, maxLen=span, seed=8500 + i)]
           for i, (n, hi, span) in enumerate([(1, 10, 3), (2, 10, 3), (5, 20, 4), (20, 50, 5),
                                              (100, 200, 6), (800, 1000, 8), (3000, 5000, 10),
                                              (10000, 20000, 12), (10000, 100, 5), (5000, 10 ** 6, 20)])]
    out += [[G("disjoint", n=n, gap=2, maxLen=1, seed=8520 + i)] for i, n in enumerate([10, 500, 5000])]
    out += [
        [G("repeat", value=[1, 2], n=5000)],
        [G("intervals", n=5000, lo=0, hi=3, maxLen=2, seed=8530)],
        [[[1, 2], [2, 3], [3, 4], [1, 3]]], [[[1, 2], [1, 2], [1, 2]]], [[[1, 2], [2, 3]]],
        [[[1, 100], [11, 22], [1, 11], [2, 12]]], [[[1, 2]]], [[[-5, -1], [-3, 0]]],
    ]
    return out


@cases("find-the-duplicate-number")
def _find_duplicate():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 10, 50, 500, 5000, 50000, 99999]):
        values = expand(G("perm", n=n, base=1, seed=8600 + i))
        extra = values[(i * 7 + 3) % n]
        out.append([G("shuffle", of=G("concat", parts=[G("perm", n=n, base=1, seed=8600 + i), [extra]]),
                      seed=8700 + i)])
    for i, n in enumerate([9, 999, 9999, 99999]):
        out.append([G("concat", parts=[G("perm", n=n, base=1, seed=8720 + i), [1]])])          # duplicate at the end
        out.append([G("concat", parts=[[n], G("perm", n=n, base=1, seed=8730 + i)])])          # duplicate at the front
        out.append([G("repeat", value=1, n=n + 1)])                                            # every value repeats
    out += [
        [[1, 1]], [[1, 3, 4, 2, 2]], [[3, 1, 3, 4, 2]], [[2, 2, 2, 2, 2]], [[1, 1, 2]], [[2, 1, 2]],
    ]
    return out


def _missing_repeating(n, seed):
    """A 1..n permutation with one value overwritten by another."""
    values = expand(G("perm", n=n, base=1, seed=seed))
    missing = values[seed % n]
    repeating = values[(seed * 7 + 1) % n]
    if missing == repeating:
        return None
    return [[repeating if v == missing else v for v in values]]


@cases("missing-and-repeating-number")
def _missing_and_repeating():
    out = []
    for i, n in enumerate([2, 3, 5, 10, 50, 200, 1000, 3000, 5000, 8000, 10000]):
        case = _missing_repeating(n, 8800 + i)
        if case:
            out.append(case)
    for i, n in enumerate([4, 40, 400, 4000]):
        out.append([[1] + list(range(2, n)) + [1]])                     # 1 repeats, n missing
        out.append([[n] + list(range(2, n + 1))])                       # n repeats, 1 missing
    out = [c for c in out if c]
    out += [
        [[3, 1, 2, 5, 3]], [[1, 1]], [[2, 2]], [[4, 3, 6, 2, 1, 1]], [[1, 2, 2, 4]], [[2, 1, 4, 4, 5]],
    ]
    return out


@cases("count-inversions")
def _count_inversions():
    out = [[ints(n, -10 ** 5, 10 ** 5, 8900 + i)] for i, n in enumerate([1, 2, 3, 5, 20, 200, 2000, 20000, 100000])]
    out += [
        [G("arange", n=100000)], [G("arange", n=100000, start=100000, step=-1)],
        [G("perm", n=100000)], [G("repeat", value=7, n=100000)],
        [ints(100000, 0, 1, 8920)], [ints(100000, 0, 9, 8921)],
        [G("concat", parts=[G("arange", n=50000, start=50000, step=-1), G("arange", n=50000)])],
        [G("shuffle", of=G("arange", n=60000), seed=8930)],
        [[2, 4, 1, 3, 5]], [[5, 4, 3, 2, 1]], [[1, 2, 3]], [[1]], [[2, 1]], [[1, 1, 1]],
    ]
    return out


@cases("search-a-2d-matrix")
def _search_a_2d_matrix():
    out = []
    for i, (rows, cols) in enumerate([(1, 1), (1, 8), (8, 1), (3, 4), (10, 10), (40, 40),
                                      (100, 100), (300, 300), (7, 291), (291, 7)]):
        spec = G("sortedgrid", rows=rows, cols=cols, start=-1000, step=7, seed=9000 + i)
        grid = expand(spec)
        flat = [v for row in grid for v in row]
        out.append([spec, flat[0]])
        out.append([spec, flat[-1]])
        out.append([spec, flat[len(flat) // 2]])
        out.append([spec, flat[0] - 1])
        out.append([spec, flat[-1] + 1])
    out += [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
        [[[1]], 1], [[[1]], 2], [[[1, 2]], 2], [[[1], [2]], 2],
    ]
    return out


@cases("majority-element-ii")
def _majority_element_ii():
    out = [[ints(n, 0, hi, 9100 + i)] for i, (n, hi) in enumerate(
        [(1, 1), (2, 2), (3, 2), (5, 3), (15, 4), (90, 6), (900, 8), (9000, 12),
         (90000, 20), (100000, 40)])]
    for i, (n, hi) in enumerate([(30, 2), (300, 3), (3000, 4), (30000, 2), (100000, 5)]):
        out.append([ints(n, 0, hi, 9120 + i)])
    for i, n in enumerate([9, 99, 999, 99999]):
        third = n // 3 + 1
        out.append([G("shuffle", of=G("concat", parts=[G("repeat", value=1, n=third),
                                                       G("repeat", value=2, n=third),
                                                       ints(n - 2 * third, 10, 99, 9140 + i)]), seed=9150 + i)])
    out += [
        [G("repeat", value=4, n=100000)],
        [G("perm", n=100000)],
        [[3, 2, 3]], [[1, 1, 1, 3, 3, 2, 2, 2]], [[1]], [[1, 2]], [[2, 2]], [[1, 2, 3]],
    ]
    return out


@cases("reverse-pairs")
def _reverse_pairs():
    out = [[ints(n, -10 ** 5, 10 ** 5, 9200 + i)] for i, n in enumerate([1, 2, 3, 6, 25, 250, 2500, 25000, 50000])]
    out += [
        [G("arange", n=50000)], [G("arange", n=50000, start=50000, step=-1)],
        [G("perm", n=50000)], [G("repeat", value=-1, n=50000)], [G("repeat", value=0, n=50000)],
        [ints(50000, -10, 10, 9220)], [ints(50000, 0, 3, 9221)],
        [ints(50000, -2 ** 31, 2 ** 31 - 1, 9222)],
        [G("concat", parts=[G("arange", n=25000, start=25000, step=-1), G("arange", n=25000)])],
        [[1, 3, 2, 3, 1]], [[2, 4, 3, 5, 1]], [[1]], [[5, 4, 3, 2, 1]], [[-5, -5]], [[2147483647, -2147483648]],
    ]
    return out


@cases("4sum")
def _four_sum():
    out = []
    for i, (n, lo, hi) in enumerate([(1, -5, 5), (3, -5, 5), (4, -5, 5), (6, -8, 8), (12, -10, 10),
                                     (30, -15, 15), (60, -30, 30), (120, -60, 60), (200, -100, 100),
                                     (200, -10 ** 6, 10 ** 6)]):
        spec = ints(n, lo, hi, 9300 + i)
        values = expand(spec)
        target = sum(values[:4]) if len(values) >= 4 else 0
        out.append([spec, target])
        out.append([spec, 0])
    out += [
        [G("repeat", value=2, n=200), 8],
        [G("repeat", value=0, n=200), 0],
        [ints(200, -2, 2, 9320), 0],
        [ints(200, 1, 10 ** 6, 9321), 0],
        [[1, 0, -1, 0, -2, 2], 0], [[2, 2, 2, 2, 2], 8], [[1, 2, 3], 6], [[0, 0, 0, 0], 0],
        [[-3, -1, 0, 2, 4, 5], 2], [[1000000000, 1000000000, 1000000000, 1000000000], 4000000000],
    ]
    return out


@cases("longest-subarray-with-sum-zero")
def _longest_subarray_zero():
    out = [[ints(n, -3, 3, 9400 + i)] for i, n in enumerate([1, 2, 3, 6, 25, 250, 2500, 25000, 100000])]
    out += [
        [ints(100000, -10 ** 4, 10 ** 4, 9420)],       # sparse: hits are rare
        [ints(100000, -1, 1, 9421)],
        [G("repeat", value=0, n=100000)],
        [G("repeat", value=1, n=100000)],
        [G("concat", parts=[G("repeat", value=1, n=50000), G("repeat", value=-1, n=50000)])],
        [G("concat", parts=[[5], G("repeat", value=0, n=99998), [-5]])],
        [ints(50000, -2, 2, 9422)],
        [[15, -2, 2, -8, 1, 7, 10, 23]], [[1, 2, 3]], [[0]], [[1, -1, 1, -1]], [[-1, 1]], [[1]],
    ]
    return out


@cases("count-subarrays-with-given-xor")
def _count_xor_subarrays():
    out = []
    for i, (n, hi, k) in enumerate([(1, 4, 4), (2, 4, 0), (5, 8, 6), (20, 16, 3), (200, 32, 7),
                                    (2000, 64, 15), (20000, 128, 31), (100000, 256, 63),
                                    (100000, 4, 0), (100000, 10 ** 9, 12345)]):
        out.append([ints(n, 0, hi, 9500 + i), k])
    out += [
        [G("repeat", value=0, n=100000), 0],
        [G("repeat", value=1, n=100000), 1],
        [G("repeat", value=1, n=100000), 0],
        [G("arange", n=100000), 0],
        [ints(100000, 0, 1, 9520), 1],
        [ints(50000, 0, 3, 9521), 3],
        [[4, 2, 2, 6, 4], 6], [[5, 6, 7, 8, 9], 5], [[1], 1], [[0, 0, 0], 0], [[1], 0], [[3, 3], 0],
    ]
    return out


@cases("container-with-most-water")
def _container_with_most_water():
    out = [[ints(n, 0, 10 ** 4, 9600 + i)] for i, n in enumerate([2, 3, 5, 20, 200, 2000, 20000, 100000])]
    out += [
        [G("arange", n=100000)], [G("arange", n=100000, start=100000, step=-1)],
        [G("repeat", value=1000, n=100000)], [ints(100000, 0, 1, 9620)],
        [G("concat", parts=[[10000], G("repeat", value=0, n=99998), [10000]])],
        [G("concat", parts=[G("arange", n=50000), G("arange", n=50000, start=50000, step=-1)])],
        [ints(100000, 9990, 10000, 9621)],
        [[1, 8, 6, 2, 5, 4, 8, 3, 7]], [[1, 1]], [[4, 3, 2, 1, 4]], [[1, 2, 1]], [[0, 2]], [[2, 0]],
    ]
    return out


@cases("max-consecutive-ones")
def _max_consecutive_ones():
    out = [[ints(n, 0, 1, 9700 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000])]
    out += [
        [G("repeat", value=1, n=100000)], [G("repeat", value=0, n=100000)],
        [G("concat", parts=[G("repeat", value=1, n=50000), [0], G("repeat", value=1, n=49999)])],
        [G("concat", parts=[G("repeat", value=0, n=99999), [1]])],
        [G("concat", parts=[[1], G("repeat", value=0, n=99999)])],
        [ints(100000, 0, 3, 9720)],
        [[1, 1, 0, 1, 1, 1]], [[1, 0, 1, 1, 0, 1]], [[0]], [[1]], [[0, 0]], [[1, 1]],
    ]
    return out


@cases("remove-duplicates-from-sorted-array")
def _remove_duplicates():
    out = [[G("sorted", n=n, lo=-10 ** 4, hi=10 ** 4, seed=9800 + i)]
           for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000])]
    out += [[G("sorted", n=n, lo=0, hi=5, seed=9820 + i)] for i, n in enumerate([50, 5000, 100000])]
    out += [
        [G("repeat", value=4, n=100000)],
        [G("arange", n=100000, start=-50000)],
        [G("sorted", n=100000, lo=-10 ** 4, hi=10 ** 4, seed=9830, unique=True)],
        [[1, 1, 2]], [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], [[1]], [[1, 1, 1]], [[1, 2]], [[-1, -1, 0]],
    ]
    return out


@cases("maximum-product-subarray")
def _maximum_product_subarray():
    # Long arrays stay inside {-1, 0, 1} so the answer keeps fitting in 32 bits,
    # exactly as the problem promises.
    out = [[ints(n, -1, 1, 9900 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 20000])]
    out += [[ints(n, -10, 10, 9920 + i)] for i, n in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9])]
    out += [
        [G("repeat", value=1, n=20000)], [G("repeat", value=-1, n=20000)], [G("repeat", value=0, n=20000)],
        [ints(20000, -1, 0, 9940)], [ints(20000, 0, 1, 9941)],
        [G("concat", parts=[G("repeat", value=-1, n=10000), G("repeat", value=1, n=10000)])],
        [[2, 3, -2, 4]], [[-2, 0, -1]], [[-2]], [[-2, 3, -4]], [[0, 2]], [[-3, 0, 1, -2]],
    ]
    return out


@cases("find-minimum-in-rotated-sorted-array")
def _find_minimum_rotated():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 9, 33, 129, 1025, 5000]):
        base = G("sorted", n=n, lo=-5000, hi=5000, seed=10000 + i, unique=True, step=2)
        values = expand(base)
        for by in {0, 1, len(values) // 3, len(values) // 2, len(values) - 1}:
            out.append([G("rotate", of=base, by=by)])
    out += [
        [[3, 4, 5, 1, 2]], [[4, 5, 6, 7, 0, 1, 2]], [[11, 13, 15, 17]], [[1]], [[2, 1]], [[1, 2]],
    ]
    return out


# ------------------------------------------------------------------- strings

PUNCT = "abcABC ,.:!'0123456789"


@cases("valid-palindrome")
def _valid_palindrome():
    out = [[text(n, 10100 + i, PUNCT)] for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 40000, 200000])]
    out += [
        [G("strrepeat", value="a", n=200000)],
        [G("strrepeat", value="ab", n=100000)],
        [G("strrepeat", value="aba", n=60000)],
        [G("strrepeat", value=".,! ", n=50000)],
        [G("concat", parts=[G("strrepeat", value="a", n=100000), G("strrepeat", value="a", n=100000)])],
        [G("concat", parts=[G("strrepeat", value="a", n=99999), "b", G("strrepeat", value="a", n=100000)])],
        [G("concat", parts=[G("strrepeat", value="ab, ", n=50000), G("strrepeat", value=" ,ba", n=50000)])],
        [text(200000, 10120, "aA .")],
        ["A man, a plan, a canal: Panama"], ["race a car"], [" "], ["0P"], ["a"], ["ab"], ["aa"],
        [".,"], ["Was it a car or a cat I saw?"], ["ab_a"],
    ]
    return out


@cases("longest-common-prefix")
def _longest_common_prefix():
    out = []
    for i, (n, length) in enumerate([(1, 1), (2, 3), (3, 5), (10, 8), (50, 20), (200, 50), (200, 200)]):
        prefix = expand(text(max(1, length // 2), 10200 + i))
        words = [prefix + expand(text(length, 10300 + i * 7 + j)) for j in range(n)]
        out.append([words])
        out.append([[expand(text(length, 10400 + i * 7 + j)) for j in range(n)]])
    out += [
        [[expand(G("strrepeat", value="a", n=200))] * 200],
        [[expand(G("strrepeat", value="a", n=200))] * 199 + [expand(G("strrepeat", value="a", n=199)) + "b"]],
        [["flower", "flow", "flight"]], [["dog", "racecar", "car"]], [["a"]], [["", "b"]],
        [["abc", "abc"]], [["abc", "ab"]], [[""]], [["ab", "abc", "abcd"]],
    ]
    return out


def to_roman(value):
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
             (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = []
    for amount, symbol in table:
        while value >= amount:
            out.append(symbol)
            value -= amount
    return "".join(out)


@cases("roman-to-integer")
def _roman_to_integer():
    numbers = [1, 2, 3, 4, 5, 6, 9, 10, 14, 19, 40, 44, 49, 58, 90, 99, 100, 400, 444, 500,
               900, 999, 1000, 1994, 2023, 3000, 3549, 3888, 3999, 1666, 2748, 1234, 876, 321, 47]
    return [[to_roman(n)] for n in numbers]


@cases("string-to-integer-atoi")
def _atoi():
    return [[s] for s in [
        "42", "   -042", "1337c0d3", "0-1", "words and 987", "-91283472332", "91283472332",
        "", "   ", "+", "-", "+-12", "-+12", "  +0 123", "00000-42a1234", "  0000000000012345678",
        "2147483647", "2147483648", "-2147483648", "-2147483649", "9223372036854775808",
        "-9223372036854775809", "3.14159", "  -3.14", "+1", "-0", "0", "0000", " 1 2", "abc",
        "  +413", "-2147483647", "2147483646", "   +0000000000000000000000001", "  -   234",
    ]]


# -------------------------------------------------------------- linked lists


@cases("add-two-numbers")
def _add_two_numbers():
    out = []
    for i, (a, b) in enumerate([(1, 1), (1, 2), (2, 1), (3, 3), (10, 10), (50, 3), (3, 50),
                                (500, 500), (2000, 1), (1, 2000), (3000, 3000)]):
        out.append([ints(a, 0, 9, 10500 + i), ints(b, 0, 9, 10600 + i)])
    out += [
        [G("repeat", value=9, n=3000), G("repeat", value=9, n=3000)],   # carry the whole way
        [G("repeat", value=9, n=3000), [1]],
        [[1], G("repeat", value=9, n=3000)],
        [G("repeat", value=0, n=3000), G("repeat", value=0, n=3000)],
        [ints(3000, 0, 1, 10620), ints(3000, 8, 9, 10621)],
        [[2, 4, 3], [5, 6, 4]], [[0], [0]], [[9, 9, 9], [1]], [[5], [5]], [[9], [9]], [[1], [9, 9]],
    ]
    return out


@cases("middle-of-the-linked-list")
def _middle_node():
    out = [[ints(n, -1000, 1000, 10700 + i)] for i, n in enumerate([1, 2, 3, 4, 5, 6, 20, 200, 1500, 3000])]
    out += [
        [G("arange", n=3000)], [G("arange", n=2999)], [G("repeat", value=1, n=2500)],
        [G("perm", n=2000)], [ints(1999, 0, 5, 10720)],
        [[1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5, 6]], [[1]], [[1, 2]], [[1, 2, 3]],
    ]
    return out


@cases("remove-nth-node-from-end-of-list")
def _remove_nth_from_end():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 10, 100, 1000, 3000]):
        spec = ints(n, -100, 100, 10800 + i)
        for k in {1, 2, n // 2 or 1, n}:
            out.append([spec, k])
    out += [
        [G("arange", n=3000), 1], [G("arange", n=3000), 3000], [G("arange", n=3000), 1500],
        [[1, 2, 3, 4, 5], 2], [[1], 1], [[1, 2], 1], [[1, 2], 2],
    ]
    return out


@cases("delete-node-in-a-linked-list")
def _delete_node():
    out = []
    for i, n in enumerate([2, 3, 5, 10, 100, 1000, 3000]):
        spec = ints(n, -100, 100, 10900 + i)
        for position in {0, 1, n // 2, n - 2}:
            if 0 <= position < n - 1:
                out.append([spec, position])
    out += [
        [G("arange", n=3000), 0], [G("arange", n=3000), 2998], [G("repeat", value=7, n=2000), 999],
        [[4, 5, 1, 9], 1], [[4, 5, 1, 9], 2], [[1, 2], 0], [[0, 1, 2, 3], 0],
    ]
    return out


@cases("intersection-of-two-linked-lists")
def _intersection_of_two_lists():
    out = []
    for i, (a, b, shared) in enumerate([(0, 0, 1), (1, 1, 1), (2, 3, 3), (10, 5, 2), (100, 100, 100),
                                        (1000, 10, 1000), (10, 1000, 1000), (2500, 2500, 2500),
                                        (5000, 1, 1), (1, 5000, 1)]):
        out.append([ints(a, 0, 99, 11000 + i) if a else [],
                    ints(b, 0, 99, 11100 + i) if b else [],
                    ints(shared, 0, 99, 11200 + i) if shared else []])
    for i, (a, b) in enumerate([(1, 1), (50, 50), (500, 500), (2500, 2500), (5000, 5000)]):
        out.append([ints(a, 0, 99, 11300 + i), ints(b, 0, 99, 11400 + i), []])   # never meet
    out += [
        [G("repeat", value=1, n=2000), G("repeat", value=1, n=2000), G("repeat", value=1, n=2000)],
        [[], [], []], [[4, 1], [5, 6, 1], [8, 4, 5]], [[2, 6, 4], [1, 5], []], [[], [], [1]], [[1], [], [2]],
    ]
    return out


def _cycle_cases(seed0):
    out = []
    for i, n in enumerate([1, 2, 3, 5, 10, 100, 1000, 10000]):
        spec = ints(n, -1000, 1000, seed0 + i)
        out.append([spec, -1])
        out.append([spec, 0])
        out.append([spec, n - 1])
        out.append([spec, n // 2])
    out += [
        [G("arange", n=10000), -1], [G("arange", n=10000), 0], [G("arange", n=10000), 9999],
        [G("arange", n=10000), 5000], [G("repeat", value=1, n=10000), 4999],
        [[3, 2, 0, -4], 1], [[1, 2], -1], [[1], 0], [[1], -1], [[], -1], [[1, 2, 3, 4], 0],
    ]
    return out


@cases("linked-list-cycle")
def _linked_list_cycle():
    return _cycle_cases(11500)


@cases("linked-list-cycle-ii")
def _linked_list_cycle_ii():
    return _cycle_cases(11600)


@cases("palindrome-linked-list")
def _palindrome_linked_list():
    out = [[ints(n, 0, 9, 11700 + i)] for i, n in enumerate([1, 2, 3, 5, 10, 100, 1000, 20000, 100000])]
    out += [[ints(n, 0, 1, 11720 + i)] for i, n in enumerate([4, 40, 400, 4000])]
    for i, n in enumerate([1, 2, 5, 50, 5000, 50000]):
        half = G("arange", n=n, start=0, step=1)
        out.append([G("concat", parts=[half, G("arange", n=n, start=n - 1, step=-1)])])          # even palindrome
        out.append([G("concat", parts=[half, [9], G("arange", n=n, start=n - 1, step=-1)])])     # odd palindrome
    out += [
        [G("repeat", value=7, n=100000)],
        [G("concat", parts=[G("repeat", value=7, n=99999), [8]])],
        [[1, 2, 2, 1]], [[1, 2]], [[1]], [[1, 2, 1]], [[1, 1]], [[1, 2, 3]],
    ]
    return out


@cases("reverse-nodes-in-k-group")
def _reverse_k_group():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 12, 100, 1000, 3000]):
        spec = ints(n, -100, 100, 11800 + i)
        for k in {1, 2, 3, n // 2 or 1, n}:
            out.append([spec, k])
    out += [
        [G("arange", n=3000), 7], [G("arange", n=3000), 3000], [G("arange", n=2999), 1000],
        [[1, 2, 3, 4, 5], 2], [[1, 2, 3, 4, 5], 3], [[1], 1], [[1, 2], 2],
    ]
    return out


@cases("rotate-list")
def _rotate_list():
    out = []
    for i, n in enumerate([0, 1, 2, 3, 7, 50, 500, 3000]):
        spec = ints(n, -100, 100, 11900 + i) if n else []
        for k in {0, 1, n, n + 1 if n else 1, 2 * n + 3, 2000000000}:
            out.append([spec, k])
    out += [
        [[1, 2, 3, 4, 5], 2], [[0, 1, 2], 4], [[], 3], [[1, 2], 0], [[1], 1000000],
    ]
    return out


@cases("reorder-list")
def _reorder_list():
    out = [[ints(n, -100, 100, 12000 + i)] for i, n in enumerate([1, 2, 3, 4, 5, 6, 20, 200, 1500, 3000])]
    out += [
        [G("arange", n=3000)], [G("arange", n=2999)], [G("repeat", value=5, n=2500)],
        [G("perm", n=2000)], [ints(2001, 0, 3, 12020)],
        [[1, 2, 3, 4]], [[1, 2, 3, 4, 5]], [[1]], [[1, 2]], [[1, 2, 3]],
    ]
    return out


def _random_list(n, seed, null_rate=25):
    """[[value, randomIndex], ...] with randomIndex sometimes null."""
    from cases import Rng
    rng = Rng(seed)
    return [[[rng.between(-10 ** 4, 10 ** 4), None if rng.below(100) < null_rate else rng.below(n)]
             for _ in range(n)]]


@cases("copy-list-with-random-pointer")
def _copy_random_list():
    out = [_random_list(n, 12100 + i) for i, n in enumerate([1, 2, 3, 5, 10, 50, 200, 500, 800, 1000])]
    out += [_random_list(n, 12120 + i, null_rate=0) for i, n in enumerate([2, 20, 200, 1000])]
    out += [_random_list(n, 12140 + i, null_rate=100) for i, n in enumerate([1, 10, 100, 1000])]
    out += [
        [[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]],
        [[[1, 1], [2, 1]]], [[]], [[[3, None], [3, 0], [3, None]]], [[[1, 0]]], [[[1, None]]],
    ]
    return out


def _columns(count, per, seed, lo=-1000, hi=1000):
    from cases import Rng
    rng = Rng(seed)
    return [[sorted(rng.between(lo, hi) for _ in range(per)) for _ in range(count)]]


@cases("flatten-a-linked-list")
def _flatten_linked_list():
    out = [_columns(count, per, 12200 + i) for i, (count, per) in enumerate(
        [(1, 1), (1, 10), (2, 1), (3, 3), (10, 5), (30, 10), (100, 10), (200, 10), (30, 100), (300, 10)])]
    out += [_columns(count, per, 12220 + i, lo=0, hi=3) for i, (count, per) in enumerate(
        [(5, 5), (50, 20), (200, 15)])]
    out += [
        [[[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]]],
        [[[1], [2], [3]]], [[[1, 2, 3]]], [[[2, 2], [1, 1]]], [[[1, 1], [1, 1]]],
    ]
    return out


# ------------------------------------------------------------- binary trees

from cases import chain, level_order  # noqa: E402


def tree_cases(seed0, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 600, 2000), null_rate=0, values=(-100, 100),
               chains=(50, 200)):
    """A spread of shapes: dense trees, sparse trees and pure chains."""
    out = [[level_order(n, seed0 + i, null_rate=null_rate, values=values)] for i, n in enumerate(sizes)]
    out += [[level_order(n, seed0 + 50 + i, null_rate=45, values=values)]
            for i, n in enumerate([5, 20, 90, 400, 1200])]
    out += [[chain(n)] for n in chains] + [[chain(n, right=False)] for n in chains]
    out += [[[]], [[1]], [[1, 2]], [[1, None, 2]], [[1, 2, 3]]]
    return out


for _slug, _seed in [("binary-tree-inorder-traversal", 13000), ("binary-tree-preorder-traversal", 13100),
                     ("binary-tree-postorder-traversal", 13200), ("morris-inorder-traversal", 13300)]:
    cases(_slug)(lambda seed=_seed: tree_cases(seed, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 600, 2000, 5000)))

cases("binary-tree-zigzag-level-order-traversal")(lambda: tree_cases(13400, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 600, 1800)))
cases("binary-tree-right-side-view")(lambda: tree_cases(13500, sizes=(0, 1, 2, 3, 7, 15, 30, 60, 90, 100)))
cases("top-view-of-binary-tree")(lambda: tree_cases(13600))
cases("bottom-view-of-binary-tree")(lambda: tree_cases(13700))
cases("vertical-order-traversal-of-a-binary-tree")(
    lambda: tree_cases(13800, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 500, 1000), values=(0, 1000)))
cases("boundary-traversal-of-binary-tree")(
    lambda: [c for c in tree_cases(13900, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000, 5000)) if c[0]])
cases("binary-tree-maximum-path-sum")(
    lambda: [c for c in tree_cases(14000, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 3000, 10000), values=(-1000, 1000)) if c[0]])
cases("diameter-of-binary-tree")(
    lambda: [c for c in tree_cases(14100, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000, 5000), chains=(50, 500)) if c[0]])
cases("balanced-binary-tree")(lambda: tree_cases(14200, sizes=(0, 1, 2, 3, 7, 15, 63, 255, 1023, 2047), chains=(20, 200)))
cases("symmetric-tree")(
    lambda: [c for c in tree_cases(14300, sizes=(1, 3, 7, 15, 31, 63, 127, 255, 511, 1000)) if c[0]])
cases("count-complete-tree-nodes")(
    lambda: [[G("arange", n=n, start=1)] for i, n in enumerate(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 31, 32, 63, 100, 255, 256, 500, 1023, 1024, 2047,
         3000, 5000, 8191, 10000, 16383, 20000, 32767, 50000])] + [[[]], [[1]], [[1, 2]], [[1, 2, 3]]])
cases("flatten-binary-tree-to-linked-list")(lambda: tree_cases(14500, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 600, 1500)))
cases("populating-next-right-pointers-in-each-node")(
    lambda: tree_cases(14600, sizes=(0, 1, 2, 3, 7, 15, 63, 255, 1023, 2000)))
cases("children-sum-property")(
    lambda: tree_cases(14700, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 600, 1500), values=(0, 1000)))
cases("maximum-width-of-binary-tree")(
    lambda: [c for c in tree_cases(14800, sizes=(1, 2, 3, 7, 15, 63, 255, 800, 1500, 3000), chains=(20, 60)) if c[0]])


@cases("same-tree")
def _same_tree():
    out = []
    for i, n in enumerate([0, 1, 2, 3, 7, 15, 40, 100]):
        tree = level_order(n, 14900 + i)
        out.append([tree, tree])                                    # identical
        out.append([tree, level_order(n, 15000 + i)])               # same size, different values
        if tree:
            changed = list(tree)
            changed[-1] = None if changed[-1] is not None else 1
            out.append([tree, changed])                             # one node different
    out += [
        [[1, 2, 3], [1, 2, 3]], [[1, 2], [1, None, 2]], [[], []], [[1, 2, 1], [1, 1, 2]],
        [[1], []], [[], [1]],
    ]
    return out


@cases("subtree-of-another-tree")
def _subtree_of_another_tree():
    out = []
    for i, n in enumerate([1, 2, 3, 7, 15, 60, 200, 800, 2000]):
        tree = level_order(n, 15100 + i)
        out.append([tree, tree])                                    # a tree contains itself
        out.append([tree, [tree[-1]] if tree[-1] is not None else [tree[0]]])
        out.append([tree, level_order(min(n, 100), 15200 + i)])
    out += [
        [[3, 4, 5, 1, 2], [4, 1, 2]],
        [[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]],
        [[1], [1]], [[1, 1], [1]], [[1, 2, 3], [2]], [[1, 2, 3], [4]],
    ]
    return out


@cases("lowest-common-ancestor-of-a-binary-tree")
def _lca_binary_tree():
    out = []
    for i, n in enumerate([2, 3, 7, 15, 63, 255, 1023, 4095, 20000]):
        tree = G("arange", n=n, start=1)                             # distinct values, complete shape
        out.append([tree, 1, n])
        out.append([tree, n, n])
        out.append([tree, n // 2, n])
        out.append([tree, 2, 3] if n >= 3 else [tree, 1, n])
    out += [
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4],
        [[1, 2], 1, 2], [[1, 2, 3, 4, 5], 4, 5], [[1, 2, 3], 2, 3],
    ]
    return out


@cases("root-to-node-path-in-binary-tree")
def _root_to_node_path():
    out = []
    for i, n in enumerate([1, 3, 7, 15, 63, 255, 1023, 4095, 10000]):
        tree = G("arange", n=n, start=1)
        for target in {1, n, n // 2, n // 3 + 1, n + 1}:
            out.append([tree, target])
    out += [
        [[1, 2, 3, 4, 5, 6, 7], 5], [[1, 2, 3], 9], [[1], 1], [[1, 2, 3, 4, 5, 6, 7], 7], [[], 1],
    ]
    return out


@cases("all-nodes-distance-k-in-binary-tree")
def _all_nodes_distance_k():
    out = []
    for i, n in enumerate([1, 3, 7, 15, 31, 63, 127, 255, 500]):
        tree = G("arange", n=n, start=1)
        for k in {0, 1, 2, 3, 10}:
            out.append([tree, n // 2 + 1, k])
        out.append([tree, 1, 2])
    out += [
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2],
        [[1], 1, 3], [[1, 2, 3], 1, 1], [[1, 2, 3], 2, 0], [[1, 2, 3], 2, 2],
    ]
    return out


@cases("minimum-time-to-burn-a-tree")
def _minimum_time_to_burn():
    out = []
    for i, n in enumerate([1, 3, 7, 15, 63, 255, 1023, 4095, 10000]):
        tree = G("arange", n=n, start=1)
        for start in {1, n, n // 2, n // 4 + 1}:
            out.append([tree, start])
    out += [
        [[1, 2, 3, 4, 5, None, 6, None, None, 7, 8], 8], [[1], 1], [[1, 2, 3], 1], [[1, 2, None, 3, None, 4], 4],
    ]
    return out


# ---------------------------------------------------------- binary search trees


def bst_cases(seed0, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000, 5000), values=(-10 ** 5, 10 ** 5)):
    out = [[level_order(n, seed0 + i, sorted_bst=True, values=values)] for i, n in enumerate(sizes)]
    out += [[level_order(n, seed0 + 60 + i, sorted_bst=True, values=(1, 50))]
            for i, n in enumerate([5, 20, 45])]
    out += [[[1]], [[2, 1]], [[1, None, 2]], [[2, 1, 3]]]
    return out


def bst_with_key(seed0, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000), values=(1, 10 ** 5)):
    """Each tree probed with a value below, inside, above and absent from it."""
    out = []
    for i, n in enumerate(sizes):
        tree = level_order(n, seed0 + i, sorted_bst=True, values=values)
        present = [v for v in tree if v is not None]
        low, high = min(present), max(present)
        for key in {low, high, present[len(present) // 2], low - 1, high + 1, (low + high) // 2}:
            out.append([tree, key])
    return out


cases("search-in-a-binary-search-tree")(
    lambda: [[t[0], (lambda vals: vals[len(vals) // 2])([v for v in t[0] if v is not None])]
             for t in bst_cases(16000, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000))]
            + [[t[0], -999999] for t in bst_cases(16050, sizes=(1, 7, 40, 600))]
            + [[[4, 2, 7, 1, 3], 2], [[4, 2, 7, 1, 3], 5], [[1], 1], [[8, 3, 10, 1, 6], 10]])

cases("kth-smallest-element-in-a-bst")(
    lambda: [[t[0], k] for t in bst_cases(16100, sizes=(1, 3, 7, 15, 40, 150, 600, 2000))
             for k in (1, 2, max(1, len([v for v in t[0] if v is not None]) // 2),
                       len([v for v in t[0] if v is not None]))]
            + [[[3, 1, 4, None, 2], 1], [[5, 3, 6, 2, 4, None, None, 1], 3], [[1], 1], [[2, 1, 3], 3]])

cases("inorder-predecessor-and-successor")(lambda: bst_with_key(16200))
cases("floor-and-ceil-in-bst")(lambda: bst_with_key(16300))
cases("largest-bst-in-a-binary-tree")(
    lambda: bst_cases(16400) + tree_cases(16500, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000), values=(-20, 20)))
cases("maximum-sum-bst-in-binary-tree")(
    lambda: bst_cases(16600, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000), values=(-4 * 10 ** 4, 4 * 10 ** 4))
            + tree_cases(16700, sizes=(1, 2, 3, 7, 15, 40, 150, 600, 2000), values=(-40, 40)))
cases("binary-tree-to-doubly-linked-list")(lambda: bst_cases(16800) + tree_cases(16850, sizes=(1, 3, 15, 150, 2000)))


@cases("lowest-common-ancestor-of-a-binary-search-tree")
def _lca_bst():
    out = []
    for i, n in enumerate([2, 3, 7, 15, 60, 250, 1000, 4000]):
        tree = level_order(n, 17000 + i, sorted_bst=True, values=(1, 10 ** 6))
        present = [v for v in tree if v is not None]
        pairs = [(present[0], present[-1]), (present[0], present[0]),
                 (present[len(present) // 2], present[-1]),
                 (present[1 % len(present)], present[2 % len(present)])]
        for p, q in pairs:
            out.append([tree, p, q])
    out += [
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4],
        [[2, 1], 2, 1], [[5, 3, 8, 1, 4], 1, 4],
    ]
    return out


@cases("two-sum-iv-input-is-a-bst")
def _two_sum_bst():
    out = []
    for i, n in enumerate([1, 2, 3, 7, 15, 60, 250, 1000, 4000]):
        tree = level_order(n, 17100 + i, sorted_bst=True, values=(-10 ** 5, 10 ** 5))
        present = [v for v in tree if v is not None]
        out.append([tree, present[0] + present[-1]])                 # reachable
        out.append([tree, 2 * present[0]])                           # needs two distinct nodes
        out.append([tree, 10 ** 9])                                  # impossible
        if len(present) > 3:
            out.append([tree, present[1] + present[2]])
    out += [
        [[5, 3, 6, 2, 4, None, 7], 9], [[5, 3, 6, 2, 4, None, 7], 28], [[2, 1, 3], 4], [[1], 2],
    ]
    return out


@cases("convert-sorted-array-to-binary-search-tree")
def _sorted_array_to_bst():
    out = [[G("sorted", n=n, lo=-10 ** 4, hi=10 ** 4, seed=17200 + i, unique=True, step=3)]
           for i, n in enumerate([1, 2, 3, 4, 5, 8, 16, 40, 150, 600, 1500])]
    out += [[G("arange", n=n, start=-n // 2)] for n in (7, 31, 127, 511, 1500)]
    out += [
        [[-10, -3, 0, 5, 9]], [[1, 3]], [[1]], [[1, 2, 3, 4]], [[1, 2]], [[-1, 0, 1]],
    ]
    return out


@cases("construct-bst-from-preorder-traversal")
def _bst_from_preorder():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 12, 50, 200, 800, 2000]):
        tree = level_order(n, 17300 + i, sorted_bst=True, values=(1, 10 ** 8))
        # Preorder of that BST, produced from the level-order encoding.
        values = [v for v in tree if v is not None]
        root = values[0]
        preorder = []

        def build(subset):
            if not subset:
                return
            head = subset[0]
            preorder.append(head)
            build([v for v in subset[1:] if v < head])
            build([v for v in subset[1:] if v > head])

        build(values if values[0] == root else values)
        out.append([preorder])
    out += [[G("arange", n=n, start=1)] for n in (5, 50, 500)]        # a right chain
    out += [
        [[8, 5, 1, 7, 10, 12]], [[1, 3]], [[4, 2]], [[1]], [[5, 3, 1, 4, 8]],
    ]
    return out


@cases("binary-search-tree-iterator")
def _bst_iterator():
    out = []
    for i, n in enumerate([1, 2, 3, 7, 15, 60, 250, 1000, 5000]):
        tree = level_order(n, 17400 + i, sorted_bst=True, values=(-10 ** 5, 10 ** 5))
        count = len([v for v in tree if v is not None])
        ops = ["BSTIterator"]
        args = [[tree]]
        for step in range(min(count, 40)):
            ops.append("next")
            args.append([])
            if step % 3 == 0:
                ops.append("hasNext")
                args.append([])
        ops.append("hasNext")
        args.append([])
        out.append([ops, args])
        # Drain the whole iterator, so hasNext ends false.
        drain_ops = ["BSTIterator"] + ["next", "hasNext"] * count
        drain_args = [[tree]] + [[]] * (2 * count)
        if count <= 300:
            out.append([drain_ops, drain_args])
    out += [
        [["BSTIterator", "next", "next", "hasNext", "next", "hasNext"],
         [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], []]],
        [["BSTIterator", "hasNext", "next", "hasNext"], [[[1]], [], [], []]],
        [["BSTIterator", "next", "next", "next"], [[[2, 1, 3]], [], [], []]],
    ]
    return out


def _traversals(tree):
    """(preorder, inorder, postorder) of a level-order encoded tree."""
    values = tree
    if not values:
        return [], [], []

    # Rebuild the tree from the level-order encoding, then walk it three ways.
    root = {"val": values[0], "left": None, "right": None}
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
                node["left"] = {"val": v, "left": None, "right": None}
                queue.append(node["left"])
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node["right"] = {"val": v, "left": None, "right": None}
                queue.append(node["right"])

    pre, ino, post = [], [], []

    def walk(node):
        if node is None:
            return
        pre.append(node["val"])
        walk(node["left"])
        ino.append(node["val"])
        walk(node["right"])
        post.append(node["val"])

    walk(root)
    return pre, ino, post


def _construction_cases(seed0, order):
    out = []
    for i, n in enumerate([1, 2, 3, 7, 15, 60, 250, 1000, 3000]):
        tree = level_order(n, seed0 + i, values=(-3000, 3000))
        values = [v for v in tree if v is not None]
        if len(set(values)) != len(values):
            # The problems promise distinct values; relabel while keeping the shape.
            it = iter(range(1, len(values) + 1))
            tree = [None if v is None else next(it) for v in tree]
        pre, ino, post = _traversals(tree)
        out.append([pre, ino] if order == "pre" else [ino, post])
    for n in (5, 50, 400):
        tree = chain(n)
        pre, ino, post = _traversals(tree)
        out.append([pre, ino] if order == "pre" else [ino, post])
        tree = chain(n, right=False)
        pre, ino, post = _traversals(tree)
        out.append([pre, ino] if order == "pre" else [ino, post])
    return out


cases("construct-binary-tree-from-preorder-and-inorder-traversal")(
    lambda: _construction_cases(17500, "pre") + [
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], [[-1], [-1]], [[1, 2], [2, 1]], [[1, 2], [1, 2]]])

cases("construct-binary-tree-from-inorder-and-postorder-traversal")(
    lambda: _construction_cases(17600, "post") + [
        [[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]], [[-1], [-1]], [[2, 1], [2, 1]], [[1, 2], [2, 1]]])

cases("serialize-and-deserialize-binary-tree")(
    lambda: tree_cases(17700, sizes=(0, 1, 2, 3, 7, 15, 40, 150, 600, 2000), values=(-1000, 1000)))


# ------------------------------------- bit tricks, binary search and greedy


@cases("sum-of-two-integers")
def _sum_of_two_integers():
    out = [[a, b] for a in (-1000, -37, -1, 0, 1, 37, 1000) for b in (-1000, -1, 0, 1, 1000)]
    return out + [[1, 2], [2, 3], [-1, 1], [-5, -7], [999, 1]]


@cases("number-of-1-bits")
def _hamming_weight():
    return [[n] for n in [0, 1, 2, 3, 7, 8, 11, 15, 16, 31, 128, 255, 256, 1023, 1024, 65535,
                          65536, 1048575, 16777215, 2147483647, 2147483648, 3221225471,
                          4294967293, 4294967295, 4042322160, 2863311530, 1431655765,
                          305419896, 4008636142, 100, 1000, 12345, 999983, 87654321]]


@cases("counting-bits")
def _counting_bits():
    return [[n] for n in [0, 1, 2, 3, 4, 5, 7, 8, 15, 16, 31, 32, 63, 64, 100, 127, 128, 255,
                          256, 511, 512, 1000, 1023, 1024, 2047, 4095, 5000, 8191, 9999]]


@cases("reverse-bits")
def _reverse_bits():
    return [[n] for n in [0, 1, 2, 3, 43261596, 4294967293, 4294967295, 2147483648, 1073741824,
                          65535, 65536, 4042322160, 2863311530, 1431655765, 305419896,
                          16777215, 255, 256, 1023, 1024, 999999937, 123456789, 987654321,
                          2, 4, 8, 16, 32, 64, 128, 2147483647]]


@cases("missing-number")
def _missing_number():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 20, 200, 2000, 20000, 100000]):
        base = G("perm", n=n + 1, seed=18000 + i)
        missing = expand(base)[i % (n + 1)]
        out.append([G("without", of=base, value=missing)])
    for i, n in enumerate([10, 1000, 100000]):
        out.append([G("arange", n=n)])                                     # n itself is missing
        out.append([G("arange", n=n, start=1)])                            # 0 is missing
    out += [[[3, 0, 1]], [[0, 1]], [[9, 6, 4, 2, 3, 5, 7, 0, 1]], [[0]], [[1]]]
    return out


@cases("powx-n")
def _pow_x_n():
    out = [[x, n] for x in (2.0, 0.5, 1.0, -2.0, 1.0001) for n in (0, 1, 2, 10, -2, 31)]
    out += [[2.0, 10], [2.1, 3], [2.0, -2], [1.0, 2147483647], [-1.0, 2147483647],
            [-1.0, -2147483648], [0.99999, 100000], [3.0, 20], [1.5, -10]]
    return out


@cases("nth-root-of-a-number")
def _nth_root():
    out = []
    for n in (1, 2, 3, 4, 5, 10, 20, 30):
        for base in (1, 2, 3, 7, 10):
            value = base ** n
            if value <= 10 ** 9:
                out.append([n, value])
                out.append([n, value + 1])
    out += [[3, 27], [4, 69], [2, 100], [1, 7], [2, 999999937], [30, 1], [2, 1000000000]]
    return out


@cases("single-element-in-a-sorted-array")
def _single_non_duplicate():
    out = []
    for i, pairs in enumerate([0, 1, 2, 5, 20, 200, 2000, 20000, 49999]):
        base = G("sorted", n=pairs, lo=0, hi=10 ** 5, seed=18100 + i, unique=True) if pairs else []
        values = expand(base) if pairs else []
        # The lone value is placed below, inside and above the doubled range.
        singles = {values[0] - 1, values[len(values) // 2] + 0, values[-1] + 1} if values else {0}
        for single in singles:
            doubled = G("duplicate", of=G("without", of=base, value=single)) if pairs else []
            out.append([G("sortof", of=G("concat", parts=[doubled, [single]]))])
    out += [[[1, 1, 2, 3, 3, 4, 4, 8, 8]], [[3, 3, 7, 7, 10, 11, 11]], [[1]], [[1, 1, 2]], [[1, 2, 2]]]
    return out


@cases("kth-element-of-two-sorted-arrays")
def _kth_element_two_arrays():
    out = []
    for i, (m, n) in enumerate([(0, 1), (1, 0), (1, 1), (3, 4), (10, 10), (100, 5), (5, 100),
                                (1000, 1000), (50000, 1), (100000, 100000)]):
        a = G("sorted", n=m, lo=-10 ** 9, hi=10 ** 9, seed=18200 + i) if m else []
        b = G("sorted", n=n, lo=-10 ** 9, hi=10 ** 9, seed=18300 + i) if n else []
        total = m + n
        for k in {1, 2, total // 2 or 1, total}:
            out.append([a, b, k])
    out += [
        [[2, 3, 6, 7, 9], [1, 4, 8, 10], 5],
        [[100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7],
        [[], [1, 2, 3], 2], [[1], [2], 2], [[1, 1, 1], [1, 1], 3],
    ]
    return out


@cases("allocate-minimum-pages")
def _allocate_pages():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 40000, 100000]):
        spec = ints(n, 1, 10 ** 4, 18400 + i)
        for students in {1, 2, n // 2 or 1, n, n + 1}:
            out.append([spec, students])
    out += [
        [G("repeat", value=100, n=100000), 7],
        [G("arange", n=100000, start=1), 5],
        [[12, 34, 67, 90], 2], [[15, 17, 20], 2], [[10, 20], 3], [[5], 1],
    ]
    return out


@cases("aggressive-cows")
def _aggressive_cows():
    out = []
    for i, n in enumerate([2, 3, 5, 20, 200, 2000, 20000, 100000]):
        spec = G("sorted", n=n, lo=0, hi=10 ** 9, seed=18500 + i, unique=True, step=17)
        for cows in {2, 3, n // 2 or 2, n}:
            if cows <= n:
                out.append([spec, cows])
    out += [
        [G("arange", n=100000), 50000],
        [G("arange", n=100000, start=0, step=1000), 2],
        [[1, 2, 4, 8, 9], 3], [[10, 1, 2, 7, 5], 3], [[1, 2], 2], [[0, 3, 4, 7, 10, 9], 4],
    ]
    return out


@cases("matrix-median")
def _matrix_median():
    out = []
    for i, (rows, cols) in enumerate([(1, 1), (1, 3), (3, 1), (3, 3), (5, 5), (9, 11), (21, 21),
                                      (51, 51), (101, 101), (299, 299), (1, 299), (299, 1)]):
        out.append([G("sortedgrid", rows=rows, cols=cols, start=1, step=1, seed=18600 + i)])
    out += [
        [[[1, 3, 5], [2, 6, 9], [3, 6, 9]]],
        [[[1, 5, 7, 9, 11], [1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]],
        [[[1]]], [[[1, 2, 3]]], [[[1], [2], [3]]], [[[5, 5, 5], [5, 5, 5], [5, 5, 5]]],
    ]
    return out


def _meeting_lists(n, seed, hi=10 ** 9, span=1000):
    """[starts, ends] where ends are starts plus a generated duration."""
    starts = ints(n, 0, hi, seed)
    return [starts, G("zipsum", parts=[starts, ints(n, 1, span, seed + 7)])]


@cases("n-meetings-in-one-room")
def _n_meetings():
    out = [_meeting_lists(n, 18700 + i) for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 40000, 100000])]
    out += [_meeting_lists(n, 18720 + i, hi=100, span=10) for i, n in enumerate([50, 5000, 100000])]
    out += [
        [G("arange", n=50000), G("arange", n=50000, start=1)],
        [G("repeat", value=1, n=50000), G("repeat", value=2, n=50000)],
        [[1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]], [[10, 12, 20], [20, 25, 30]], [[1], [2]],
        [[1, 2, 3], [2, 3, 4]],
    ]
    return out


@cases("minimum-platforms")
def _minimum_platforms():
    out = [_meeting_lists(n, 18800 + i) for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 40000, 100000])]
    out += [_meeting_lists(n, 18820 + i, hi=1000, span=500) for i, n in enumerate([100, 10000, 100000])]
    out += [
        [G("repeat", value=1, n=50000), G("repeat", value=2, n=50000)],
        [G("arange", n=50000), G("arange", n=50000, start=1)],
        [[900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]],
        [[900, 1100, 1235], [1000, 1200, 1240]], [[1], [2]], [[1, 1, 1], [2, 2, 2]],
    ]
    return out


@cases("job-sequencing-problem")
def _job_sequencing():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 40000, 100000]):
        out.append([ints(n, 1, max(1, n), 18900 + i), ints(n, 1, 10 ** 4, 19000 + i)])
    out += [
        [G("repeat", value=1, n=50000), ints(50000, 1, 10 ** 4, 19020)],
        [G("arange", n=50000, start=1), G("repeat", value=100, n=50000)],
        [[4, 1, 1, 1], [20, 10, 40, 30]], [[2, 1, 2, 1, 1], [100, 19, 27, 25, 15]],
        [[1], [5]], [[1, 1], [5, 7]],
    ]
    return out


@cases("fractional-knapsack")
def _fractional_knapsack():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 40000, 100000]):
        weights = ints(n, 1, 10 ** 4, 19100 + i)
        values = ints(n, 1, 10 ** 4, 19200 + i)
        for capacity in {1, 1000, 10 ** 6, 10 ** 9}:
            out.append([weights, values, capacity])
    out += [
        [[10, 20, 30], [60, 100, 120], 50], [[10], [60], 5], [[1, 1], [10, 20], 1],
        [[4, 5], [10, 20], 100],
    ]
    return out


@cases("assign-cookies")
def _assign_cookies():
    out = []
    for i, (a, b) in enumerate([(1, 1), (1, 5), (5, 1), (10, 10), (100, 50), (1000, 1000),
                                (10000, 10000), (50000, 50000), (50000, 1)]):
        out.append([ints(a, 1, 1000, 19300 + i), ints(b, 1, 1000, 19400 + i)])
    out += [
        [G("repeat", value=1, n=50000), G("repeat", value=1, n=50000)],
        [G("arange", n=50000, start=1), G("arange", n=50000, start=1)],
        [G("repeat", value=2 ** 31 - 1, n=1000), G("repeat", value=1, n=1000)],
        [[1, 2, 3], [1, 1]], [[1, 2], [1, 2, 3]], [[10], [1]], [[1, 1, 1], [1, 1]],
    ]
    return out


@cases("minimum-coins")
def _minimum_coins():
    return [[n] for n in [0, 1, 2, 3, 4, 5, 7, 9, 11, 19, 21, 49, 70, 99, 121, 199, 200, 499,
                          500, 999, 2000, 2001, 3999, 4321, 9999, 12345, 99999, 123456,
                          1000000, 999999999, 1000000000, 87, 543, 6789]]


def _interval_cases(seed0, allow_empty=True):
    out = [[G("intervals", n=n, lo=0, hi=hi, maxLen=span, seed=seed0 + i)]
           for i, (n, hi, span) in enumerate([(1, 10, 3), (2, 10, 3), (5, 30, 5), (20, 60, 6),
                                              (100, 300, 8), (800, 2000, 10), (3000, 10 ** 4, 12),
                                              (10000, 10 ** 6, 15), (10000, 50, 5)])]
    out += [[G("disjoint", n=n, gap=2, maxLen=1, seed=seed0 + 40 + i)] for i, n in enumerate([5, 500, 10000])]
    out += [
        [G("repeat", value=[1, 2], n=5000)],
        [[[0, 30], [5, 10], [15, 20]]], [[[7, 10], [2, 4]]], [[[1, 2]]], [[[1, 5], [2, 6], [3, 7]]],
        [[[1, 2], [2, 3]]],
    ]
    if allow_empty:
        out.append([[]])
    return out


cases("meeting-rooms")(lambda: _interval_cases(19500))
cases("meeting-rooms-ii")(lambda: _interval_cases(19600, allow_empty=False))


# ------------------------------------------------------- dynamic programming


@cases("longest-common-subsequence")
def _lcs():
    out = []
    for i, (a, b, alphabet) in enumerate([(1, 1, "ab"), (2, 3, "ab"), (5, 5, "abc"), (20, 25, "abc"),
                                          (100, 100, "abcde"), (400, 300, "abc"), (1000, 1000, "ab"),
                                          (1000, 1000, LOWER), (1000, 50, "abc"), (50, 1000, "abc")]):
        out.append([text(a, 20000 + i, alphabet), text(b, 20100 + i, alphabet)])
    for i, n in enumerate([10, 100, 1000]):
        same = text(n, 20200 + i)
        out.append([same, same])
        out.append([same, G("shuffle", of=same, seed=20300 + i)])
    out += [
        [G("strrepeat", value="a", n=1000), G("strrepeat", value="a", n=1000)],
        [G("strrepeat", value="a", n=1000), G("strrepeat", value="b", n=1000)],
        [G("strrepeat", value="ab", n=500), G("strrepeat", value="ba", n=500)],
        ["abcde", "ace"], ["abc", "abc"], ["abc", "def"], ["a", "a"], ["a", "b"],
    ]
    return out


@cases("0-1-knapsack")
def _knapsack():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 120, 400, 1000]):
        weights = ints(n, 1, 1000, 20400 + i)
        values = ints(n, 1, 1000, 20500 + i)
        for capacity in {1, 10, 100, 1000}:
            out.append([weights, values, capacity])
    out += [
        [G("repeat", value=1, n=1000), G("repeat", value=1, n=1000), 1000],
        [G("repeat", value=1000, n=1000), ints(1000, 1, 1000, 20520), 999],
        [[1, 3, 4, 5], [1, 4, 5, 7], 7], [[4, 5, 1], [1, 2, 3], 4], [[10], [100], 5], [[1, 1], [5, 6], 2],
    ]
    return out


@cases("subset-sum-equal-to-target")
def _subset_sum():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 80, 150, 200]):
        spec = ints(n, 0, 1000, 20600 + i)
        values = expand(spec)
        for target in {0, 1, sum(values[:max(1, n // 2)]), 10 ** 4, sum(values) // 2}:
            if target <= 10 ** 4:
                out.append([spec, target])
    out += [
        [G("repeat", value=1, n=200), 200], [G("repeat", value=1, n=200), 201],
        [G("repeat", value=0, n=200), 0], [G("arange", n=200, start=1), 10 ** 4],
        [[3, 34, 4, 12, 5, 2], 9], [[3, 34, 4, 12, 5, 2], 30], [[1], 0], [[2, 3], 5],
    ]
    return out


@cases("count-subsets-with-given-sum")
def _count_subsets():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 20, 60, 120, 200]):
        spec = ints(n, 0, 60, 20700 + i)
        values = expand(spec)
        for target in {0, 1, sum(values) // 2, sum(values), 10 ** 4}:
            if target <= 10 ** 4:
                out.append([spec, target])
    out += [
        [G("repeat", value=1, n=60), 30], [G("repeat", value=0, n=20), 0],
        [[1, 2, 3, 3], 6], [[1, 1, 1, 1], 1], [[0, 0, 1], 1], [[2], 3],
    ]
    return out


@cases("minimum-sum-partition")
def _minimum_sum_partition():
    out = [[ints(n, 0, 500, 20800 + i)] for i, n in enumerate([1, 2, 3, 8, 25, 60, 120, 200])]
    out += [
        [G("repeat", value=500, n=200)], [G("repeat", value=500, n=199)], [G("repeat", value=0, n=200)],
        [G("arange", n=200, start=1)], [ints(200, 0, 1, 20820)], [ints(200, 499, 500, 20821)],
        [[1, 6, 11, 5]], [[1, 4]], [[1]], [[2, 2]], [[1, 2, 3]],
    ]
    return out


@cases("rod-cutting")
def _rod_cutting():
    out = [[ints(n, 1, 10 ** 5, 20900 + i)] for i, n in enumerate([1, 2, 3, 8, 25, 100, 400, 1000])]
    out += [
        [G("arange", n=1000, start=1)], [G("arange", n=1000, start=1000, step=-1)],
        [G("repeat", value=7, n=1000)], [ints(1000, 1, 10, 20920)],
        [[1, 5, 8, 9, 10, 17, 17, 20]], [[3, 5, 8, 9, 10, 17, 17, 20]], [[1]], [[2, 3]],
    ]
    return out


@cases("egg-dropping")
def _egg_drop():
    out = [[eggs, floors] for eggs in (1, 2, 3, 5, 10, 50, 100) for floors in (1, 2, 10, 100, 10000)]
    return out + [[1, 2], [2, 10], [2, 100], [3, 14], [100, 10000], [1, 10000]]


@cases("matrix-chain-multiplication")
def _matrix_chain():
    out = [[ints(n, 1, 500, 21000 + i)] for i, n in enumerate([2, 3, 4, 6, 12, 30, 80, 150, 200])]
    out += [
        [G("repeat", value=100, n=200)], [G("arange", n=200, start=1)],
        [G("arange", n=200, start=200, step=-1)], [ints(200, 1, 5, 21020)],
        [[40, 20, 30, 10, 30]], [[10, 20, 30]], [[1, 2]], [[10, 20, 30, 40]],
    ]
    return out


@cases("palindrome-partitioning-ii")
def _min_cut():
    out = [[text(n, 21100 + i, "ab")] for i, n in enumerate([1, 2, 3, 8, 30, 120, 500, 1200, 2000])]
    out += [[text(n, 21120 + i, LOWER)] for i, n in enumerate([50, 500, 2000])]
    out += [
        [G("strrepeat", value="a", n=2000)],
        [G("strrepeat", value="ab", n=1000)],
        [G("concat", parts=[G("strrepeat", value="a", n=1000), G("strrepeat", value="b", n=1000)])],
        ["aab"], ["a"], ["ab"], ["abccba"], ["aabbaa"],
    ]
    return out


@cases("maximum-sum-increasing-subsequence")
def _max_sum_is():
    out = [[ints(n, 1, 10 ** 5, 21200 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 120, 500, 1200, 2000])]
    out += [
        [G("arange", n=2000, start=1)], [G("arange", n=2000, start=2000, step=-1)],
        [G("repeat", value=5, n=2000)], [G("perm", n=2000, base=1)], [ints(2000, 1, 10, 21220)],
        [[1, 101, 2, 3, 100]], [[4, 1, 2, 3]], [[10]], [[5, 4, 3]],
    ]
    return out


@cases("maximum-profit-in-job-scheduling")
def _max_profit_job_scheduling():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 40, 400, 4000, 20000, 50000]):
        starts = ints(n, 1, 10 ** 9 - 1000, 21300 + i)
        ends = G("zipsum", parts=[starts, ints(n, 1, 1000, 21350 + i)])
        out.append([starts, ends, ints(n, 1, 10 ** 4, 21400 + i)])
    for i, n in enumerate([1000, 20000]):
        out.append([G("arange", n=n, start=1), G("arange", n=n, start=2),
                    G("repeat", value=10 ** 4, n=n)])                               # nothing overlaps
        out.append([G("repeat", value=1, n=n), G("repeat", value=10 ** 9, n=n),
                    ints(n, 1, 10 ** 4, 21420 + i)])                                # everything overlaps
    out += [
        [[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]],
        [[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]],
        [[1, 1, 1], [2, 3, 4], [5, 6, 4]], [[1], [2], [5]],
    ]
    return out


@cases("house-robber-ii")
def _house_robber_ii():
    out = [[ints(n, 0, 1000, 21500 + i)] for i, n in enumerate([1, 2, 3, 4, 5, 10, 30, 60, 100])]
    out += [
        [G("repeat", value=1000, n=100)], [G("repeat", value=0, n=100)],
        [G("arange", n=100)], [G("arange", n=100, start=100, step=-1)],
        [ints(100, 0, 1, 21520)], [ints(100, 995, 1000, 21521)],
        [[2, 3, 2]], [[1, 2, 3, 1]], [[1]], [[1, 2, 3]], [[2, 1]], [[1, 2]],
    ]
    return out


@cases("decode-ways")
def _decode_ways():
    out = [[text(n, 21600 + i, "0123456789")] for i, n in enumerate([1, 2, 3, 5, 10, 30, 60, 100])]
    out += [[text(n, 21620 + i, "12")] for i, n in enumerate([5, 20, 60, 100])]
    out += [[text(n, 21640 + i, "126")] for i, n in enumerate([10, 50, 100])]
    out += [
        [G("strrepeat", value="1", n=100)], [G("strrepeat", value="2", n=100)],
        [G("strrepeat", value="10", n=50)], [G("strrepeat", value="27", n=50)],
        [G("concat", parts=[G("strrepeat", value="1", n=99), "0"])],
        ["12"], ["226"], ["06"], ["10"], ["0"], ["100"], ["2101"], ["27"],
    ]
    return out


@cases("jump-game")
def _jump_game():
    out = [[ints(n, 0, 5, 21700 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 120, 1000, 10000])]
    out += [
        [G("repeat", value=1, n=10000)], [G("repeat", value=0, n=10000)],
        [G("concat", parts=[G("repeat", value=1, n=9998), [0, 0]])],
        [G("concat", parts=[[10 ** 5], G("repeat", value=0, n=9999)])],
        [G("arange", n=10000, start=10000, step=-1)], [ints(10000, 0, 1, 21720)],
        [[2, 3, 1, 1, 4]], [[3, 2, 1, 0, 4]], [[0]], [[1, 0, 1]], [[2, 0, 0]],
    ]
    return out


@cases("combination-sum-iv")
def _combination_sum_iv():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 10, 40, 100, 200]):
        spec = G("sorted", n=n, lo=1, hi=1000, seed=21800 + i, unique=True)
        for target in {1, 10, 100, 1000}:
            out.append([spec, target])
    out += [
        [[1], 1000], [[1, 2], 1000], [[1, 2, 3], 4], [[9], 3], [[1], 5], [[2, 3], 6],
        [G("arange", n=200, start=1), 1000],
    ]
    return out


@cases("palindromic-substrings")
def _palindromic_substrings():
    out = [[text(n, 21900 + i, "ab")] for i, n in enumerate([1, 2, 3, 8, 30, 120, 500, 1000])]
    out += [[text(n, 21920 + i, LOWER)] for i, n in enumerate([50, 500, 1000])]
    out += [
        [G("strrepeat", value="a", n=1000)], [G("strrepeat", value="ab", n=500)],
        [G("strrepeat", value="aab", n=333)],
        [G("concat", parts=[G("strrepeat", value="a", n=500), G("strrepeat", value="b", n=500)])],
        ["abc"], ["aaa"], ["a"], ["abba"], ["aba"],
    ]
    return out


@cases("longest-repeating-character-replacement")
def _character_replacement():
    out = []
    for i, (n, alphabet) in enumerate([(1, "AB"), (2, "AB"), (5, "AB"), (20, "ABC"), (100, "ABCD"),
                                       (1000, "ABCDE"), (10000, "ABCDEFGHIJ"), (100000, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                                       (100000, "AB")]):
        spec = text(n, 22000 + i, alphabet)
        for k in {0, 1, n // 10, n}:
            out.append([spec, k])
    out += [
        [G("strrepeat", value="A", n=100000), 0],
        [G("strrepeat", value="AB", n=50000), 1],
        ["ABAB", 2], ["AABABBA", 1], ["A", 0], ["ABBB", 0],
    ]
    return out


@cases("word-break-ii")
def _word_break_ii():
    dictionaries = [
        ["cat", "cats", "and", "sand", "dog"],
        ["a", "aa", "aaa", "aaaa"],
        ["apple", "pen", "applepen", "pine", "pineapple"],
        ["ab", "abc", "b", "c", "bc", "a"],
    ]
    out = []
    for i, words in enumerate(dictionaries):
        for n in (1, 3, 6, 10, 14, 18, 20):
            out.append([text(n, 22100 + i * 10 + n, "abc"), words])
    out += [
        [G("strrepeat", value="a", n=20), ["a", "aa", "aaa"]],
        [G("strrepeat", value="a", n=20), ["a"]],
        [G("concat", parts=[G("strrepeat", value="a", n=19), "b"]), ["a", "aa", "aaa", "aaaa"]],
        ["catsanddog", ["cat", "cats", "and", "sand", "dog"]],
        ["pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]],
        ["catsandog", ["cats", "dog", "sand", "and", "cat"]], ["a", ["a"]], ["ab", ["a", "b", "ab"]],
    ]
    return out


@cases("minimum-characters-for-palindrome")
def _min_chars_for_palindrome():
    out = [[text(n, 22200 + i, "ab")] for i, n in enumerate([1, 2, 3, 8, 30, 120, 1000, 10000, 100000])]
    out += [[text(n, 22220 + i, LOWER)] for i, n in enumerate([50, 500, 50000])]
    out += [
        [G("strrepeat", value="a", n=100000)],
        [G("strrepeat", value="ab", n=50000)],
        [G("concat", parts=[G("strrepeat", value="a", n=50000), G("strrepeat", value="b", n=50000)])],
        [G("concat", parts=[G("strrepeat", value="ab", n=25000), G("strrepeat", value="ba", n=25000)])],
        ["aacecaaa"], ["abcd"], ["a"], ["aabb"], ["aba"],
    ]
    return out


@cases("count-and-say")
def _count_and_say():
    return [[n] for n in range(1, 31)]


# ------------------------------------------------------------------- graphs


def _adjacency(n, edge_count, seed, directed=False):
    """A generator spec — expanding it here would inline megabytes of JSON."""
    return G("adj", n=edge_count, nodes=n, seed=seed, directed=directed)


def _edge_cases(seed0, dag=False):
    out = []
    for i, (n, count) in enumerate([(1, 0), (2, 1), (3, 3), (8, 10), (40, 60), (300, 500),
                                    (2000, 4000), (20000, 40000), (50000, 100000)]):
        out.append([n, G("edges", n=count, nodes=n, seed=seed0 + i)])
        out.append([n, G("edges", n=count, nodes=n, seed=seed0 + 50 + i, dag=True)])
    out += [
        [1000, []],                                                      # no edges at all
        [1000, G("edges", n=999, nodes=1000, seed=seed0 + 90, dag=True)],
        [10, G("edges", n=45, nodes=10, seed=seed0 + 91)],               # dense
    ]
    return out


@cases("clone-graph")
def _clone_graph():
    out = []
    for i, (n, count) in enumerate([(1, 0), (2, 1), (4, 4), (8, 10), (15, 20), (25, 35),
                                    (40, 60), (60, 80), (80, 100), (100, 120), (100, 99),
                                    (50, 60), (30, 40), (12, 15)]):
        adj = expand(_adjacency(n, count, 23000 + i))
        # LeetCode's clone-graph has no self-loops or repeated edges, and is connected.
        cleaned = []
        for node, neighbours in enumerate(adj):
            unique = sorted({v + 1 for v in neighbours if v != node})
            cleaned.append(unique)
        for node in range(n - 1):                                        # keep it connected
            if node + 2 not in cleaned[node]:
                cleaned[node].append(node + 2)
                cleaned[node + 1].append(node + 1)
        out.append([[sorted(set(row)) for row in cleaned]])
    out += [
        [[[2, 4], [1, 3], [2, 4], [1, 3]]], [[[]]], [[]], [[[2], [1]]],
        [[[2, 3], [1, 3], [1, 2]]],
    ]
    return out


cases("bfs-of-graph")(lambda: [[_adjacency(n, count, 23100 + i)]
                               for i, (n, count) in enumerate(
                                   [(1, 0), (2, 1), (4, 4), (10, 20), (60, 100), (400, 800),
                                    (3000, 6000), (10000, 20000), (10000, 9999), (500, 0)])]
                              + [[[[1, 2], [0, 3], [0], [1]]], [[[], []]], [[[]]], [[[2], [], [0]]]])

cases("dfs-of-graph")(lambda: [[_adjacency(n, count, 23200 + i)]
                               for i, (n, count) in enumerate(
                                   [(1, 0), (2, 1), (4, 4), (10, 20), (60, 100), (400, 800),
                                    (3000, 6000), (9000, 18000), (9000, 8999), (500, 0)])]
                              + [[[[1, 2], [0, 3], [0], [1]]], [[[], []]], [[[]]], [[[2], [], [0]]]])

cases("detect-cycle-in-undirected-graph")(lambda: _edge_cases(23300))
cases("detect-cycle-in-directed-graph")(lambda: _edge_cases(23400))
cases("topological-sort")(lambda: _edge_cases(23500))
cases("is-graph-bipartite")(lambda: _edge_cases(23600))
cases("number-of-connected-components-in-an-undirected-graph")(lambda: _edge_cases(23700))
cases("graph-valid-tree")(
    lambda: _edge_cases(23800) + [
        [n, [[i, i + 1] for i in range(n - 1)]] for n in (2, 10, 100, 1000)])
cases("strongly-connected-components")(lambda: _edge_cases(23900))


@cases("flood-fill")
def _flood_fill():
    out = []
    for i, (rows, cols, hi) in enumerate([(1, 1, 1), (1, 6, 2), (6, 1, 2), (3, 3, 2), (10, 10, 3),
                                          (30, 30, 4), (60, 60, 2), (100, 100, 5), (100, 100, 1)]):
        grid = G("grid", rows=rows, cols=cols, lo=0, hi=hi, seed=24000 + i)
        out.append([grid, 0, 0, 9])
        out.append([grid, rows // 2, cols // 2, 0])
    out += [
        [G("grid", rows=100, cols=100, lo=1, hi=1, seed=24020), 50, 50, 2],
        [G("grid", rows=100, cols=100, lo=1, hi=1, seed=24021), 0, 0, 1],
        [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2], [[[0, 0], [0, 0]], 0, 0, 0],
        [[[1]], 0, 0, 2], [[[1, 2], [2, 1]], 0, 0, 3],
    ]
    return out


@cases("rotting-oranges")
def _rotting_oranges():
    out = [[G("grid", rows=r, cols=c, lo=0, hi=2, seed=24100 + i)]
           for i, (r, c) in enumerate([(1, 1), (1, 8), (8, 1), (3, 3), (12, 12), (40, 40),
                                       (100, 100), (200, 200), (300, 300), (7, 297)])]
    out += [
        [G("grid", rows=100, cols=100, lo=1, hi=1, seed=24120)],          # all fresh: -1
        [G("grid", rows=100, cols=100, lo=2, hi=2, seed=24121)],          # all rotten: 0
        [G("grid", rows=100, cols=100, lo=0, hi=0, seed=24122)],          # empty grid
        [G("grid", rows=300, cols=300, lo=0, hi=1, seed=24123)],
        [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]],
        [[[0, 2]]], [[[1]]],
    ]
    return out


@cases("pacific-atlantic-water-flow")
def _pacific_atlantic():
    out = [[G("grid", rows=r, cols=c, lo=0, hi=hi, seed=24200 + i)]
           for i, (r, c, hi) in enumerate([(1, 1, 1), (1, 6, 5), (6, 1, 5), (3, 3, 3), (10, 10, 8),
                                           (25, 25, 20), (60, 60, 50), (120, 120, 10 ** 5),
                                           (200, 200, 10 ** 5), (200, 30, 4)])]
    out += [
        [G("grid", rows=60, cols=60, lo=7, hi=7, seed=24220)],            # flat: every cell qualifies
        [G("grid", rows=60, cols=60, lo=0, hi=1, seed=24221)],
        [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]],
        [[[1]]], [[[1, 1], [1, 1]]], [[[3, 3, 3], [3, 1, 3], [3, 3, 3]]],
    ]
    return out


def _alien_words(order, count, seed, max_len=6):
    """Words sorted by `order`, so the alphabet is recoverable from them."""
    from cases import Rng
    rng = Rng(seed)
    rank = {ch: i for i, ch in enumerate(order)}
    words = []
    for _ in range(count):
        length = rng.between(1, max_len)
        words.append("".join(order[rng.below(len(order))] for _ in range(length)))
    words.sort(key=lambda w: [rank[c] for c in w])
    return [words]


@cases("alien-dictionary")
def _alien_dictionary():
    alphabets = ["abc", "cba", "bac", "zyx", "abcdef", "fedcba", "qwerty", LOWER, LOWER[::-1]]
    out = [_alien_words(order, count, 24300 + i)
           for i, (order, count) in enumerate(zip(alphabets, [5, 8, 12, 20, 40, 60, 80, 100, 100]))]
    out += [_alien_words(order, 100, 24320 + i, max_len=20)
            for i, order in enumerate(["abcdefghij", "jihgfedcba", "acegikbdfhj"])]
    out += [
        [["wrt", "wrf", "er", "ett", "rftt"]], [["z", "x", "z"]], [["abc", "ab"]], [["z", "x"]],
        [["a"]], [["ab", "ab"]], [["ba", "ab", "ba"]],
    ]
    return out


def _weighted_edges(n, count, seed, lo=0, hi=10 ** 4):
    return G("wedges", n=count, nodes=n, seed=seed, lo=lo, hi=hi)


def _connected_weighted(n, extra, seed, lo=0, hi=10 ** 4):
    """A spanning path plus extra random edges, so the graph is always connected."""
    return G("wedges", n=extra, nodes=n, seed=seed, lo=lo, hi=hi, connected=True)


@cases("dijkstras-algorithm")
def _dijkstra():
    out = []
    for i, (n, count) in enumerate([(1, 0), (2, 1), (5, 6), (20, 40), (100, 300), (1000, 3000),
                                    (5000, 15000), (20000, 60000), (20000, 19999)]):
        out.append([n, _weighted_edges(n, count, 24400 + i), 0])
        out.append([n, _connected_weighted(n, count, 24500 + i), n // 2])
    out += [
        [1000, _connected_weighted(1000, 0, 24520, lo=0, hi=0), 0],       # zero-weight chain
        [1000, [], 0],
        [3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 0], [3, [[0, 1, 5]], 0], [1, [], 0], [2, [[0, 1, 0]], 1],
    ]
    return out


@cases("bellman-ford-algorithm")
def _bellman_ford():
    out = []
    for i, (n, count) in enumerate([(1, 0), (2, 1), (5, 6), (20, 40), (60, 150), (150, 400),
                                    (300, 1500), (500, 5000), (500, 499)]):
        out.append([n, _weighted_edges(n, count, 24600 + i, lo=-10, hi=1000), 0])
        out.append([n, _weighted_edges(n, count, 24700 + i, lo=-1000, hi=1000), 0])
    out += [
        [500, _weighted_edges(500, 2000, 24720, lo=1, hi=1000), 0],       # no negative edges
        [500, [], 0],
        [3, [[0, 1, 5], [1, 2, -2], [0, 2, 10]], 0], [3, [[0, 1, 1], [1, 2, -1], [2, 1, -1]], 0],
        [2, [], 0], [1, [], 0],
    ]
    return out


def _distance_matrix(n, seed, density=40, lo=-100, hi=1000):
    from cases import Rng
    rng = Rng(seed)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            elif rng.below(100) < density:
                row.append(rng.between(lo, hi))
            else:
                row.append(-1)
        matrix.append(row)
    return [matrix]


@cases("floyd-warshall-algorithm")
def _floyd_warshall():
    out = [_distance_matrix(n, 24800 + i) for i, n in enumerate([1, 2, 3, 5, 12, 30, 60, 90, 120])]
    out += [_distance_matrix(n, 24820 + i, density=95, lo=1, hi=100) for i, n in enumerate([10, 60, 120])]
    out += [_distance_matrix(n, 24840 + i, density=5) for i, n in enumerate([20, 100])]
    out += [
        [[[0, 1, 43], [1, 0, 6], [-1, -1, 0]]], [[[0, -1], [-1, 0]]], [[[0]]],
        [[[0, 5, -1], [-1, 0, 2], [-1, -1, 0]]],
    ]
    return out


def _mst_cases(seed0):
    out = []
    for i, (n, extra) in enumerate([(1, 0), (2, 0), (5, 5), (20, 30), (100, 200), (1000, 2000),
                                    (10000, 20000), (50000, 100000), (50000, 0)]):
        out.append([n, _connected_weighted(n, extra, seed0 + i)])
    out += [
        [1000, _connected_weighted(1000, 0, seed0 + 40, lo=5, hi=5)],
        [1000, _connected_weighted(1000, 3000, seed0 + 41, lo=0, hi=0)],
        [3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]], [2, [[0, 1, 7]]], [1, []],
        [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]]],
    ]
    return out


cases("minimum-spanning-tree-prims")(lambda: _mst_cases(24900))
cases("minimum-spanning-tree-kruskals")(lambda: _mst_cases(25000))


@cases("word-search-ii")
def _word_search_ii():
    out = []
    for i, (rows, cols, count) in enumerate([(1, 1, 1), (2, 2, 3), (3, 3, 10), (5, 5, 40),
                                             (8, 8, 200), (12, 12, 1000), (12, 12, 5000),
                                             (10, 10, 3000), (12, 12, 300)]):
        board = G("grid", rows=rows, cols=cols, alphabet="abc", asString=False, seed=25100 + i)
        out.append([board, G("words", n=count, minLen=1, maxLen=6, alphabet="abc", seed=25200 + i)])
    out += [
        [[list("aaaaaaaaaaaa") for _ in range(12)], ["a" * 10, "a" * 10 + "b", "ab"]],
        [[list("abcdefghijkl") for _ in range(12)], ["abcdefghij", "lkjihg", "aa"]],
        [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
         ["oath", "pea", "eat", "rain"]],
        [[["a", "b"], ["c", "d"]], ["abcb"]], [[["a"]], ["a"]], [[["a", "b"]], ["ab", "ba", "b"]],
    ]
    return out


# ------------------------------------------------ stacks, queues and design


def oplog(cls, ctor, methods, count, seed):
    """A design-problem call log as two generator specs (operations, arguments).

    Shipping the log literally costs hundreds of kilobytes per problem; this is
    a few hundred bytes and expands to the same calls in both harnesses.
    """
    shared = {"cls": cls, "ctor": ctor, "methods": methods, "n": count, "seed": seed}
    return [G("oplog", part="ops", **shared), G("oplog", part="args", **shared)]


@cases("implement-stack-using-arrays")
def _array_stack():
    methods = [
        {"name": "push", "args": [{"int": [-1000, 1000]}], "delta": 1, "weight": 3},
        {"name": "pop", "delta": -1},
        {"name": "top"},
        {"name": "size"},
    ]
    out = [oplog("ArrayStack", [cap], methods, count, 26000 + i)
           for i, (cap, count) in enumerate([(1, 5), (2, 10), (5, 30), (10, 100), (50, 300),
                                             (100, 1000), (1000, 5000), (10, 5000), (100000, 20000)])]
    out += [
        [["ArrayStack", "push", "push", "top", "pop", "size", "pop", "pop"], [[2], [1], [2], [], [], [], [], []]],
        [["ArrayStack", "pop", "top", "size"], [[1], [], [], []]],
        [["ArrayStack", "push", "push", "size"], [[1], [5], [6], []]],
    ]
    return out

@cases("implement-queue-using-arrays")
def _array_queue():
    methods = [
        {"name": "push", "args": [{"int": [-1000, 1000]}], "delta": 1, "weight": 3},
        {"name": "pop", "delta": -1},
        {"name": "front"},
        {"name": "size"},
    ]
    out = [oplog("ArrayQueue", [cap], methods, count, 26100 + i)
           for i, (cap, count) in enumerate([(1, 5), (2, 10), (5, 30), (10, 100), (50, 300),
                                             (100, 1000), (1000, 5000), (10, 5000), (100000, 20000)])]
    out += [
        [["ArrayQueue", "push", "push", "front", "pop", "size", "pop", "pop"], [[2], [1], [2], [3], [], [], [], []]],
        [["ArrayQueue", "pop", "front", "size"], [[1], [], [], []]],
        [["ArrayQueue", "push", "push", "push", "pop", "push", "front"], [[2], [1], [2], [3], [], [4], []]],
    ]
    return out

@cases("implement-stack-using-queues")
def _stack_using_queues():
    # `pop` and `top` are only called on a non-empty stack, which the delta and
    # needs fields enforce while the log is generated.
    methods = [
        {"name": "push", "args": [{"int": [1, 9]}], "delta": 1, "weight": 3},
        {"name": "pop", "delta": -1, "needs": 1},
        {"name": "top", "needs": 1},
        {"name": "empty"},
    ]
    out = [oplog("MyStack", [], methods, count, 26200 + i)
           for i, count in enumerate([1, 2, 5, 10, 20, 40, 60, 80, 99])]
    out += [
        [["MyStack", "push", "push", "top", "pop", "empty"], [[], [1], [2], [], [], []]],
        [["MyStack", "empty"], [[], []]],
        [["MyStack", "push", "pop", "empty"], [[], [3], [], []]],
    ]
    return out

@cases("implement-queue-using-stacks")
def _queue_using_stacks():
    methods = [
        {"name": "push", "args": [{"int": [1, 9]}], "delta": 1, "weight": 3},
        {"name": "pop", "delta": -1, "needs": 1},
        {"name": "peek", "needs": 1},
        {"name": "empty"},
    ]
    out = [oplog("MyQueue", [], methods, count, 26300 + i)
           for i, count in enumerate([1, 2, 5, 10, 20, 40, 60, 80, 99])]
    out += [
        [["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]],
        [["MyQueue", "empty"], [[], []]],
        [["MyQueue", "push", "pop", "empty"], [[], [3], [], []]],
    ]
    return out

@cases("min-stack")
def _min_stack():
    def methods(lo, hi):
        return [
            {"name": "push", "args": [{"int": [lo, hi]}], "delta": 1, "weight": 3},
            {"name": "pop", "delta": -1, "needs": 1},
            {"name": "top", "needs": 1},
            {"name": "getMin", "needs": 1},
        ]

    out = [oplog("MinStack", [], methods(-10 ** 9, 10 ** 9), count, 26400 + i)
           for i, count in enumerate([1, 3, 10, 40, 200, 1000, 5000, 20000, 30000])]
    out += [oplog("MinStack", [], methods(-5, 5), count, 26420 + i)
            for i, count in enumerate([50, 500, 5000, 20000])]
    out += [
        [["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
         [[], [-2], [0], [-3], [], [], [], []]],
        [["MinStack", "push", "getMin", "top"], [[], [5], [], []]],
        [["MinStack", "push", "push", "pop", "getMin"], [[], [2], [1], [], []]],
    ]
    return out

@cases("lru-cache")
def _lru_cache():
    def methods(space):
        return [
            {"name": "get", "args": [{"int": [0, space]}], "weight": 45},
            {"name": "put", "args": [{"int": [0, space]}, {"int": [0, 10 ** 4]}], "weight": 55},
        ]

    out = [oplog("LRUCache", [cap], methods(space), count, 26500 + i)
           for i, (cap, count, space) in enumerate([(1, 5, 3), (2, 20, 4), (3, 60, 6), (10, 200, 20),
                                                    (50, 1000, 100), (100, 3000, 150),
                                                    (500, 10000, 1000), (3000, 50000, 5000),
                                                    (5, 50000, 8)])]
    out += [
        oplog("LRUCache", [2], methods(2), 2000, 26520),      # always hits
        oplog("LRUCache", [2], methods(200), 2000, 26521),    # almost always misses
        [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]],
        [["LRUCache", "put", "get", "get"], [[1], [1, 5], [1], [2]]],
        [["LRUCache", "put", "put", "put", "get"], [[2], [1, 1], [2, 2], [1, 9], [1]]],
    ]
    return out

@cases("lfu-cache")
def _lfu_cache():
    def methods(space):
        return [
            {"name": "get", "args": [{"int": [0, space]}], "weight": 45},
            {"name": "put", "args": [{"int": [0, space]}, {"int": [0, 10 ** 5]}], "weight": 55},
        ]

    out = [oplog("LFUCache", [cap], methods(space), count, 26600 + i)
           for i, (cap, count, space) in enumerate([(0, 5, 3), (1, 10, 3), (2, 30, 4), (3, 80, 6),
                                                    (10, 300, 20), (50, 1500, 100),
                                                    (200, 8000, 400), (1000, 40000, 2000),
                                                    (4, 40000, 6)])]
    out += [
        oplog("LFUCache", [3], methods(3), 2000, 26620),
        oplog("LFUCache", [3], methods(300), 2000, 26621),
        [["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
         [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]],
        [["LFUCache", "put", "get"], [[0], [1, 1], [1]]],
        [["LFUCache", "put", "put", "put", "get", "get"], [[2], [1, 1], [2, 2], [3, 3], [1], [3]]],
    ]
    return out

@cases("online-stock-span")
def _stock_spanner():
    def methods(hi):
        return [{"name": "next", "args": [{"int": [1, hi]}]}]

    out = [oplog("StockSpanner", [], methods(10 ** 5), count, 26700 + i)
           for i, count in enumerate([1, 2, 5, 20, 100, 500, 2000, 8000, 10000])]
    out += [oplog("StockSpanner", [], methods(hi), 8000, 26720 + i) for i, hi in enumerate([2, 10, 1000])]
    for i, count in enumerate([100, 1000, 10000]):
        out.append([["StockSpanner"] + ["next"] * count, [[]] + [[j + 1] for j in range(count)]])
        out.append([["StockSpanner"] + ["next"] * count, [[]] + [[count - j] for j in range(count)]])
    out += [
        [["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
         [[], [100], [80], [60], [70], [60], [75], [85]]],
        [["StockSpanner", "next", "next"], [[], [5], [5]]],
        [["StockSpanner", "next", "next", "next"], [[], [3], [2], [1]]],
    ]
    return out

@cases("kth-largest-element-in-a-stream")
def _kth_largest_stream():
    methods = [{"name": "add", "args": [{"int": [-10 ** 4, 10 ** 4]}]}]
    out = []
    for i, (k, initial, count) in enumerate([(1, 0, 5), (1, 3, 10), (2, 2, 20), (3, 4, 40),
                                             (10, 20, 100), (50, 100, 500), (100, 500, 2000),
                                             (1000, 5000, 5000), (5, 10000, 5000)]):
        nums = expand(ints(initial, -10 ** 4, 10 ** 4, 26800 + i)) if initial else []
        out.append(oplog("KthLargest", [k, nums], methods, count, 26900 + i))
    out += [
        [["KthLargest", "add", "add", "add", "add", "add"], [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]],
        [["KthLargest", "add", "add"], [[1, []], [-1], [1]]],
        [["KthLargest", "add"], [[2, [1, 2]], [3]]],
    ]
    return out

@cases("find-median-from-data-stream")
def _median_finder():
    def methods(lo, hi):
        return [
            {"name": "addNum", "args": [{"int": [lo, hi]}], "delta": 1, "weight": 2},
            {"name": "findMedian", "needs": 1},
        ]

    out = [oplog("MedianFinder", [], methods(-10 ** 5, 10 ** 5), count, 27000 + i)
           for i, count in enumerate([1, 2, 5, 20, 100, 500, 2000, 10000, 20000])]
    out += [oplog("MedianFinder", [], methods(0, 1), count, 27020 + i)
            for i, count in enumerate([50, 500, 5000, 20000])]
    out += [
        [["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
         [[], [1], [2], [], [3], []]],
        [["MedianFinder", "addNum", "findMedian"], [[], [5], []]],
        [["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
         [[], [4], [1], [3], [2], []]],
    ]
    return out

@cases("next-greater-element-i")
def _next_greater_element_i():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 120, 400, 1000]):
        values = expand(G("perm", n=n, seed=27100 + i))
        subset = values[:: max(1, n // 5)]
        out.append([subset, values])
        out.append([values, values])
    out += [
        [expand(G("arange", n=1000)), expand(G("arange", n=1000))],
        [expand(G("arange", n=1000)), expand(G("arange", n=1000, start=999, step=-1))],
        [[4, 1, 2], [1, 3, 4, 2]], [[2, 4], [1, 2, 3, 4]], [[1], [1]], [[3, 1], [3, 1, 5]],
    ]
    return out


@cases("next-smaller-element")
def _next_smaller_element():
    out = [[ints(n, -10 ** 9, 10 ** 9, 27200 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000])]
    out += [
        [G("arange", n=100000)], [G("arange", n=100000, start=100000, step=-1)],
        [G("repeat", value=5, n=100000)], [G("perm", n=100000)], [ints(100000, 0, 3, 27220)],
        [[4, 8, 5, 2, 25]], [[1, 2, 3]], [[3, 2, 1]], [[5]], [[2, 2, 1]],
    ]
    return out


@cases("sort-a-stack")
def _sort_a_stack():
    out = [[ints(n, -10 ** 9, 10 ** 9, 27300 + i)] for i, n in enumerate([0, 1, 2, 3, 8, 30, 300, 1200, 2000])]
    out += [
        [G("arange", n=2000)], [G("arange", n=2000, start=2000, step=-1)],
        [G("repeat", value=4, n=2000)], [G("perm", n=2000)], [ints(2000, 0, 5, 27320)],
        [[11, 2, 32, 3, 41]], [[-3, 14, 18, -5, 30]], [[]], [[1]], [[2, 1]],
    ]
    return out


@cases("largest-rectangle-in-histogram")
def _largest_rectangle():
    out = [[ints(n, 0, 10 ** 4, 27400 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000])]
    out += [
        [G("arange", n=100000)], [G("arange", n=100000, start=100000, step=-1)],
        [G("repeat", value=10 ** 4, n=100000)], [G("repeat", value=0, n=100000)],
        [ints(100000, 0, 1, 27420)],
        [G("concat", parts=[G("arange", n=50000), G("arange", n=50000, start=50000, step=-1)])],
        [[2, 1, 5, 6, 2, 3]], [[2, 4]], [[0]], [[1, 1, 1, 1]], [[5, 4, 3, 2, 1]],
    ]
    return out


@cases("sliding-window-maximum")
def _sliding_window_maximum():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000]):
        spec = ints(n, -10 ** 4, 10 ** 4, 27500 + i)
        for k in {1, 2, n // 2 or 1, n}:
            out.append([spec, k])
    out += [
        [G("arange", n=100000), 1000], [G("arange", n=100000, start=100000, step=-1), 1000],
        [G("repeat", value=7, n=100000), 500], [ints(100000, 0, 1, 27520), 3],
        [[1, 3, -1, -3, 5, 3, 6, 7], 3], [[1], 1], [[1, -1], 1], [[9, 8, 7, 6], 2],
    ]
    return out


@cases("maximum-of-minimum-every-window-size")
def _max_of_min():
    out = [[ints(n, -10 ** 9, 10 ** 9, 27600 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000])]
    out += [
        [G("arange", n=100000)], [G("arange", n=100000, start=100000, step=-1)],
        [G("repeat", value=9, n=100000)], [G("perm", n=100000)], [ints(100000, 0, 3, 27620)],
        [[10, 20, 30, 50, 10, 70, 30]], [[10, 20, 30]], [[5]], [[1, 1]], [[3, 1, 3]],
    ]
    return out


def _celebrity_matrix(n, seed, celebrity=None):
    return [G("knows", n=n, seed=seed, celebrity=celebrity)]


@cases("the-celebrity-problem")
def _celebrity():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 150, 600, 1500, 3000]):
        out.append(_celebrity_matrix(n, 27700 + i))                       # usually nobody
        out.append(_celebrity_matrix(n, 27800 + i, celebrity=n // 2))     # exactly one
    out += [
        _celebrity_matrix(1000, 27820, celebrity=0),
        _celebrity_matrix(1000, 27821, celebrity=999),
        [[[1, 1, 0], [0, 1, 0], [1, 1, 1]]], [[[1, 0, 1], [1, 1, 0], [0, 1, 1]]],
        [[[1]]], [[[1, 1], [0, 1]]],
    ]
    return out


@cases("distinct-numbers-in-every-window")
def _distinct_in_window():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000]):
        spec = ints(n, -10 ** 9, 10 ** 9, 27900 + i)
        for k in {1, 2, n // 2 or 1, n}:
            out.append([spec, k])
    out += [
        [G("repeat", value=1, n=100000), 100], [G("arange", n=100000), 100],
        [ints(100000, 0, 5, 27920), 10], [G("perm", n=100000), 1000],
        [[1, 2, 1, 3, 4, 2, 3], 4], [[1, 1, 1], 2], [[1], 1], [[1, 2, 3], 3],
    ]
    return out


@cases("maximum-sum-combinations")
def _max_sum_combinations():
    out = []
    for i, n in enumerate([1, 2, 3, 8, 30, 100, 300, 1000, 3000]):
        a = ints(n, -10 ** 5, 10 ** 5, 28000 + i)
        b = ints(n, -10 ** 5, 10 ** 5, 28100 + i)
        for k in {1, 2, min(n * n, 100), min(n * n, 10 ** 4)}:
            out.append([a, b, k])
    out += [
        [G("repeat", value=5, n=100), G("repeat", value=5, n=100), 100],
        [G("arange", n=100), G("arange", n=100), 100],
        [[3, 2], [1, 4], 2], [[1, 4, 2, 3], [2, 5, 1, 6], 3], [[1], [1], 1], [[1, 2], [3, 4], 4],
    ]
    return out


# ------------------------------------------------------------- backtracking


@cases("permutations")
def _permutations():
    out = [[expand(G("perm", n=n, seed=28200 + i))] for i, n in enumerate([1, 2, 3, 4, 5, 6, 7, 8])]
    out += [[expand(ints(n, -10, 10, 28220 + i))] for i, n in enumerate([1, 2, 3, 4, 5])]
    out += [[list(range(n))] for n in (1, 2, 3, 4, 5, 6, 7, 8)]
    out += [[[1, 2, 3]], [[0, 1]], [[1]], [[-1, 2]], [[-10, 0, 10]], [[5, 4, 3, 2]]]
    return out


@cases("subsets-ii")
def _subsets_ii():
    out = [[expand(ints(n, -10, 10, 28300 + i))] for i, n in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
    out += [[expand(ints(n, 0, 1, 28320 + i))] for i, n in enumerate([2, 4, 6, 8, 10])]
    out += [[[1] * n] for n in (1, 3, 5, 8, 10)]
    out += [[[1, 2, 2]], [[0]], [[1, 1]], [[4, 4, 4, 1, 4]], [[-1, 0, 1]]]
    return out


@cases("subset-sums")
def _subset_sums():
    out = [[expand(ints(n, 0, 10 ** 4, 28400 + i))] for i, n in enumerate([1, 2, 3, 5, 8, 10, 11, 12, 15])]
    out += [[[0] * n] for n in (1, 3, 6, 10)]
    out += [[list(range(1, n + 1))] for n in (1, 4, 8, 11, 15)]
    out += [[[2, 3]], [[5, 2, 1]], [[0]], [[1, 1]]]
    return out


@cases("power-set")
def _power_set():
    alphabet = "abcdefghijklmnop"
    out = [[alphabet[:n]] for n in range(1, 17)]
    out += [["abc"], ["ab"], ["a"], ["xy"], ["zyxw"], ["qwerty"]]
    return out


@cases("combination-sum")
def _combination_sum():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 8, 15, 30]):
        spec = expand(G("sorted", n=n, lo=2, hi=40, seed=28500 + i, unique=True))
        for target in (7, 20, 30, 40):
            out.append([spec, target])
    out += [
        [[2], 40], [[2, 3], 40], [list(range(2, 32)), 40], [[40], 40], [[39], 40],
        [[2, 3, 6, 7], 7], [[2, 3, 5], 8], [[2], 1], [[3], 9],
    ]
    return out


@cases("combination-sum-ii")
def _combination_sum_ii():
    out = []
    for i, n in enumerate([1, 2, 3, 5, 10, 25, 50, 100]):
        spec = expand(ints(n, 1, 50, 28600 + i))
        for target in (5, 15, 30):
            out.append([spec, target])
    out += [
        [[1] * 30, 5], [[2] * 30, 30], [[1, 1, 1, 2, 2, 3, 3, 3, 5], 6],
        [[10, 1, 2, 7, 6, 1, 5], 8], [[2, 5, 2, 1, 2], 5], [[1], 2], [[1, 1], 2],
    ]
    return out


@cases("palindrome-partitioning")
def _palindrome_partitioning():
    out = [[expand(text(n, 28700 + i, "ab"))] for i, n in enumerate([1, 2, 3, 4, 6, 8, 10, 12, 14, 16])]
    out += [[expand(text(n, 28720 + i, "abcd"))] for i, n in enumerate([4, 8, 12, 16])]
    out += [["a" * n] for n in (1, 4, 8, 12, 16)]
    out += [["aab"], ["a"], ["ab"], ["aba"], ["abba"]]
    return out


@cases("permutation-sequence")
def _permutation_sequence():
    import math
    out = []
    for n in range(1, 10):
        total = math.factorial(n)
        for k in {1, 2, total // 2, total - 1, total}:
            if 1 <= k <= total:
                out.append([n, k])
    return out


@cases("n-queens")
def _n_queens():
    return [[n] for n in range(1, 10)] + [[4], [1], [2], [3], [6], [8]]


def _sudoku_from_seed(seed, blanks):
    """A solved grid (shuffled from the canonical pattern) with `blanks` cells removed."""
    from cases import Rng
    rng = Rng(seed)
    digits = [str(d) for d in range(1, 10)]
    for i in range(8, 0, -1):
        j = rng.below(i + 1)
        digits[i], digits[j] = digits[j], digits[i]
    rows = [(3 * (r % 3) + r // 3) for r in range(9)]
    grid = [[digits[(rows[r] + c) % 9] for c in range(9)] for r in range(9)]

    cells = [(r, c) for r in range(9) for c in range(9)]
    for i in range(len(cells) - 1, 0, -1):
        j = rng.below(i + 1)
        cells[i], cells[j] = cells[j], cells[i]
    for r, c in cells[:blanks]:
        grid[r][c] = "."
    return [grid]


def _sudoku_unique(args, _expected):
    """Only keep puzzles with exactly one solution, as the problem promises."""
    board = [row[:] for row in args[0]]
    empty = [(r, c) for r in range(9) for c in range(9) if board[r][c] == "."]
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3) * 3 + c // 3].add(board[r][c])

    found = [0]

    def walk(index):
        if index == len(empty):
            found[0] += 1
            return found[0] > 1
        r, c = empty[index]
        box = (r // 3) * 3 + c // 3
        for digit in "123456789":
            if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                continue
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)
            if walk(index + 1):
                return True
            rows[r].discard(digit)
            cols[c].discard(digit)
            boxes[box].discard(digit)
        return False

    walk(0)
    return found[0] == 1


@cases("sudoku-solver", validate=_sudoku_unique)
def _sudoku_solver():
    out = [_sudoku_from_seed(28800 + i, blanks) for i, blanks in enumerate(
        [1, 2, 3, 5, 8, 12, 16, 20, 24, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48])]
    out += [_sudoku_from_seed(28900 + i, 45) for i in range(10)]
    out += [
        [[["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]],
    ]
    return out


@cases("m-coloring-problem")
def _m_coloring():
    out = []
    for i, (n, count) in enumerate([(1, 0), (2, 1), (3, 3), (5, 7), (8, 15), (12, 25), (16, 40), (20, 60)]):
        edges = expand(G("edges", n=count, nodes=n, seed=29000 + i))
        edges = [[a, b] for a, b in edges if a != b]
        for m in {1, 2, 3, min(n, 4)}:
            out.append([n, edges, m])
    out += [
        [10, [[i, j] for i in range(10) for j in range(i + 1, 10)], 9],     # complete graph
        [10, [[i, j] for i in range(10) for j in range(i + 1, 10)], 10],
        [10, [[i, i + 1] for i in range(9)], 2],                            # a path
        [4, [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]], 3],
        [3, [[0, 1], [1, 2], [2, 0]], 2], [1, [], 1], [4, [[0, 1], [1, 2], [2, 3], [3, 0]], 2],
    ]
    return out


@cases("rat-in-a-maze")
def _rat_in_a_maze():
    out = []
    for i, (n, density) in enumerate([(1, 100), (2, 100), (2, 60), (3, 80), (3, 60), (4, 85),
                                      (4, 70), (5, 90), (5, 75), (5, 60)]):
        grid = expand(G("grid", rows=n, cols=n, lo=0, hi=99, seed=29100 + i))
        maze = [[1 if value < density else 0 for value in row] for row in grid]
        out.append([maze])
    out += [[[[1] * n for _ in range(n)]] for n in (1, 2, 3, 4, 5)]
    out += [
        [[[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]],
        [[[1, 0], [1, 0]]], [[[1]]], [[[1, 1], [1, 1]]], [[[0]]],
        [[[1, 1, 1], [0, 0, 1], [1, 1, 1]]],
    ]
    return out


# --------------------------------------------------------- tries and strings


def _word_pool(count, seed, min_len=1, max_len=8, alphabet="abcd"):
    return expand(G("words", n=count, minLen=min_len, maxLen=max_len, alphabet=alphabet, seed=seed))


def _word_pool_spec(count, seed, min_len=1, max_len=8, alphabet="abcd"):
    return G("words", n=count, minLen=min_len, maxLen=max_len, alphabet=alphabet, seed=seed)


@cases("implement-trie-prefix-tree")
def _trie():
    def methods(alphabet, max_len):
        word = {"word": {"minLen": 1, "maxLen": max_len, "alphabet": alphabet}}
        return [
            {"name": "insert", "args": [word], "weight": 2},
            {"name": "search", "args": [word]},
            {"name": "startsWith", "args": [word]},
        ]

    out = [oplog("Trie", [], methods(alphabet, max_len), count, 29200 + i)
           for i, (alphabet, max_len, count) in enumerate(
               [("ab", 2, 5), ("ab", 3, 20), ("abc", 4, 60), ("abc", 5, 200), ("abcd", 6, 800),
                ("abcd", 8, 3000), ("abcde", 10, 10000), ("abcdefgh", 12, 20000),
                ("ab", 20, 20000)])]
    out += [
        [["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
         [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]],
        [["Trie", "search", "startsWith"], [[], ["a"], ["a"]]],
        [["Trie", "insert", "startsWith", "startsWith"], [[], ["ab"], ["abc"], ["a"]]],
    ]
    return out

@cases("implement-trie-ii")
def _trie_ii():
    def methods(alphabet, max_len):
        word = {"word": {"minLen": 1, "maxLen": max_len, "alphabet": alphabet}}
        return [
            {"name": "insert", "args": [word], "weight": 2},
            {"name": "countWordsEqualTo", "args": [word]},
            {"name": "countWordsStartingWith", "args": [word]},
        ]

    # `erase` needs a word that is definitely present, which a stateless log
    # cannot promise — the hand-written cases below cover it instead.
    out = [oplog("Trie", [], methods(alphabet, max_len), count, 29400 + i)
           for i, (alphabet, max_len, count) in enumerate(
               [("ab", 2, 6), ("ab", 3, 20), ("abc", 4, 60), ("abc", 5, 200), ("abcd", 6, 800),
                ("abcd", 8, 3000), ("abcde", 10, 10000), ("abcdefgh", 12, 20000),
                ("ab", 20, 20000)])]
    out += [
        [["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith",
          "erase", "countWordsEqualTo", "countWordsStartingWith"],
         [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"]]],
        [["Trie", "countWordsEqualTo", "countWordsStartingWith"], [[], ["a"], ["a"]]],
        [["Trie", "insert", "insert", "erase", "countWordsStartingWith"], [[], ["ab"], ["abc"], ["ab"], ["a"]]],
    ]
    return out

@cases("design-add-and-search-words-data-structure")
def _word_dictionary():
    def methods(alphabet, max_len):
        return [
            {"name": "addWord", "args": [{"word": {"minLen": 1, "maxLen": max_len, "alphabet": alphabet}}],
             "weight": 2},
            {"name": "search", "args": [{"word": {"minLen": 1, "maxLen": max_len,
                                                  "alphabet": alphabet + "."}}], "weight": 3},
        ]

    out = [oplog("WordDictionary", [], methods(alphabet, max_len), count, 29600 + i)
           for i, (alphabet, max_len, count) in enumerate(
               [("ab", 2, 5), ("ab", 3, 20), ("abc", 4, 60), ("abc", 5, 200), ("abc", 6, 800),
                ("abcd", 8, 2000), ("abcd", 10, 5000), ("abcde", 12, 8000), ("ab", 20, 8000)])]
    out += [
        [["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
         [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]],
        [["WordDictionary", "search"], [[], ["a"]]],
        [["WordDictionary", "addWord", "search", "search"], [[], ["a"], ["."], ["a."]]],
    ]
    return out

@cases("longest-string-with-all-prefixes")
def _longest_word_all_prefixes():
    out = []
    for i, count in enumerate([1, 2, 5, 20, 100, 1000, 10000, 50000, 100000]):
        out.append([_word_pool_spec(count, 29800 + i, min_len=1, max_len=6, alphabet="abc")])
    for i, depth in enumerate([2, 5, 12, 30]):
        chain = ["a" * k for k in range(1, depth + 1)]
        out.append([chain])
        out.append([chain[1:]])                                            # missing the shortest prefix
    out += [
        [["n", "ni", "nin", "ninj", "ninja", "nil"]], [["ab", "a", "abc", "abcd"]],
        [["b", "ba", "bal"]], [["ab"]], [["a"]],
    ]
    return out


@cases("number-of-distinct-substrings")
def _distinct_substrings():
    out = [[text(n, 29900 + i, "ab")] for i, n in enumerate([1, 2, 3, 8, 30, 100, 300, 700, 1000])]
    out += [[text(n, 29920 + i, LOWER)] for i, n in enumerate([10, 100, 1000])]
    out += [
        [G("strrepeat", value="a", n=1000)], [G("strrepeat", value="ab", n=500)],
        [G("strrepeat", value="abc", n=333)], [text(1000, 29930, "abcde")],
        ["ababa"], ["ccfdf"], ["a"], ["aa"], ["abc"],
    ]
    return out


@cases("maximum-xor-of-two-numbers-in-an-array")
def _maximum_xor():
    out = [[ints(n, 0, 2 ** 31 - 1, 30000 + i)] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 200000])]
    out += [
        [ints(200000, 0, 255, 30020)], [G("arange", n=200000)], [G("repeat", value=12345, n=200000)],
        [G("perm", n=100000)], [[2 ** 31 - 1, 0]], [ints(100000, 0, 1, 30021)],
        [[3, 10, 5, 25, 2, 8]], [[0]], [[8, 10, 2]], [[2147483647, 0]],
    ]
    return out


@cases("maximum-xor-with-an-element-from-array")
def _maximize_xor():
    out = []
    for i, (n, q) in enumerate([(1, 1), (2, 3), (5, 5), (20, 20), (100, 100), (1000, 1000),
                                (10000, 10000), (100000, 100000), (100000, 1000)]):
        nums = ints(n, 0, 10 ** 9, 30100 + i)
        queries = [[x, m] for x, m in zip(expand(ints(q, 0, 10 ** 9, 30200 + i)),
                                          expand(ints(q, 0, 10 ** 9, 30300 + i)))]
        out.append([nums, queries])
    out += [
        [[1], [[1, 0]]], [[1], [[1, 1]]],
        [[0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]],
        [[5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]],
        [G("repeat", value=7, n=1000), [[7, 7], [0, 0], [10 ** 9, 10 ** 9]]],
    ]
    return out


@cases("reverse-words-in-a-string")
def _reverse_words():
    out = [[text(n, 30400 + i, "abc   ")] for i, n in enumerate([1, 2, 5, 20, 100, 1000, 5000, 10000])]
    out += [
        [G("strrepeat", value="ab ", n=3000)],
        [G("strrepeat", value=" ", n=5000)],
        [G("concat", parts=[G("strrepeat", value=" ", n=4000), "word"])],
        [G("concat", parts=["word", G("strrepeat", value=" ", n=4000)])],
        ["the sky is blue"], ["  hello world  "], ["a good   example"], ["single"], ["a"],
    ]
    return out


@cases("compare-version-numbers")
def _compare_version():
    def version(parts, seed, width=3):
        from cases import Rng
        rng = Rng(seed)
        return ".".join(str(rng.below(10 ** width)) for _ in range(parts))

    out = []
    for i, (a, b) in enumerate([(1, 1), (1, 2), (2, 1), (3, 3), (5, 5), (10, 3), (3, 10), (60, 60)]):
        out.append([version(a, 30500 + i), version(b, 30600 + i)])
        same = version(a, 30700 + i)
        out.append([same, same])
        out.append([same, same + ".0"])
        out.append([same, "0" * 3 + same])
    out += [
        ["1.01", "1.001"], ["1.0", "1.0.0"], ["0.1", "1.1"], ["1.2", "1.10"], ["1", "1.0.0.0"],
        ["0", "0.0"], ["1.0.1", "1"],
    ]
    return out


def _matching_cases(seed0):
    out = []
    for i, (n, m, alphabet) in enumerate([(1, 1, "a"), (5, 2, "ab"), (20, 3, "ab"), (100, 5, "abc"),
                                          (1000, 10, "abc"), (10000, 20, "ab"), (100000, 50, LOWER),
                                          (100000, 3, "ab"), (100000, 1, "a")]):
        text_spec = text(n, seed0 + i, alphabet)
        out.append([text_spec, text(m, seed0 + 50 + i, alphabet)])
        expanded = expand(text_spec)
        if len(expanded) >= m:
            out.append([text_spec, expanded[: m]])                      # occurs at least once
            out.append([text_spec, expanded[len(expanded) - m:]])
    out += [
        [G("strrepeat", value="a", n=100000), G("strrepeat", value="a", n=100)],
        [G("strrepeat", value="ab", n=50000), "abab"],
        [G("concat", parts=[G("strrepeat", value="a", n=99999), "b"]), "ab"],
        ["abcabcabc", "abc"], ["aaaa", "aa"], ["abcd", "e"], ["a", "a"],
    ]
    return out


cases("rabin-karp")(lambda: _matching_cases(30800))
cases("kmp-algorithm")(lambda: _matching_cases(30900))


@cases("z-algorithm")
def _z_algorithm():
    out = [[text(n, 31000 + i, "ab")] for i, n in enumerate([1, 2, 3, 8, 30, 300, 3000, 30000, 100000])]
    out += [[text(n, 31020 + i, LOWER)] for i, n in enumerate([50, 5000, 100000])]
    out += [
        [G("strrepeat", value="a", n=100000)], [G("strrepeat", value="ab", n=50000)],
        [G("strrepeat", value="aab", n=33333)],
        [G("concat", parts=[G("strrepeat", value="a", n=50000), G("strrepeat", value="b", n=50000)])],
        ["aabxaabxcaabxaabxay"], ["aaaa"], ["a"], ["abc"],
    ]
    return out


@cases("encode-and-decode-strings")
def _encode_decode_strings():
    out = []
    for i, (count, length) in enumerate([(0, 0), (1, 0), (1, 5), (3, 10), (10, 50), (50, 100),
                                         (100, 200), (200, 200), (200, 1)]):
        words = [expand(text(length, 31100 + i * 20 + j, "ab#0123 ")) if length else "" for j in range(count)]
        out.append([words])
    out += [
        [["hello", "world"]], [[""]], [[]], [["a#b", "3#x", ""]],
        [["", "", ""]], [["#" * 200]], [["2#ab", "ab"]], [[" ", "  ", "   "]],
    ]
    return out


# ------------------------------------------------------------------ top-ups
#
# Problems whose suites came up short once oversized answers were dropped.

add("bfs-of-graph", [[_adjacency(n, count, 31200 + i)] for i, (n, count) in enumerate(
    [(3, 2), (6, 8), (15, 25), (40, 60), (120, 200), (350, 600), (900, 1500), (2500, 5000)])])

add("dfs-of-graph", [[_adjacency(n, count, 31300 + i)] for i, (n, count) in enumerate(
    [(3, 2), (6, 8), (15, 25), (40, 60), (120, 200), (350, 600), (900, 1500), (2500, 5000)])])

add("floyd-warshall-algorithm", [_distance_matrix(n, 31400 + i, density=d)
                                 for i, (n, d) in enumerate(
                                     [(4, 30), (7, 60), (15, 20), (25, 70), (45, 45), (70, 25),
                                      (90, 80), (110, 10)])])

add("z-algorithm", [[text(n, 31500 + i, alphabet)] for i, (n, alphabet) in enumerate(
    [(4, "ab"), (12, "ab"), (60, "abc"), (600, "abc"), (6000, "abcd"), (60000, LOWER),
     (100000, "ab"), (100000, "abcde")])])

add("power-set", [[s] for s in ["b", "xy", "abcd", "wxyz", "mnopq", "abcdefg", "hijklmno",
                                "abcdefghij", "qrstuvwxyz", "abcdefghijklmno"]])

add("encode-and-decode-strings", [
    [["", "a", "", "bc", ""]], [["#", "##", "###"]], [["1#a", "0#", "2#bc"]],
    [[" " * 200]], [["\\n", "\\t", "\\\\"]], [["x" * 200] * 5], [["a"] * 200],
    [[str(i) for i in range(200)]],
])

add("next-smaller-element", sweep([5, 15, 60, 250, 900, 4000, 25000, 70000], -1000, 1000, 31600))

add("maximum-of-minimum-every-window-size",
    sweep([5, 15, 60, 250, 900, 4000, 25000, 70000], -1000, 1000, 31700))

add("min-stack", [[["MinStack", "push", "push", "push", "pop", "getMin", "top", "pop", "getMin"],
                   [[], [v], [v - 1], [v + 1], [], [], [], [], []]] for v in
                  (0, 5, -5, 1000, -1000, 2 ** 31 - 1, -2 ** 31, 42, 7, 13)])

add("implement-trie-prefix-tree", [
    [["Trie"] + ops, [[]] + [[w] for w in words]]
    for ops, words in [
        (["insert", "search"], ["a", "a"]),
        (["insert", "search", "startsWith"], ["abc", "ab", "ab"]),
        (["insert", "insert", "search", "search"], ["ab", "abc", "ab", "abc"]),
        (["startsWith", "insert", "startsWith"], ["z", "zz", "z"]),
        (["insert", "insert", "insert", "search", "startsWith"], ["a", "ab", "abc", "abcd", "abc"]),
        (["insert", "search", "search", "search"], ["hello", "hell", "hello", "helloo"]),
        (["insert", "startsWith", "startsWith", "startsWith"], ["prefix", "pre", "prefix", "prefixx"]),
        (["insert", "insert", "search"], ["same", "same", "same"]),
    ]])

add("implement-trie-ii", [
    [["Trie"] + ops, [[]] + [[w] for w in words]]
    for ops, words in [
        (["insert", "countWordsEqualTo"], ["a", "a"]),
        (["insert", "insert", "countWordsEqualTo", "erase", "countWordsEqualTo"], ["a", "a", "a", "a", "a"]),
        (["insert", "countWordsStartingWith", "countWordsStartingWith"], ["abc", "ab", "abcd"]),
        (["insert", "insert", "insert", "countWordsStartingWith", "erase", "countWordsStartingWith"],
         ["ab", "abc", "abd", "ab", "abc", "ab"]),
        (["countWordsEqualTo", "countWordsStartingWith"], ["x", "x"]),
        (["insert", "erase", "countWordsEqualTo", "countWordsStartingWith"], ["q", "q", "q", "q"]),
    ]])

add("design-add-and-search-words-data-structure", [
    [["WordDictionary"] + ops, [[]] + [[w] for w in words]]
    for ops, words in [
        (["addWord", "search"], ["a", "a"]),
        (["addWord", "search", "search"], ["ab", ".b", "a."]),
        (["addWord", "addWord", "search", "search"], ["abc", "abd", "ab.", "a.c"]),
        (["search", "addWord", "search"], ["...", "xyz", "..."]),
        (["addWord", "search", "search", "search"], ["hello", "h....", ".....", "h...."]),
        (["addWord", "addWord", "addWord", "search"], ["aa", "ab", "ac", "a."]),
        (["addWord", "search"], ["a" * 25, "." * 25]),
    ]])

add("find-median-from-data-stream", [
    [["MedianFinder"] + ops, [[]] + args]
    for ops, args in [
        (["addNum", "findMedian"], [[1], []]),
        (["addNum", "addNum", "findMedian"], [[-1], [1], []]),
        (["addNum", "addNum", "addNum", "findMedian"], [[5], [5], [5], []]),
        (["addNum", "findMedian", "addNum", "findMedian"], [[100000], [], [-100000], []]),
        (["addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"],
         [[1], [2], [3], [4], [5], []]),
        (["addNum", "addNum", "findMedian", "addNum", "addNum", "findMedian"],
         [[0], [0], [], [1], [-1], []]),
    ]])

add("kth-largest-element-in-a-stream", [
    [["KthLargest"] + ["add"] * len(values), [[k, initial]] + [[v] for v in values]]
    for k, initial, values in [
        (1, [], [3, 1, 2]), (2, [1], [2, 3, 4]), (3, [4, 5, 8, 2], [3, 5, 10, 9, 4]),
        (1, [5], [1, 2, 3]), (4, [1, 2, 3, 4], [5, 6, 7]), (2, [-1, -2], [-3, 0, 1]),
        (5, list(range(10)), [11, 12, 13]), (3, [7, 7, 7], [7, 7]),
    ]])

add("implement-queue-using-stacks", [
    [["MyQueue"] + ops, [[]] + args]
    for ops, args in [
        (["push", "peek"], [[1], []]),
        (["push", "push", "pop", "peek"], [[1], [2], [], []]),
        (["push", "pop", "push", "pop", "empty"], [[1], [], [2], [], []]),
        (["push", "push", "push", "pop", "pop", "peek"], [[1], [2], [3], [], [], []]),
        (["empty", "push", "empty"], [[], [9], []]),
        (["push", "peek", "peek", "pop", "empty"], [[4], [], [], [], []]),
    ]])

add("implement-stack-using-queues", [
    [["MyStack"] + ops, [[]] + args]
    for ops, args in [
        (["push", "top"], [[1], []]),
        (["push", "push", "pop", "top"], [[1], [2], [], []]),
        (["push", "pop", "push", "pop", "empty"], [[1], [], [2], [], []]),
        (["push", "push", "push", "pop", "pop", "top"], [[1], [2], [3], [], [], []]),
        (["empty", "push", "empty"], [[], [9], []]),
        (["push", "top", "top", "pop", "empty"], [[4], [], [], [], []]),
    ]])

add("implement-stack-using-arrays", [
    [["ArrayStack"] + ops, [[cap]] + args]
    for cap, ops, args in [
        (1, ["push", "push", "top", "size"], [[1], [2], [], []]),
        (3, ["pop", "push", "pop", "pop"], [[], [7], [], []]),
        (2, ["push", "push", "pop", "push", "top"], [[1], [2], [], [3], []]),
        (5, ["size", "push", "size", "pop", "size"], [[], [4], [], [], []]),
        (1, ["push", "pop", "push", "top"], [[8], [], [9], []]),
    ]])

add("implement-queue-using-arrays", [
    [["ArrayQueue"] + ops, [[cap]] + args]
    for cap, ops, args in [
        (1, ["push", "push", "front", "size"], [[1], [2], [], []]),
        (3, ["pop", "push", "pop", "pop"], [[], [7], [], []]),
        (2, ["push", "push", "pop", "push", "front"], [[1], [2], [], [3], []]),
        (5, ["size", "push", "size", "pop", "size"], [[], [4], [], [], []]),
        (1, ["push", "pop", "push", "front"], [[8], [], [9], []]),
    ]])

add("lru-cache", [
    [["LRUCache"] + ops, [[cap]] + args]
    for cap, ops, args in [
        (1, ["put", "put", "get", "get"], [[1, 1], [2, 2], [1], [2]]),
        (2, ["put", "put", "put", "get", "get", "get"], [[1, 1], [2, 2], [3, 3], [1], [2], [3]]),
        (3, ["put", "get", "put", "get", "put", "get"], [[1, 1], [1], [2, 2], [1], [3, 3], [2]]),
        (1, ["get", "put", "get", "put", "get"], [[1], [1, 1], [1], [2, 2], [1]]),
        (2, ["put", "put", "get", "put", "get", "get"], [[1, 1], [1, 2], [1], [2, 2], [1], [2]]),
    ]])

add("lfu-cache", [
    [["LFUCache"] + ops, [[cap]] + args]
    for cap, ops, args in [
        (1, ["put", "put", "get", "get"], [[1, 1], [2, 2], [1], [2]]),
        (2, ["put", "put", "get", "put", "get", "get"], [[1, 1], [2, 2], [1], [3, 3], [2], [3]]),
        (2, ["put", "get", "get", "put", "put", "get", "get"],
         [[1, 1], [1], [1], [2, 2], [3, 3], [2], [3]]),
        (0, ["put", "get", "put", "get"], [[1, 1], [1], [2, 2], [2]]),
        (3, ["put", "put", "put", "get", "get", "put", "get"],
         [[1, 1], [2, 2], [3, 3], [1], [2], [4, 4], [3]]),
    ]])

add("maximum-xor-with-an-element-from-array", [
    [ints(n, 0, 10 ** 9, 31800 + i), [[x, m] for x, m in zip(
        expand(ints(q, 0, 10 ** 9, 31850 + i)), expand(ints(q, 0, 10 ** 9, 31900 + i)))]]
    for i, (n, q) in enumerate([(3, 2), (10, 5), (50, 25), (200, 100), (2000, 200),
                                (20000, 500), (100000, 800), (100000, 2000)])])
