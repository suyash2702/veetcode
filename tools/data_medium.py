"""Medium problem definitions."""

PROBLEMS = [
    {
        "id": 16,
        "slug": "group-anagrams",
        "title": "Group Anagrams",
        "difficulty": "Medium",
        "tags": ["Array", "String", "Hash Table", "Sorting"],
        "complexity": "O(n * k log k) time",
        "functionName": "groupAnagrams",
        "params": ["strs"],
        "compare": "unordered2d",
        "description": """
Group the strings that are anagrams of each other.

Return a list of groups. The order of the groups, and the order of strings inside a group, does not matter.

**Constraints**

- `1 <= strs.length <= 10^4`
- `strs[i]` consists of lowercase English letters.
""",
        "hints": ["Every anagram class needs one canonical key — sorted letters, or a 26-slot count tuple."],
        "tests": [
            {
                "input": [["eat", "tea", "tan", "ate", "nat", "bat"]],
                "output": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
                "sample": True,
            },
            {"input": [[""]], "output": [[""]], "sample": True},
            {"input": [["a"]], "output": [["a"]]},
            {"input": [["abc", "bca", "cab", "xyz"]], "output": [["abc", "bca", "cab"], ["xyz"]]},
            {"input": [["ddddddddddg", "dgggggggggg"]], "output": [["ddddddddddg"], ["dgggggggggg"]]},
        ],
    },
    {
        "id": 17,
        "slug": "longest-substring-without-repeating-characters",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "tags": ["String", "Hash Table", "Sliding Window"],
        "complexity": "O(n) time, O(k) space",
        "functionName": "lengthOfLongestSubstring",
        "params": ["s"],
        "description": """
Given a string `s`, return the length of the longest substring that contains no repeated characters.

A substring is contiguous — `"pwke"` is a subsequence of `"pwwkew"`, not a substring.

**Constraints**

- `0 <= s.length <= 10^5`
""",
        "hints": [
            "Slide a window and keep the last index of every character.",
            "When you hit a repeat, jump the left edge past the previous occurrence — never move it backwards.",
        ],
        "tests": [
            {"input": ["abcabcbb"], "output": 3, "sample": True, "explanation": "\"abc\" has length 3."},
            {"input": ["bbbbb"], "output": 1, "sample": True},
            {"input": ["pwwkew"], "output": 3},
            {"input": [""], "output": 0},
            {"input": [" "], "output": 1},
            {"input": ["dvdf"], "output": 3},
            {"input": ["abba"], "output": 2},
        ],
    },
    {
        "id": 18,
        "slug": "product-of-array-except-self",
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "tags": ["Array", "Prefix Sum"],
        "complexity": "O(n) time, O(1) extra space",
        "functionName": "productExceptSelf",
        "params": ["nums"],
        "description": """
Return an array `answer` where `answer[i]` is the product of every element of `nums` except `nums[i]`.

Solve it without using division and in `O(n)` time.

**Constraints**

- `2 <= nums.length <= 10^5`
- The product of any prefix or suffix fits in a 32-bit integer.
""",
        "hints": ["answer[i] = (product of everything left of i) * (product of everything right of i)."],
        "tests": [
            {"input": [[1, 2, 3, 4]], "output": [24, 12, 8, 6], "sample": True},
            {"input": [[-1, 1, 0, -3, 3]], "output": [0, 0, 9, 0, 0], "sample": True},
            {"input": [[2, 3]], "output": [3, 2]},
            {"input": [[0, 0]], "output": [0, 0]},
            {"input": [[1, 1, 1, 1]], "output": [1, 1, 1, 1]},
            {"input": [[-1, -2, -3]], "output": [6, 3, 2]},
        ],
    },
    {
        "id": 19,
        "slug": "top-k-frequent-elements",
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "tags": ["Array", "Hash Table", "Heap", "Bucket Sort"],
        "complexity": "O(n) time with bucket sort",
        "functionName": "topKFrequent",
        "params": ["nums", "k"],
        "compare": "unordered",
        "description": """
Return the `k` most frequent elements of `nums`, in any order.

The answer is guaranteed to be unique.

**Constraints**

- `1 <= nums.length <= 10^5`
- `k` is between 1 and the number of distinct elements.
""",
        "hints": [
            "Count with a hash map first.",
            "Frequencies are bounded by n, so you can bucket by frequency instead of sorting.",
        ],
        "tests": [
            {"input": [[1, 1, 1, 2, 2, 3], 2], "output": [1, 2], "sample": True},
            {"input": [[1], 1], "output": [1], "sample": True},
            {"input": [[4, 4, 4, 5, 5, 6], 2], "output": [4, 5]},
            {"input": [[-1, -1, 2, 2, 3], 3], "output": [-1, 2, 3]},
            {"input": [[5, 5, 5, 5], 1], "output": [5]},
        ],
    },
    {
        "id": 20,
        "slug": "coin-change",
        "title": "Coin Change",
        "difficulty": "Medium",
        "tags": ["Dynamic Programming", "BFS"],
        "complexity": "O(amount * coins) time",
        "functionName": "coinChange",
        "params": ["coins", "amount"],
        "description": """
Given coin denominations `coins` and a target `amount`, return the fewest coins needed to make up that amount.

You have an infinite supply of each coin. If the amount cannot be made, return `-1`.

**Constraints**

- `1 <= coins.length <= 12`
- `0 <= amount <= 10^4`
""",
        "hints": [
            "Greedy fails: coins [1,3,4], amount 6 needs 3+3, not 4+1+1.",
            "dp[a] = 1 + min(dp[a - c]) over every coin c that fits.",
        ],
        "tests": [
            {"input": [[1, 2, 5], 11], "output": 3, "sample": True, "explanation": "11 = 5 + 5 + 1"},
            {"input": [[2], 3], "output": -1, "sample": True},
            {"input": [[1], 0], "output": 0},
            {"input": [[1, 3, 4], 6], "output": 2},
            {"input": [[186, 419, 83, 408], 6249], "output": 20},
            {"input": [[2, 5, 10, 1], 27], "output": 4},
        ],
    },
    {
        "id": 21,
        "slug": "number-of-islands",
        "title": "Number of Islands",
        "difficulty": "Medium",
        "tags": ["Graph", "DFS", "BFS", "Union Find", "Matrix"],
        "complexity": "O(m * n) time",
        "functionName": "numIslands",
        "params": ["grid"],
        "description": """
`grid` is an `m x n` map where `"1"` is land and `"0"` is water. Return the number of islands.

An island is land connected horizontally or vertically; the grid edges are surrounded by water.

**Constraints**

- `1 <= m, n <= 300`
- Cells are the strings `"0"` or `"1"`.
""",
        "hints": ["Scan for an unvisited '1', flood-fill the whole island, then count one."],
        "tests": [
            {
                "input": [[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]],
                "output": 1,
                "sample": True,
            },
            {
                "input": [[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]],
                "output": 3,
                "sample": True,
            },
            {"input": [[["0"]]], "output": 0},
            {"input": [[["1"]]], "output": 1},
            {"input": [[["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]], "output": 5},
        ],
    },
    {
        "id": 22,
        "slug": "course-schedule",
        "title": "Course Schedule",
        "difficulty": "Medium",
        "tags": ["Graph", "Topological Sort", "DFS", "BFS"],
        "complexity": "O(V + E) time",
        "functionName": "canFinish",
        "params": ["numCourses", "prerequisites"],
        "description": """
There are `numCourses` courses labelled `0` to `numCourses - 1`. `prerequisites[i] = [a, b]` means you must take `b` before `a`.

Return `true` if you can finish every course.

**Constraints**

- `1 <= numCourses <= 5000`
- `0 <= prerequisites.length <= 6000`
""",
        "hints": ["The answer is yes exactly when the directed graph has no cycle — Kahn's algorithm or a DFS colouring."],
        "tests": [
            {"input": [2, [[1, 0]]], "output": True, "sample": True},
            {"input": [2, [[1, 0], [0, 1]]], "output": False, "sample": True},
            {"input": [1, []], "output": True},
            {"input": [5, [[1, 4], [2, 4], [3, 1], [3, 2]]], "output": True},
            {"input": [3, [[0, 1], [1, 2], [2, 0]]], "output": False},
            {"input": [4, [[2, 0], [1, 0], [3, 1], [3, 2]]], "output": True},
        ],
    },
    {
        "id": 23,
        "slug": "3sum",
        "title": "3Sum",
        "difficulty": "Medium",
        "tags": ["Array", "Two Pointers", "Sorting"],
        "complexity": "O(n^2) time",
        "functionName": "threeSum",
        "params": ["nums"],
        "compare": "unordered2d",
        "description": """
Return every unique triplet `[nums[i], nums[j], nums[k]]` with distinct indices that sums to zero.

The solution set must not contain duplicate triplets. Order does not matter.

**Constraints**

- `3 <= nums.length <= 3000`
""",
        "hints": [
            "Sort first — then each fixed first element becomes a two-pointer scan of the rest.",
            "Skip over equal neighbours to avoid emitting the same triplet twice.",
        ],
        "tests": [
            {"input": [[-1, 0, 1, 2, -1, -4]], "output": [[-1, -1, 2], [-1, 0, 1]], "sample": True},
            {"input": [[0, 1, 1]], "output": [], "sample": True},
            {"input": [[0, 0, 0]], "output": [[0, 0, 0]]},
            {"input": [[0, 0, 0, 0]], "output": [[0, 0, 0]]},
            {"input": [[-2, 0, 1, 1, 2]], "output": [[-2, 0, 2], [-2, 1, 1]]},
        ],
    },
    {
        "id": 24,
        "slug": "search-in-rotated-sorted-array",
        "title": "Search in Rotated Sorted Array",
        "difficulty": "Medium",
        "tags": ["Array", "Binary Search"],
        "complexity": "O(log n) time",
        "functionName": "search",
        "params": ["nums", "target"],
        "description": """
`nums` was sorted ascending with distinct values, then rotated at some unknown pivot.

Return the index of `target`, or `-1`. Your solution must run in `O(log n)` time.

**Constraints**

- `1 <= nums.length <= 5000`
- Every value in `nums` is unique.
""",
        "hints": ["At every step at least one half is properly sorted — decide which, then test whether the target lies inside it."],
        "tests": [
            {"input": [[4, 5, 6, 7, 0, 1, 2], 0], "output": 4, "sample": True},
            {"input": [[4, 5, 6, 7, 0, 1, 2], 3], "output": -1, "sample": True},
            {"input": [[1], 0], "output": -1},
            {"input": [[1], 1], "output": 0},
            {"input": [[5, 1, 3], 3], "output": 2},
            {"input": [[3, 1], 1], "output": 1},
        ],
    },
    {
        "id": 25,
        "slug": "validate-binary-search-tree",
        "title": "Validate Binary Search Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "DFS", "Binary Search Tree"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "isValidBST",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return `true` if a binary tree is a valid binary search tree: every node in the left subtree is strictly smaller, every node in the right subtree is strictly larger, and both subtrees are themselves BSTs.

`TreeNode` is predefined for you.

**Constraints**

- `1 <= number of nodes <= 10^4`
""",
        "hints": [
            "Comparing each node only against its direct children is not enough — check the picture for [5,1,4,null,null,3,6].",
            "Carry an allowed (low, high) range down the recursion, or check that an in-order traversal is strictly increasing.",
        ],
        "tests": [
            {"input": [[2, 1, 3]], "output": True, "sample": True},
            {"input": [[5, 1, 4, None, None, 3, 6]], "output": False, "sample": True, "explanation": "3 sits right of 5 but is smaller."},
            {"input": [[1]], "output": True},
            {"input": [[2, 2, 2]], "output": False},
            {"input": [[5, 4, 6, None, None, 3, 7]], "output": False},
            {"input": [[10, 5, 15, 3, 7, 13, 20]], "output": True},
        ],
    },
    {
        "id": 26,
        "slug": "binary-tree-level-order-traversal",
        "title": "Binary Tree Level Order Traversal",
        "difficulty": "Medium",
        "tags": ["Tree", "BFS"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "levelOrder",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the values of a binary tree level by level, left to right, as a list of lists.

`TreeNode` is predefined for you.

**Constraints**

- `0 <= number of nodes <= 2000`
""",
        "hints": ["Process the queue one full level at a time: record its size before draining it."],
        "tests": [
            {"input": [[3, 9, 20, None, None, 15, 7]], "output": [[3], [9, 20], [15, 7]], "sample": True},
            {"input": [[1]], "output": [[1]], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1, 2, 3, 4, None, None, 5]], "output": [[1], [2, 3], [4, 5]]},
        ],
    },
    {
        "id": 27,
        "slug": "house-robber",
        "title": "House Robber",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "rob",
        "params": ["nums"],
        "description": """
Each house on a street holds `nums[i]` of loot, but robbing two adjacent houses triggers the alarm.

Return the maximum amount you can rob tonight.

**Constraints**

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 400`
""",
        "hints": ["At each house: skip it and keep the previous best, or take it plus the best from two houses back."],
        "tests": [
            {"input": [[1, 2, 3, 1]], "output": 4, "sample": True, "explanation": "Rob houses 0 and 2."},
            {"input": [[2, 7, 9, 3, 1]], "output": 12, "sample": True},
            {"input": [[5]], "output": 5},
            {"input": [[2, 1, 1, 2]], "output": 4},
            {"input": [[0, 0, 0]], "output": 0},
            {"input": [[100, 1, 1, 100]], "output": 200},
        ],
    },
    {
        "id": 28,
        "slug": "longest-consecutive-sequence",
        "title": "Longest Consecutive Sequence",
        "difficulty": "Medium",
        "tags": ["Array", "Hash Table", "Union Find"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "longestConsecutive",
        "params": ["nums"],
        "description": """
Return the length of the longest run of consecutive integers present in `nums` (the values need not be adjacent in the array).

Your solution must run in `O(n)` time.

**Constraints**

- `0 <= nums.length <= 10^5`
""",
        "hints": [
            "Put everything in a set.",
            "Only start counting upwards from values with no `x - 1` in the set — every run is then walked once.",
        ],
        "tests": [
            {"input": [[100, 4, 200, 1, 3, 2]], "output": 4, "sample": True, "explanation": "1,2,3,4"},
            {"input": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "output": 9, "sample": True},
            {"input": [[]], "output": 0},
            {"input": [[1, 1, 1]], "output": 1},
            {"input": [[-3, -2, -1, 5]], "output": 3},
        ],
    },
    {
        "id": 29,
        "slug": "word-break",
        "title": "Word Break",
        "difficulty": "Medium",
        "tags": ["String", "Dynamic Programming", "Trie"],
        "complexity": "O(n^2 * k) time",
        "functionName": "wordBreak",
        "params": ["s", "wordDict"],
        "description": """
Return `true` if `s` can be segmented into a sequence of one or more dictionary words. Words may be reused.

**Constraints**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
""",
        "hints": [
            "dp[i] = true when some word ends at position i and dp[start of that word] is also true.",
            "Plain recursion without memoisation blows up on inputs like \"aaaaaaa...b\".",
        ],
        "tests": [
            {"input": ["leetcode", ["leet", "code"]], "output": True, "sample": True},
            {"input": ["catsandog", ["cats", "dog", "sand", "and", "cat"]], "output": False, "sample": True},
            {"input": ["applepenapple", ["apple", "pen"]], "output": True},
            {"input": ["a", ["b"]], "output": False},
            {"input": ["aaaaaaaaaaaaaaaaaaaab", ["a", "aa", "aaa", "aaaa"]], "output": False},
            {"input": ["cars", ["car", "ca", "rs"]], "output": True},
        ],
    },
    {
        "id": 30,
        "slug": "spiral-matrix",
        "title": "Spiral Matrix",
        "difficulty": "Medium",
        "tags": ["Array", "Matrix", "Simulation"],
        "complexity": "O(m * n) time",
        "functionName": "spiralOrder",
        "params": ["matrix"],
        "description": """
Return all elements of an `m x n` matrix in spiral order: left to right along the top, down the right side, right to left along the bottom, up the left side, then inward.

**Constraints**

- `1 <= m, n <= 60`
""",
        "hints": ["Keep four boundaries and shrink one after each pass; stop as soon as they cross."],
        "tests": [
            {"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "output": [1, 2, 3, 6, 9, 8, 7, 4, 5], "sample": True},
            {"input": [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], "output": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "sample": True},
            {"input": [[[7]]], "output": [7]},
            {"input": [[[1, 2], [3, 4]]], "output": [1, 2, 4, 3]},
            {"input": [[[1], [2], [3]]], "output": [1, 2, 3]},
        ],
    },
    {
        "id": 31,
        "slug": "rotate-image",
        "title": "Rotate Image",
        "difficulty": "Medium",
        "tags": ["Array", "Matrix", "Math"],
        "complexity": "O(n^2) time, O(1) space",
        "functionName": "rotate",
        "params": ["matrix"],
        "checkArg": 0,
        "description": """
Rotate an `n x n` matrix 90 degrees clockwise **in place**. Do not allocate another matrix — the checker inspects the matrix you were given.

**Constraints**

- `1 <= n <= 60`
""",
        "hints": ["Transpose the matrix, then reverse every row."],
        "tests": [
            {"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "output": [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "sample": True},
            {
                "input": [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]],
                "output": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
                "sample": True,
            },
            {"input": [[[1]]], "output": [[1]]},
            {"input": [[[1, 2], [3, 4]]], "output": [[3, 1], [4, 2]]},
        ],
    },
    {
        "id": 32,
        "slug": "kth-largest-element-in-an-array",
        "title": "Kth Largest Element in an Array",
        "difficulty": "Medium",
        "tags": ["Array", "Heap", "Quickselect", "Sorting"],
        "complexity": "O(n) average with quickselect",
        "functionName": "findKthLargest",
        "params": ["nums", "k"],
        "description": """
Return the `k`-th largest element in `nums` — the `k`-th in sorted order, not the `k`-th distinct value.

**Constraints**

- `1 <= k <= nums.length <= 10^5`
""",
        "hints": ["A size-k min-heap keeps the k largest seen so far; quickselect gets you O(n) on average."],
        "tests": [
            {"input": [[3, 2, 1, 5, 6, 4], 2], "output": 5, "sample": True},
            {"input": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], "output": 4, "sample": True},
            {"input": [[1], 1], "output": 1},
            {"input": [[7, 7, 7], 3], "output": 7},
            {"input": [[-1, -5, 0], 1], "output": 0},
        ],
    },
    {
        "id": 33,
        "slug": "unique-paths",
        "title": "Unique Paths",
        "difficulty": "Medium",
        "tags": ["Dynamic Programming", "Math", "Combinatorics"],
        "complexity": "O(m * n) time, O(n) space",
        "functionName": "uniquePaths",
        "params": ["m", "n"],
        "description": """
A robot starts at the top-left corner of an `m x n` grid and can only move right or down. How many distinct paths reach the bottom-right corner?

**Constraints**

- `1 <= m, n <= 100`
""",
        "hints": ["paths[i][j] = paths[i-1][j] + paths[i][j-1]; one row of state is enough."],
        "tests": [
            {"input": [3, 7], "output": 28, "sample": True},
            {"input": [3, 2], "output": 3, "sample": True},
            {"input": [1, 1], "output": 1},
            {"input": [7, 3], "output": 28},
            {"input": [10, 10], "output": 48620},
        ],
    },
]
