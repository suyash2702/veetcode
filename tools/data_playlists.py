"""DSA sheets shipped with the extension.

A sheet is an ordered list of problem slugs grouped into sections. Sheets may
list problems this build does not bundle yet — the loader reports those as
"not bundled" rather than failing, so a full sheet can ship ahead of the
problems behind it.

Progress is stored per problem slug, never per sheet, so a problem that
appears in several sheets shows as solved in all of them.
"""

VEETCODE_STARTER = {
    "id": "veetcode-starter",
    "name": "VeetCode Starter",
    "kind": "curated",
    "order": 0,
    "author": "VeetCode",
    "description": "A first pass through the core patterns, easiest first — every problem here is bundled.",
    "sections": [
        {"name": "Arrays and Hashing", "slugs": [
            "two-sum", "contains-duplicate", "valid-anagram", "majority-element", "move-zeroes",
            "best-time-to-buy-and-sell-stock", "maximum-subarray", "product-of-array-except-self",
            "group-anagrams", "top-k-frequent-elements", "longest-consecutive-sequence",
        ]},
        {"name": "Two Pointers and Sliding Window", "slugs": [
            "merge-sorted-array", "3sum", "trapping-rain-water",
            "longest-substring-without-repeating-characters", "minimum-window-substring",
        ]},
        {"name": "Binary Search", "slugs": [
            "binary-search", "search-in-rotated-sorted-array", "kth-largest-element-in-an-array",
            "median-of-two-sorted-arrays",
        ]},
        {"name": "Stack and Strings", "slugs": [
            "valid-parentheses", "longest-palindromic-substring",
        ]},
        {"name": "Linked List", "slugs": [
            "reverse-linked-list", "merge-two-sorted-lists", "merge-k-sorted-lists",
        ]},
        {"name": "Trees", "slugs": [
            "maximum-depth-of-binary-tree", "invert-binary-tree",
            "binary-tree-level-order-traversal", "validate-binary-search-tree",
        ]},
        {"name": "Graphs", "slugs": [
            "number-of-islands", "course-schedule",
        ]},
        {"name": "Matrix", "slugs": [
            "spiral-matrix", "rotate-image", "word-search",
        ]},
        {"name": "Dynamic Programming", "slugs": [
            "climbing-stairs", "house-robber", "unique-paths", "coin-change", "word-break",
            "longest-increasing-subsequence", "edit-distance",
        ]},
    ],
}


BLIND_75 = {
    "id": "blind-75",
    "name": "Blind 75",
    "kind": "curated",
    "order": 1,
    "author": "Yangshun Tay",
    "description": "The 75-question list that covers every pattern interviews keep reusing.",
    "sections": [
        {"name": "Array", "slugs": [
            "two-sum", "best-time-to-buy-and-sell-stock", "contains-duplicate",
            "product-of-array-except-self", "maximum-subarray", "maximum-product-subarray",
            "find-minimum-in-rotated-sorted-array", "search-in-rotated-sorted-array",
            "3sum", "container-with-most-water",
        ]},
        {"name": "Binary", "slugs": [
            "sum-of-two-integers", "number-of-1-bits", "counting-bits", "missing-number",
            "reverse-bits",
        ]},
        {"name": "Dynamic Programming", "slugs": [
            "climbing-stairs", "coin-change", "longest-increasing-subsequence",
            "longest-common-subsequence", "word-break", "combination-sum-iv", "house-robber",
            "house-robber-ii", "decode-ways", "unique-paths", "jump-game",
        ]},
        {"name": "Graph", "slugs": [
            "clone-graph", "course-schedule", "pacific-atlantic-water-flow", "number-of-islands",
            "longest-consecutive-sequence", "alien-dictionary", "graph-valid-tree",
            "number-of-connected-components-in-an-undirected-graph",
        ]},
        {"name": "Interval", "slugs": [
            "insert-interval", "merge-intervals", "non-overlapping-intervals", "meeting-rooms",
            "meeting-rooms-ii",
        ]},
        {"name": "Linked List", "slugs": [
            "reverse-linked-list", "linked-list-cycle", "merge-two-sorted-lists",
            "merge-k-sorted-lists", "remove-nth-node-from-end-of-list", "reorder-list",
        ]},
        {"name": "Matrix", "slugs": [
            "set-matrix-zeroes", "spiral-matrix", "rotate-image", "word-search",
        ]},
        {"name": "String", "slugs": [
            "longest-substring-without-repeating-characters",
            "longest-repeating-character-replacement", "minimum-window-substring", "valid-anagram",
            "group-anagrams", "valid-parentheses", "valid-palindrome",
            "longest-palindromic-substring", "palindromic-substrings", "encode-and-decode-strings",
        ]},
        {"name": "Tree", "slugs": [
            "maximum-depth-of-binary-tree", "same-tree", "invert-binary-tree",
            "binary-tree-maximum-path-sum", "binary-tree-level-order-traversal",
            "serialize-and-deserialize-binary-tree", "subtree-of-another-tree",
            "construct-binary-tree-from-preorder-and-inorder-traversal",
            "validate-binary-search-tree", "kth-smallest-element-in-a-bst",
            "lowest-common-ancestor-of-a-binary-search-tree", "implement-trie-prefix-tree",
            "design-add-and-search-words-data-structure", "word-search-ii",
        ]},
        {"name": "Heap", "slugs": [
            "top-k-frequent-elements", "find-median-from-data-stream",
        ]},
    ],
}

STRIVER_SDE = {
    "id": "striver-sde",
    "name": "Striver SDE Sheet",
    "kind": "curated",
    "order": 2,
    "author": "Raj Vikramaditya (take U forward)",
    "description": "The SDE sheet's 27 coding days: arrays to graphs to DP, in the order it is meant to be done. Days 28-31 are OS/DBMS/CN/system-design theory and are not coding problems.",
    "sections": [
        {"name": "Day 1 — Arrays", "slugs": [
            "set-matrix-zeroes", "pascals-triangle", "next-permutation", "maximum-subarray",
            "sort-colors", "best-time-to-buy-and-sell-stock",
        ]},
        {"name": "Day 2 — Arrays II", "slugs": [
            "rotate-image", "merge-intervals", "merge-sorted-array", "find-the-duplicate-number",
            "missing-and-repeating-number", "count-inversions",
        ]},
        {"name": "Day 3 — Arrays III", "slugs": [
            "search-a-2d-matrix", "powx-n", "majority-element", "majority-element-ii",
            "unique-paths", "reverse-pairs",
        ]},
        {"name": "Day 4 — Arrays IV", "slugs": [
            "two-sum", "4sum", "longest-consecutive-sequence", "longest-subarray-with-sum-zero",
            "count-subarrays-with-given-xor", "longest-substring-without-repeating-characters",
        ]},
        {"name": "Day 5 — Linked List", "slugs": [
            "reverse-linked-list", "middle-of-the-linked-list", "merge-two-sorted-lists",
            "remove-nth-node-from-end-of-list", "add-two-numbers", "delete-node-in-a-linked-list",
        ]},
        {"name": "Day 6 — Linked List II", "slugs": [
            "intersection-of-two-linked-lists", "linked-list-cycle", "reverse-nodes-in-k-group",
            "palindrome-linked-list", "linked-list-cycle-ii", "flatten-a-linked-list",
        ]},
        {"name": "Day 7 — Linked List and Arrays", "slugs": [
            "rotate-list", "copy-list-with-random-pointer", "3sum", "trapping-rain-water",
            "remove-duplicates-from-sorted-array", "max-consecutive-ones",
        ]},
        {"name": "Day 8 — Greedy", "slugs": [
            "n-meetings-in-one-room", "minimum-platforms", "job-sequencing-problem",
            "fractional-knapsack", "minimum-coins", "assign-cookies",
        ]},
        {"name": "Day 9 — Recursion", "slugs": [
            "subset-sums", "subsets-ii", "combination-sum", "combination-sum-ii",
            "palindrome-partitioning", "permutation-sequence",
        ]},
        {"name": "Day 10 — Recursion and Backtracking", "slugs": [
            "permutations", "n-queens", "sudoku-solver", "m-coloring-problem", "rat-in-a-maze",
            "word-break-ii",
        ]},
        {"name": "Day 11 — Binary Search", "slugs": [
            "nth-root-of-a-number", "matrix-median", "single-element-in-a-sorted-array",
            "search-in-rotated-sorted-array", "median-of-two-sorted-arrays",
            "kth-element-of-two-sorted-arrays", "allocate-minimum-pages", "aggressive-cows",
        ]},
        {"name": "Day 12 — Heaps", "slugs": [
            "kth-largest-element-in-an-array", "maximum-sum-combinations",
            "find-median-from-data-stream", "merge-k-sorted-lists", "top-k-frequent-elements",
        ]},
        {"name": "Day 13 — Stack and Queue", "slugs": [
            "implement-stack-using-arrays", "implement-queue-using-arrays",
            "implement-stack-using-queues", "implement-queue-using-stacks", "valid-parentheses",
            "next-greater-element-i", "sort-a-stack",
        ]},
        {"name": "Day 14 — Stack and Queue II", "slugs": [
            "next-smaller-element", "lru-cache", "lfu-cache", "largest-rectangle-in-histogram",
            "sliding-window-maximum", "min-stack", "rotting-oranges", "online-stock-span",
            "maximum-of-minimum-every-window-size", "the-celebrity-problem",
        ]},
        {"name": "Day 15 — Strings", "slugs": [
            "reverse-words-in-a-string", "longest-palindromic-substring", "roman-to-integer",
            "string-to-integer-atoi", "longest-common-prefix", "rabin-karp",
        ]},
        {"name": "Day 16 — Strings II", "slugs": [
            "z-algorithm", "kmp-algorithm", "minimum-characters-for-palindrome", "valid-anagram",
            "count-and-say", "compare-version-numbers",
        ]},
        {"name": "Day 17 — Binary Tree", "slugs": [
            "binary-tree-inorder-traversal", "binary-tree-preorder-traversal",
            "binary-tree-postorder-traversal", "binary-tree-level-order-traversal",
            "binary-tree-maximum-path-sum", "diameter-of-binary-tree", "balanced-binary-tree",
            "lowest-common-ancestor-of-a-binary-tree", "same-tree",
            "binary-tree-zigzag-level-order-traversal", "boundary-traversal-of-binary-tree",
        ]},
        {"name": "Day 18 — Binary Tree II", "slugs": [
            "vertical-order-traversal-of-a-binary-tree", "top-view-of-binary-tree",
            "bottom-view-of-binary-tree", "binary-tree-right-side-view", "symmetric-tree",
        ]},
        {"name": "Day 19 — Binary Tree III", "slugs": [
            "root-to-node-path-in-binary-tree", "maximum-width-of-binary-tree",
            "children-sum-property", "all-nodes-distance-k-in-binary-tree",
            "minimum-time-to-burn-a-tree", "count-complete-tree-nodes",
            "construct-binary-tree-from-preorder-and-inorder-traversal",
            "construct-binary-tree-from-inorder-and-postorder-traversal",
            "serialize-and-deserialize-binary-tree", "flatten-binary-tree-to-linked-list",
        ]},
        {"name": "Day 20 — Binary Search Tree", "slugs": [
            "populating-next-right-pointers-in-each-node", "search-in-a-binary-search-tree",
            "convert-sorted-array-to-binary-search-tree", "construct-bst-from-preorder-traversal",
            "validate-binary-search-tree", "lowest-common-ancestor-of-a-binary-search-tree",
            "inorder-predecessor-and-successor",
        ]},
        {"name": "Day 21 — Binary Search Tree II", "slugs": [
            "floor-and-ceil-in-bst", "kth-smallest-element-in-a-bst", "two-sum-iv-input-is-a-bst",
            "binary-search-tree-iterator", "largest-bst-in-a-binary-tree",
            "maximum-sum-bst-in-binary-tree",
        ]},
        {"name": "Day 22 — Mixed", "slugs": [
            "binary-tree-to-doubly-linked-list", "kth-largest-element-in-a-stream",
            "distinct-numbers-in-every-window", "flood-fill", "morris-inorder-traversal",
        ]},
        {"name": "Day 23 — Graph", "slugs": [
            "clone-graph", "bfs-of-graph", "dfs-of-graph", "detect-cycle-in-undirected-graph",
            "detect-cycle-in-directed-graph", "topological-sort", "number-of-islands",
            "is-graph-bipartite",
        ]},
        {"name": "Day 24 — Graph II", "slugs": [
            "strongly-connected-components", "dijkstras-algorithm", "bellman-ford-algorithm",
            "floyd-warshall-algorithm", "minimum-spanning-tree-prims",
            "minimum-spanning-tree-kruskals",
        ]},
        {"name": "Day 25 — Dynamic Programming", "slugs": [
            "maximum-product-subarray", "longest-increasing-subsequence",
            "longest-common-subsequence", "0-1-knapsack", "edit-distance",
            "maximum-sum-increasing-subsequence", "matrix-chain-multiplication",
        ]},
        {"name": "Day 26 — Dynamic Programming II", "slugs": [
            "minimum-sum-partition", "count-subsets-with-given-sum", "coin-change",
            "subset-sum-equal-to-target", "rod-cutting", "egg-dropping", "word-break",
            "palindrome-partitioning-ii", "maximum-profit-in-job-scheduling",
        ]},
        {"name": "Day 27 — Trie", "slugs": [
            "implement-trie-prefix-tree", "implement-trie-ii", "longest-string-with-all-prefixes",
            "number-of-distinct-substrings", "power-set",
            "maximum-xor-of-two-numbers-in-an-array", "maximum-xor-with-an-element-from-array",
        ]},
    ],
}


# ------------------------------------------------------------- company lists
#
# Each company sheet draws only on problems the curated sheets above already
# list, so every slug resolves to the same problem — and to the same progress
# entry — no matter which sheet you reach it through.

COMPANIES = [
    ("google", "Google", 10, "Graph, string and interval questions Google keeps coming back to.", [
        "number-of-islands", "word-search-ii", "longest-substring-without-repeating-characters",
        "trapping-rain-water", "median-of-two-sorted-arrays", "merge-intervals", "insert-interval",
        "lru-cache", "minimum-window-substring", "decode-ways", "jump-game", "course-schedule",
        "alien-dictionary", "serialize-and-deserialize-binary-tree", "binary-tree-maximum-path-sum",
        "largest-rectangle-in-histogram", "sliding-window-maximum", "find-median-from-data-stream",
        "maximum-subarray", "coin-change", "edit-distance", "unique-paths", "spiral-matrix",
        "subsets-ii", "permutations", "combination-sum", "n-queens", "valid-parentheses",
        "longest-palindromic-substring", "palindromic-substrings", "top-k-frequent-elements",
        "pacific-atlantic-water-flow", "graph-valid-tree", "count-and-say",
    ]),
    ("amazon", "Amazon", 11, "The classic Amazon loop: data structures, BFS, and a lot of intervals.", [
        "two-sum", "lru-cache", "number-of-islands", "merge-intervals", "trapping-rain-water",
        "copy-list-with-random-pointer", "merge-k-sorted-lists", "top-k-frequent-elements",
        "kth-largest-element-in-an-array", "word-break", "valid-parentheses", "group-anagrams",
        "longest-substring-without-repeating-characters", "rotting-oranges", "course-schedule",
        "min-stack", "reorder-list", "best-time-to-buy-and-sell-stock",
        "product-of-array-except-self", "search-in-rotated-sorted-array", "3sum", "maximum-subarray",
        "coin-change", "unique-paths", "house-robber", "binary-tree-level-order-traversal",
        "lowest-common-ancestor-of-a-binary-tree", "validate-binary-search-tree",
        "serialize-and-deserialize-binary-tree", "subtree-of-another-tree",
        "implement-trie-prefix-tree", "design-add-and-search-words-data-structure",
        "find-median-from-data-stream", "sliding-window-maximum", "meeting-rooms-ii",
    ]),
    ("meta", "Meta", 12, "Fast, clean implementations — Meta interviews reward the second solution.", [
        "valid-palindrome", "minimum-window-substring", "merge-intervals",
        "binary-tree-right-side-view", "all-nodes-distance-k-in-binary-tree",
        "lowest-common-ancestor-of-a-binary-tree", "add-two-numbers",
        "remove-nth-node-from-end-of-list", "valid-parentheses", "3sum",
        "product-of-array-except-self", "kth-largest-element-in-an-array", "top-k-frequent-elements",
        "clone-graph", "number-of-islands", "course-schedule", "palindromic-substrings",
        "longest-palindromic-substring", "word-break", "decode-ways", "jump-game",
        "copy-list-with-random-pointer", "merge-k-sorted-lists",
        "serialize-and-deserialize-binary-tree", "binary-tree-maximum-path-sum",
        "validate-binary-search-tree", "kth-smallest-element-in-a-bst", "string-to-integer-atoi",
        "next-permutation", "sort-colors", "container-with-most-water", "insert-interval",
        "meeting-rooms-ii", "find-median-from-data-stream", "alien-dictionary",
    ]),
    ("microsoft", "Microsoft", 13, "Linked lists, matrices and trees, asked plainly.", [
        "reverse-linked-list", "linked-list-cycle", "merge-two-sorted-lists", "add-two-numbers",
        "valid-parentheses", "min-stack", "lru-cache", "spiral-matrix", "rotate-image",
        "set-matrix-zeroes", "search-a-2d-matrix", "two-sum", "3sum", "maximum-subarray",
        "best-time-to-buy-and-sell-stock", "longest-palindromic-substring", "valid-anagram",
        "group-anagrams", "roman-to-integer", "string-to-integer-atoi",
        "binary-tree-level-order-traversal", "binary-tree-zigzag-level-order-traversal",
        "validate-binary-search-tree", "lowest-common-ancestor-of-a-binary-search-tree",
        "invert-binary-tree", "symmetric-tree", "number-of-islands", "course-schedule",
        "coin-change", "climbing-stairs", "house-robber", "unique-paths", "edit-distance",
        "word-break", "implement-trie-prefix-tree",
    ]),
    ("apple", "Apple", 14, "Broad coverage with a bias toward clean data-structure work.", [
        "two-sum", "valid-parentheses", "merge-intervals", "lru-cache", "number-of-islands",
        "product-of-array-except-self", "maximum-subarray",
        "longest-substring-without-repeating-characters", "group-anagrams", "valid-anagram",
        "merge-two-sorted-lists", "reverse-linked-list", "linked-list-cycle",
        "binary-tree-level-order-traversal", "maximum-depth-of-binary-tree", "same-tree",
        "invert-binary-tree", "validate-binary-search-tree", "kth-largest-element-in-an-array",
        "top-k-frequent-elements", "coin-change", "climbing-stairs", "jump-game", "unique-paths",
        "spiral-matrix", "rotate-image", "trapping-rain-water", "container-with-most-water", "3sum",
        "search-in-rotated-sorted-array", "median-of-two-sorted-arrays", "min-stack",
        "implement-queue-using-stacks", "roman-to-integer", "longest-common-prefix",
    ]),
    ("flipkart", "Flipkart", 20, "Arrays, greedy and DP — the Indian product-company staple.", [
        "two-sum", "3sum", "4sum", "maximum-subarray", "sort-colors", "next-permutation",
        "merge-intervals", "minimum-platforms", "n-meetings-in-one-room", "job-sequencing-problem",
        "fractional-knapsack", "trapping-rain-water", "largest-rectangle-in-histogram",
        "sliding-window-maximum", "lru-cache", "min-stack", "number-of-islands",
        "detect-cycle-in-undirected-graph", "topological-sort", "coin-change", "0-1-knapsack",
        "longest-common-subsequence", "edit-distance", "longest-increasing-subsequence",
        "matrix-chain-multiplication", "find-the-duplicate-number", "count-inversions",
        "search-in-rotated-sorted-array", "allocate-minimum-pages", "aggressive-cows",
        "kth-largest-element-in-an-array", "merge-k-sorted-lists",
    ]),
    ("zomato", "Zomato", 21, "Hash maps, heaps and graph traversal on delivery-shaped problems.", [
        "two-sum", "group-anagrams", "valid-anagram", "top-k-frequent-elements",
        "kth-largest-element-in-an-array", "find-median-from-data-stream", "merge-intervals",
        "insert-interval", "meeting-rooms-ii", "number-of-islands", "rotting-oranges", "flood-fill",
        "clone-graph", "course-schedule", "dijkstras-algorithm", "minimum-spanning-tree-prims",
        "lru-cache", "min-stack", "valid-parentheses", "longest-substring-without-repeating-characters",
        "minimum-window-substring", "maximum-subarray", "best-time-to-buy-and-sell-stock",
        "coin-change", "climbing-stairs", "house-robber", "word-break", "implement-trie-prefix-tree",
        "binary-tree-level-order-traversal", "lowest-common-ancestor-of-a-binary-tree",
    ]),
    ("swiggy", "Swiggy", 22, "Scheduling, intervals and shortest paths.", [
        "n-meetings-in-one-room", "minimum-platforms", "job-sequencing-problem", "merge-intervals",
        "insert-interval", "non-overlapping-intervals", "meeting-rooms", "meeting-rooms-ii",
        "dijkstras-algorithm", "bellman-ford-algorithm", "floyd-warshall-algorithm",
        "topological-sort", "detect-cycle-in-directed-graph", "number-of-islands", "rotting-oranges",
        "two-sum", "3sum", "maximum-subarray", "product-of-array-except-self",
        "search-in-rotated-sorted-array", "median-of-two-sorted-arrays", "lru-cache", "lfu-cache",
        "sliding-window-maximum", "longest-substring-without-repeating-characters", "coin-change",
        "0-1-knapsack", "longest-increasing-subsequence", "word-break", "edit-distance",
    ]),
    ("razorpay", "Razorpay", 23, "Strings, hashing and correctness-heavy edge cases.", [
        "valid-parentheses", "valid-anagram", "group-anagrams", "longest-common-prefix",
        "roman-to-integer", "string-to-integer-atoi", "compare-version-numbers", "count-and-say",
        "reverse-words-in-a-string", "longest-palindromic-substring", "palindromic-substrings",
        "minimum-characters-for-palindrome", "rabin-karp", "kmp-algorithm", "two-sum",
        "longest-subarray-with-sum-zero", "count-subarrays-with-given-xor",
        "longest-consecutive-sequence", "lru-cache", "min-stack", "implement-queue-using-stacks",
        "implement-trie-prefix-tree", "number-of-distinct-substrings", "coin-change", "word-break",
        "climbing-stairs", "unique-paths", "binary-tree-inorder-traversal",
        "validate-binary-search-tree", "merge-intervals",
    ]),
    ("atlassian", "Atlassian", 24, "Design-flavoured questions plus solid tree and graph work.", [
        "lru-cache", "lfu-cache", "min-stack", "implement-trie-prefix-tree", "implement-trie-ii",
        "design-add-and-search-words-data-structure", "find-median-from-data-stream",
        "kth-largest-element-in-a-stream", "binary-search-tree-iterator", "merge-intervals",
        "insert-interval", "meeting-rooms-ii", "number-of-islands", "clone-graph",
        "course-schedule", "topological-sort", "is-graph-bipartite", "word-break",
        "longest-substring-without-repeating-characters", "minimum-window-substring",
        "group-anagrams", "top-k-frequent-elements", "serialize-and-deserialize-binary-tree",
        "binary-tree-right-side-view", "vertical-order-traversal-of-a-binary-tree",
        "lowest-common-ancestor-of-a-binary-tree", "validate-binary-search-tree", "coin-change",
        "unique-paths", "jump-game",
    ]),
    ("jane-street", "Jane Street", 30, "Sharp reasoning on arrays, probability-flavoured counting and clean recursion.", [
        "maximum-subarray", "maximum-product-subarray", "trapping-rain-water",
        "largest-rectangle-in-histogram", "sliding-window-maximum", "next-permutation",
        "reverse-pairs", "count-inversions", "median-of-two-sorted-arrays",
        "kth-element-of-two-sorted-arrays", "find-the-duplicate-number",
        "missing-and-repeating-number", "count-subarrays-with-given-xor",
        "maximum-xor-of-two-numbers-in-an-array", "counting-bits", "number-of-1-bits",
        "sum-of-two-integers", "powx-n", "permutations", "n-queens", "sudoku-solver",
        "subset-sums", "combination-sum", "0-1-knapsack", "matrix-chain-multiplication",
        "egg-dropping", "longest-increasing-subsequence", "edit-distance", "aggressive-cows",
        "allocate-minimum-pages",
    ]),
    ("citadel", "Citadel", 31, "Latency-shaped algorithms: heaps, monotonic stacks, and tight DP.", [
        "find-median-from-data-stream", "kth-largest-element-in-an-array",
        "kth-largest-element-in-a-stream", "top-k-frequent-elements", "merge-k-sorted-lists",
        "sliding-window-maximum", "maximum-of-minimum-every-window-size", "online-stock-span",
        "next-greater-element-i", "next-smaller-element", "largest-rectangle-in-histogram",
        "trapping-rain-water", "maximum-subarray", "maximum-product-subarray",
        "longest-increasing-subsequence", "maximum-sum-increasing-subsequence",
        "maximum-profit-in-job-scheduling", "job-sequencing-problem", "coin-change",
        "0-1-knapsack", "count-subsets-with-given-sum", "subset-sum-equal-to-target",
        "median-of-two-sorted-arrays", "search-in-rotated-sorted-array",
        "single-element-in-a-sorted-array", "nth-root-of-a-number", "matrix-median",
        "distinct-numbers-in-every-window", "lru-cache", "dijkstras-algorithm",
    ]),
    ("tower-research", "Tower Research", 32, "Low-level thinking: bit tricks, binary search, and exact math.", [
        "sum-of-two-integers", "number-of-1-bits", "counting-bits", "reverse-bits",
        "missing-number", "maximum-xor-of-two-numbers-in-an-array",
        "maximum-xor-with-an-element-from-array", "count-subarrays-with-given-xor", "powx-n",
        "nth-root-of-a-number", "single-element-in-a-sorted-array", "search-a-2d-matrix",
        "matrix-median", "median-of-two-sorted-arrays", "kth-element-of-two-sorted-arrays",
        "aggressive-cows", "allocate-minimum-pages", "reverse-pairs", "count-inversions",
        "find-the-duplicate-number", "trapping-rain-water", "largest-rectangle-in-histogram",
        "sliding-window-maximum", "maximum-subarray", "longest-increasing-subsequence",
        "0-1-knapsack", "rod-cutting", "egg-dropping", "matrix-chain-multiplication",
        "palindrome-partitioning-ii",
    ]),
    ("optiver", "Optiver", 33, "Speed round: array scans, stacks and shortest-path warm-ups.", [
        "two-sum", "maximum-subarray", "best-time-to-buy-and-sell-stock", "container-with-most-water",
        "trapping-rain-water", "next-greater-element-i", "online-stock-span", "min-stack",
        "sliding-window-maximum", "largest-rectangle-in-histogram",
        "longest-substring-without-repeating-characters", "longest-consecutive-sequence",
        "top-k-frequent-elements", "kth-largest-element-in-an-array", "find-median-from-data-stream",
        "merge-intervals", "insert-interval", "meeting-rooms-ii", "search-in-rotated-sorted-array",
        "median-of-two-sorted-arrays", "coin-change", "climbing-stairs", "house-robber",
        "jump-game", "unique-paths", "number-of-islands", "course-schedule", "clone-graph",
        "dijkstras-algorithm", "valid-parentheses",
    ]),
    ("uber", "Uber", 40, "Graphs, geometry-free routing and cache design.", [
        "number-of-islands", "clone-graph", "course-schedule", "topological-sort",
        "dijkstras-algorithm", "is-graph-bipartite", "detect-cycle-in-directed-graph",
        "graph-valid-tree", "number-of-connected-components-in-an-undirected-graph", "flood-fill",
        "rotting-oranges", "lru-cache", "lfu-cache", "min-stack", "merge-intervals",
        "insert-interval", "meeting-rooms-ii", "non-overlapping-intervals", "two-sum", "3sum",
        "group-anagrams", "longest-substring-without-repeating-characters", "minimum-window-substring",
        "word-break", "coin-change", "jump-game", "edit-distance", "top-k-frequent-elements",
        "find-median-from-data-stream", "serialize-and-deserialize-binary-tree",
    ]),
    ("airbnb", "Airbnb", 41, "String parsing, intervals and design-lite questions.", [
        "merge-intervals", "insert-interval", "non-overlapping-intervals", "meeting-rooms",
        "meeting-rooms-ii", "encode-and-decode-strings", "string-to-integer-atoi",
        "valid-parentheses", "valid-palindrome", "group-anagrams", "word-break", "word-break-ii",
        "palindrome-partitioning", "combination-sum", "subsets-ii", "permutations",
        "longest-substring-without-repeating-characters", "minimum-window-substring", "lru-cache",
        "implement-trie-prefix-tree", "design-add-and-search-words-data-structure",
        "number-of-islands", "clone-graph", "course-schedule", "alien-dictionary",
        "top-k-frequent-elements", "find-median-from-data-stream", "coin-change", "unique-paths",
        "maximum-subarray",
    ]),
    ("stripe", "Stripe", 42, "Correctness over cleverness: parsing, money-shaped DP, and idempotent design.", [
        "string-to-integer-atoi", "compare-version-numbers", "roman-to-integer",
        "longest-common-prefix", "valid-parentheses", "encode-and-decode-strings",
        "reverse-words-in-a-string", "group-anagrams", "valid-anagram", "two-sum",
        "longest-subarray-with-sum-zero", "count-subarrays-with-given-xor", "merge-intervals",
        "insert-interval", "coin-change", "minimum-coins", "0-1-knapsack",
        "subset-sum-equal-to-target", "count-subsets-with-given-sum", "word-break", "lru-cache",
        "lfu-cache", "min-stack", "implement-queue-using-stacks", "implement-trie-prefix-tree",
        "top-k-frequent-elements", "find-median-from-data-stream", "number-of-islands",
        "course-schedule", "climbing-stairs",
    ]),
    ("databricks", "Databricks", 43, "Systems-flavoured algorithms: streaming, partitioning and big graphs.", [
        "find-median-from-data-stream", "kth-largest-element-in-a-stream",
        "kth-largest-element-in-an-array", "top-k-frequent-elements", "merge-k-sorted-lists",
        "sliding-window-maximum", "distinct-numbers-in-every-window", "lru-cache", "lfu-cache",
        "implement-trie-prefix-tree", "design-add-and-search-words-data-structure",
        "serialize-and-deserialize-binary-tree", "number-of-islands", "clone-graph",
        "course-schedule", "topological-sort", "strongly-connected-components",
        "minimum-spanning-tree-kruskals", "dijkstras-algorithm", "number-of-connected-components-in-an-undirected-graph",
        "longest-consecutive-sequence", "group-anagrams", "word-break",
        "longest-substring-without-repeating-characters", "minimum-window-substring", "coin-change",
        "0-1-knapsack", "edit-distance", "longest-common-subsequence", "maximum-subarray",
    ]),
]


def company_playlists():
    """One sheet per company, sectioned by difficulty-agnostic study order."""
    out = []
    for company_id, name, order, description, slugs in COMPANIES:
        out.append({
            "id": "company-" + company_id,
            "name": name,
            "kind": "company",
            "order": order,
            "description": description,
            "sections": [{"name": "Most asked", "slugs": slugs}],
        })
    return out


PLAYLISTS = [VEETCODE_STARTER, BLIND_75, STRIVER_SDE] + company_playlists()
