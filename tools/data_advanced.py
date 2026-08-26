"""Harder problems: the medium-hard end of the ladder."""

PROBLEMS = [
    {
        "id": 34,
        "slug": "longest-palindromic-substring",
        "title": "Longest Palindromic Substring",
        "difficulty": "Medium",
        "tags": ["String", "Dynamic Programming", "Two Pointers"],
        "complexity": "O(n^2) time, O(1) space",
        "functionName": "longestPalindrome",
        "params": ["s"],
        "compare": "anyOf",
        "description": """
Return the longest palindromic substring of `s`. If several are equally long, returning any one of them is accepted.

**Constraints**

- `1 <= s.length <= 1000`
- `s` consists of digits and English letters.
""",
        "hints": [
            "Expand around every centre — there are 2n - 1 of them, odd and even.",
            "Manacher's algorithm gets this to O(n) if you want the challenge.",
        ],
        "tests": [
            {"input": ["babad"], "output": ["bab", "aba"], "sample": True, "explanation": "Either answer is accepted."},
            {"input": ["cbbd"], "output": ["bb"], "sample": True},
            {"input": ["a"], "output": ["a"]},
            {"input": ["ac"], "output": ["a", "c"]},
            {"input": ["racecarx"], "output": ["racecar"]},
            {"input": ["abbcccbbbcaaccbababcbcabca"], "output": ["bbcccbb"]},
        ],
    },
    {
        "id": 35,
        "slug": "word-search",
        "title": "Word Search",
        "difficulty": "Medium",
        "tags": ["Matrix", "Backtracking", "DFS"],
        "complexity": "O(m * n * 4^L) time",
        "functionName": "exist",
        "params": ["board", "word"],
        "description": """
Given an `m x n` grid of characters and a `word`, return `true` if the word can be spelled by walking through horizontally or vertically neighbouring cells.

The same cell may not be used twice in one path.

**Constraints**

- `1 <= m, n <= 12`
- `1 <= word.length <= 20`
""",
        "hints": ["Backtrack from every cell; mark a cell as used before recursing and restore it afterwards."],
        "tests": [
            {
                "input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
                "output": True,
                "sample": True,
            },
            {
                "input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"],
                "output": False,
                "sample": True,
                "explanation": "The B cell cannot be reused.",
            },
            {
                "input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
                "output": True,
            },
            {"input": [[["a"]], "a"], "output": True},
            {"input": [[["a", "b"], ["c", "d"]], "abcd"], "output": False},
        ],
    },
    {
        "id": 36,
        "slug": "longest-increasing-subsequence",
        "title": "Longest Increasing Subsequence",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming", "Binary Search"],
        "complexity": "O(n log n) time",
        "functionName": "lengthOfLIS",
        "params": ["nums"],
        "description": """
Return the length of the longest strictly increasing subsequence of `nums`.

A subsequence keeps the original order but may drop elements.

**Constraints**

- `1 <= nums.length <= 2500`
""",
        "hints": [
            "The O(n^2) DP is dp[i] = 1 + max(dp[j]) over j < i with nums[j] < nums[i].",
            "For O(n log n), keep the smallest possible tail for each length and binary search it.",
        ],
        "tests": [
            {"input": [[10, 9, 2, 5, 3, 7, 101, 18]], "output": 4, "sample": True, "explanation": "[2,3,7,101]"},
            {"input": [[0, 1, 0, 3, 2, 3]], "output": 4, "sample": True},
            {"input": [[7, 7, 7, 7, 7]], "output": 1},
            {"input": [[1]], "output": 1},
            {"input": [[4, 10, 4, 3, 8, 9]], "output": 3},
        ],
    },
    {
        "id": 37,
        "slug": "edit-distance",
        "title": "Edit Distance",
        "difficulty": "Medium",
        "tags": ["String", "Dynamic Programming"],
        "complexity": "O(m * n) time",
        "functionName": "minDistance",
        "params": ["word1", "word2"],
        "description": """
Return the minimum number of single-character insertions, deletions or replacements needed to turn `word1` into `word2`.

**Constraints**

- `0 <= word1.length, word2.length <= 500`
""",
        "hints": [
            "dp[i][j] is the distance between the first i characters of word1 and the first j of word2.",
            "Equal characters cost nothing; otherwise pay 1 plus the best of insert, delete or replace.",
        ],
        "tests": [
            {"input": ["horse", "ros"], "output": 3, "sample": True},
            {"input": ["intention", "execution"], "output": 5, "sample": True},
            {"input": ["", ""], "output": 0},
            {"input": ["", "abc"], "output": 3},
            {"input": ["same", "same"], "output": 0},
            {"input": ["plasma", "altruism"], "output": 6},
        ],
    },
    {
        "id": 38,
        "slug": "trapping-rain-water",
        "title": "Trapping Rain Water",
        "difficulty": "Hard",
        "tags": ["Array", "Two Pointers", "Stack", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "trap",
        "params": ["height"],
        "description": """
`height[i]` is the height of a bar of width 1. After it rains, how much water is trapped between the bars?

**Constraints**

- `1 <= height.length <= 2 * 10^4`
- `0 <= height[i] <= 10^5`
""",
        "hints": [
            "Water above bar i is min(max height to its left, max height to its right) - height[i].",
            "Two pointers moving inward from both ends compute that without storing the prefix arrays.",
        ],
        "tests": [
            {"input": [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], "output": 6, "sample": True},
            {"input": [[4, 2, 0, 3, 2, 5]], "output": 9, "sample": True},
            {"input": [[1]], "output": 0},
            {"input": [[3, 3, 3]], "output": 0},
            {"input": [[5, 0, 5]], "output": 5},
            {"input": [[2, 0, 2, 0, 2]], "output": 4},
        ],
    },
    {
        "id": 39,
        "slug": "median-of-two-sorted-arrays",
        "title": "Median of Two Sorted Arrays",
        "difficulty": "Hard",
        "tags": ["Array", "Binary Search", "Divide and Conquer"],
        "complexity": "O(log(min(m, n))) time",
        "functionName": "findMedianSortedArrays",
        "params": ["nums1", "nums2"],
        "compare": "approx",
        "description": """
Given two sorted arrays, return the median of their combined ordering.

The overall run time should be `O(log (m + n))`. Answers are compared with a tolerance, so returning `2` where `2.0` is expected is fine.

**Constraints**

- `0 <= m + n <= 2000`, and `m + n >= 1`.
""",
        "hints": [
            "Binary search the split point of the shorter array so both halves hold the same count.",
            "A partition is correct when maxLeft1 <= minRight2 and maxLeft2 <= minRight1.",
        ],
        "tests": [
            {"input": [[1, 3], [2]], "output": 2.0, "sample": True},
            {"input": [[1, 2], [3, 4]], "output": 2.5, "sample": True, "explanation": "(2 + 3) / 2"},
            {"input": [[], [1]], "output": 1.0},
            {"input": [[2], []], "output": 2.0},
            {"input": [[1, 1, 1], [1, 1]], "output": 1.0},
            {"input": [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]], "output": 6.0},
        ],
    },
    {
        "id": 40,
        "slug": "merge-k-sorted-lists",
        "title": "Merge k Sorted Lists",
        "difficulty": "Hard",
        "tags": ["Linked List", "Heap", "Divide and Conquer"],
        "complexity": "O(N log k) time",
        "functionName": "mergeKLists",
        "params": ["lists"],
        "paramTypes": ["list[]"],
        "returnType": "list",
        "description": """
You are given an array of `k` sorted linked lists. Merge them into one sorted list and return its head.

`ListNode` is predefined; `lists` arrives as an array of real linked lists.

**Constraints**

- `0 <= k <= 10^4`
- The total number of nodes is at most `10^4`.
""",
        "hints": [
            "A heap over the current heads gives O(N log k).",
            "Merging lists pairwise in rounds gets the same bound with no heap.",
        ],
        "tests": [
            {"input": [[[1, 4, 5], [1, 3, 4], [2, 6]]], "output": [1, 1, 2, 3, 4, 4, 5, 6], "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[[]]], "output": []},
            {"input": [[[], [1]]], "output": [1]},
            {"input": [[[-2, -1], [-3], [0, 5]]], "output": [-3, -2, -1, 0, 5]},
        ],
    },
    {
        "id": 41,
        "slug": "minimum-window-substring",
        "title": "Minimum Window Substring",
        "difficulty": "Hard",
        "tags": ["String", "Hash Table", "Sliding Window"],
        "complexity": "O(m + n) time",
        "functionName": "minWindow",
        "params": ["s", "t"],
        "description": """
Return the shortest substring of `s` that contains every character of `t`, including duplicates. If no such window exists, return `""`.

The answer is guaranteed to be unique.

**Constraints**

- `1 <= s.length, t.length <= 10^5`
""",
        "hints": [
            "Grow the window until it is valid, then shrink from the left while it stays valid.",
            "Track how many required characters are still missing instead of rescanning the counts.",
        ],
        "tests": [
            {"input": ["ADOBECODEBANC", "ABC"], "output": "BANC", "sample": True},
            {"input": ["a", "a"], "output": "a", "sample": True},
            {"input": ["a", "aa"], "output": ""},
            {"input": ["ab", "b"], "output": "b"},
            {"input": ["aaflslflsldkalskaaa", "aaa"], "output": "aaa"},
            {"input": ["bba", "ab"], "output": "ba"},
        ],
    },
]
