"""Dynamic programming problems from the Blind 75 and SDE sheets."""

PROBLEMS = [
    {
        "id": 140,
        "slug": "longest-common-subsequence",
        "title": "Longest Common Subsequence",
        "difficulty": "Medium",
        "tags": ["String", "Dynamic Programming"],
        "complexity": "O(m * n) time, O(min(m, n)) space",
        "functionName": "longestCommonSubsequence",
        "params": ["text1", "text2"],
        "description": """
Return the length of the longest subsequence present in both strings. A subsequence keeps the order of characters but may skip any of them.

**Constraints**

- `1 <= text1.length, text2.length <= 1000`
- Lowercase English letters
""",
        "hints": [
            "`dp[i][j]` is the answer for the first `i` and `j` characters.",
            "Matching characters extend the diagonal; otherwise take the better of dropping one character.",
        ],
        "tests": [
            {"input": ["abcde", "ace"], "output": 3, "sample": True},
            {"input": ["abc", "abc"], "output": 3, "sample": True},
            {"input": ["abc", "def"], "output": 0},
            {"input": ["a", "a"], "output": 1},
        ],
    },
    {
        "id": 141,
        "slug": "0-1-knapsack",
        "title": "0/1 Knapsack",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n * capacity) time, O(capacity) space",
        "functionName": "knapsack",
        "params": ["weights", "values", "capacity"],
        "description": """
Each item may be taken once or left. Return the maximum total value that fits in a knapsack of the given capacity.

**Constraints**

- `1 <= n <= 1000`
- `1 <= weight[i], value[i] <= 1000`
- `1 <= capacity <= 1000`
""",
        "hints": [
            "`dp[c]` is the best value for capacity `c` using the items seen so far.",
            "Iterate capacities downwards so each item is used at most once.",
        ],
        "tests": [
            {"input": [[1, 3, 4, 5], [1, 4, 5, 7], 7], "output": 9, "sample": True},
            {"input": [[4, 5, 1], [1, 2, 3], 4], "output": 3, "sample": True},
            {"input": [[10], [100], 5], "output": 0},
            {"input": [[1, 1], [5, 6], 2], "output": 11},
        ],
    },
    {
        "id": 142,
        "slug": "subset-sum-equal-to-target",
        "title": "Subset Sum Equal to Target",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n * target) time, O(target) space",
        "functionName": "subsetSum",
        "params": ["nums", "target"],
        "description": """
Return whether some subset of `nums` sums to exactly `target`.

**Constraints**

- `1 <= nums.length <= 200`
- `0 <= nums[i] <= 1000`
- `0 <= target <= 10^4`
""",
        "hints": ["A boolean array over reachable sums, updated from the top down, is enough."],
        "tests": [
            {"input": [[3, 34, 4, 12, 5, 2], 9], "output": True, "sample": True},
            {"input": [[3, 34, 4, 12, 5, 2], 30], "output": False, "sample": True},
            {"input": [[1], 0], "output": True},
            {"input": [[2, 3], 5], "output": True},
        ],
    },
    {
        "id": 143,
        "slug": "count-subsets-with-given-sum",
        "title": "Count Subsets with Given Sum",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n * target) time, O(target) space",
        "functionName": "countSubsets",
        "params": ["nums", "target"],
        "description": """
Count the subsets of `nums` whose values sum to `target`. Subsets are counted by position, so equal values in different positions count separately, and the empty subset counts when `target` is `0`.

**Constraints**

- `1 <= nums.length <= 200`
- `0 <= nums[i] <= 1000`
- `0 <= target <= 10^4`
""",
        "hints": ["The same table as subset sum, but storing counts instead of booleans."],
        "tests": [
            {"input": [[1, 2, 3, 3], 6], "output": 3, "sample": True},
            {"input": [[1, 1, 1, 1], 1], "output": 4, "sample": True},
            {"input": [[0, 0, 1], 1], "output": 4, "explanation": "Each zero can be in or out."},
            {"input": [[2], 3], "output": 0},
        ],
    },
    {
        "id": 144,
        "slug": "minimum-sum-partition",
        "title": "Minimum Sum Partition",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n * sum) time, O(sum) space",
        "functionName": "minDifference",
        "params": ["nums"],
        "description": """
Split `nums` into two subsets and return the smallest possible absolute difference of their sums. Every element must land in one of the two subsets.

**Constraints**

- `1 <= nums.length <= 200`
- `0 <= nums[i] <= 500`
""",
        "hints": [
            "The two sums add up to the total, so one of them determines the difference.",
            "Find the reachable subset sum closest to half the total.",
        ],
        "tests": [
            {"input": [[1, 6, 11, 5]], "output": 1, "sample": True},
            {"input": [[1, 4]], "output": 3, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[2, 2]], "output": 0},
        ],
    },
    {
        "id": 145,
        "slug": "rod-cutting",
        "title": "Rod Cutting",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n^2) time, O(n) space",
        "functionName": "cutRod",
        "params": ["prices"],
        "description": """
`prices[i]` is what a piece of length `i + 1` sells for. Cut a rod of length `n = prices.length` into any number of pieces and return the largest total price.

**Constraints**

- `1 <= prices.length <= 1000`
- `1 <= prices[i] <= 10^5`
""",
        "hints": ["Unbounded knapsack: each length may be cut any number of times, so iterate lengths upwards."],
        "tests": [
            {"input": [[1, 5, 8, 9, 10, 17, 17, 20]], "output": 22, "sample": True},
            {"input": [[3, 5, 8, 9, 10, 17, 17, 20]], "output": 24, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[2, 3]], "output": 4},
        ],
    },
    {
        "id": 146,
        "slug": "egg-dropping",
        "title": "Egg Dropping",
        "difficulty": "Hard",
        "tags": ["Dynamic Programming", "Math"],
        "complexity": "O(eggs * floors) time, O(floors) space",
        "functionName": "eggDrop",
        "params": ["eggs", "floors"],
        "description": """
With `eggs` identical eggs and a building of `floors` floors, find the smallest number of drops that always determines the highest safe floor in the worst case. An egg that survives a drop can be reused; a broken one cannot.

**Constraints**

- `1 <= eggs <= 100`
- `1 <= floors <= 10^4`
""",
        "hints": [
            "The O(eggs * floors^2) recurrence over drop floors is the classic answer, but it is slow here.",
            "Flip the question: with `e` eggs and `d` drops, how many floors can you cover? Increase `d` until it reaches `floors`.",
        ],
        "tests": [
            {"input": [1, 2], "output": 2, "sample": True},
            {"input": [2, 10], "output": 4, "sample": True},
            {"input": [2, 100], "output": 14},
            {"input": [3, 14], "output": 4},
        ],
    },
    {
        "id": 147,
        "slug": "matrix-chain-multiplication",
        "title": "Matrix Chain Multiplication",
        "difficulty": "Hard",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n^3) time, O(n^2) space",
        "functionName": "matrixMultiplication",
        "params": ["dims"],
        "description": """
`dims` describes a chain of matrices: matrix `i` has shape `dims[i - 1] x dims[i]`. Return the fewest scalar multiplications needed to multiply the whole chain, choosing the parenthesisation.

**Constraints**

- `2 <= dims.length <= 200`
- `1 <= dims[i] <= 500`
""",
        "hints": [
            "`dp[i][j]` is the cost of the chain from `i` to `j`, split at every `k` between them.",
            "Fill by increasing chain length so the smaller pieces are already solved.",
        ],
        "tests": [
            {"input": [[40, 20, 30, 10, 30]], "output": 26000, "sample": True},
            {"input": [[10, 20, 30]], "output": 6000, "sample": True},
            {"input": [[1, 2]], "output": 0},
            {"input": [[10, 20, 30, 40]], "output": 18000},
        ],
    },
    {
        "id": 148,
        "slug": "palindrome-partitioning-ii",
        "title": "Palindrome Partitioning II",
        "difficulty": "Hard",
        "tags": ["String", "Dynamic Programming"],
        "complexity": "O(n^2) time, O(n^2) space",
        "functionName": "minCut",
        "params": ["s"],
        "description": """
Return the minimum number of cuts needed so that every piece of `s` is a palindrome.

**Constraints**

- `1 <= s.length <= 2000`
- Lowercase English letters
""",
        "hints": [
            "Precompute which substrings are palindromes — expanding around centres does it in O(n^2).",
            "Then `cuts[i]` is the best over every palindromic prefix ending at `i`.",
        ],
        "tests": [
            {"input": ["aab"], "output": 1, "sample": True},
            {"input": ["a"], "output": 0, "sample": True},
            {"input": ["ab"], "output": 1},
            {"input": ["abccba"], "output": 0},
        ],
    },
    {
        "id": 149,
        "slug": "maximum-sum-increasing-subsequence",
        "title": "Maximum Sum Increasing Subsequence",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n^2) time, O(n) space",
        "functionName": "maxSumIS",
        "params": ["nums"],
        "description": """
Return the largest sum of a strictly increasing subsequence of `nums`.

**Constraints**

- `1 <= nums.length <= 2000`
- `1 <= nums[i] <= 10^5`
""",
        "hints": ["Like the longest increasing subsequence, but each state stores the best sum ending there."],
        "tests": [
            {"input": [[1, 101, 2, 3, 100]], "output": 106, "sample": True},
            {"input": [[4, 1, 2, 3]], "output": 6, "sample": True},
            {"input": [[10]], "output": 10},
            {"input": [[5, 4, 3]], "output": 5},
        ],
    },
    {
        "id": 150,
        "slug": "maximum-profit-in-job-scheduling",
        "title": "Maximum Profit in Job Scheduling",
        "difficulty": "Hard",
        "tags": ["Array", "Dynamic Programming", "Binary Search", "Sorting"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "jobScheduling",
        "params": ["startTime", "endTime", "profit"],
        "description": """
Jobs may not overlap, though one may start exactly when another ends. Return the largest profit obtainable.

**Constraints**

- `1 <= n <= 5 * 10^4`
- `1 <= startTime[i] < endTime[i] <= 10^9`
- `1 <= profit[i] <= 10^4`
""",
        "hints": [
            "Sort by end time; `best[i]` is the most profit using only the first `i` jobs.",
            "Binary search for the last job that finishes by the current job's start.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], "output": 120, "sample": True},
            {"input": [[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]], "output": 150, "sample": True},
            {"input": [[1, 1, 1], [2, 3, 4], [5, 6, 4]], "output": 6},
            {"input": [[1], [2], [5]], "output": 5},
        ],
    },
    {
        "id": 151,
        "slug": "house-robber-ii",
        "title": "House Robber II",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "rob",
        "params": ["nums"],
        "description": """
The houses are arranged in a circle, so the first and the last are adjacent. Robbing two adjacent houses triggers the alarm. Return the most money you can take.

**Constraints**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`
""",
        "hints": ["Either the first house is skipped or the last is — run the linear version on both windows."],
        "tests": [
            {"input": [[2, 3, 2]], "output": 3, "sample": True},
            {"input": [[1, 2, 3, 1]], "output": 4, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[1, 2, 3]], "output": 3},
        ],
    },
    {
        "id": 152,
        "slug": "decode-ways",
        "title": "Decode Ways",
        "difficulty": "Medium",
        "tags": ["String", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "numDecodings",
        "params": ["s"],
        "description": """
`'A'` maps to `"1"` through `'Z'` to `"26"`. Return how many ways the digit string `s` can be decoded. A piece may not have a leading zero, so `"06"` is not a valid `'F'`.

**Constraints**

- `1 <= s.length <= 100`
- `s` holds digits only
""",
        "hints": [
            "Fibonacci-shaped: the count at `i` comes from taking one digit and from taking two.",
            "A `'0'` can only be decoded as part of `\"10\"` or `\"20\"`.",
        ],
        "tests": [
            {"input": ["12"], "output": 2, "sample": True},
            {"input": ["226"], "output": 3, "sample": True},
            {"input": ["06"], "output": 0},
            {"input": ["10"], "output": 1},
        ],
    },
    {
        "id": 153,
        "slug": "jump-game",
        "title": "Jump Game",
        "difficulty": "Medium",
        "tags": ["Array", "Greedy", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "canJump",
        "params": ["nums"],
        "description": """
`nums[i]` is the furthest you may jump from index `i`. Starting at index `0`, return whether the last index is reachable.

**Constraints**

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`
""",
        "hints": ["Track the furthest index reachable so far; failing to reach the current index ends the walk."],
        "tests": [
            {"input": [[2, 3, 1, 1, 4]], "output": True, "sample": True},
            {"input": [[3, 2, 1, 0, 4]], "output": False, "sample": True},
            {"input": [[0]], "output": True},
            {"input": [[1, 0, 1]], "output": False},
        ],
    },
    {
        "id": 154,
        "slug": "combination-sum-iv",
        "title": "Combination Sum IV",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(target * n) time, O(target) space",
        "functionName": "combinationSum4",
        "params": ["nums", "target"],
        "description": """
Count the ways to add up to `target` using values from `nums`, where each value may be reused and **different orders count as different combinations**.

**Constraints**

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 1000`, all distinct
- `1 <= target <= 1000`
""",
        "hints": [
            "Because order matters, the target loop must be on the outside and the values on the inside.",
            "Swapping those loops counts unordered combinations instead — a different problem.",
        ],
        "tests": [
            {"input": [[1, 2, 3], 4], "output": 7, "sample": True},
            {"input": [[9], 3], "output": 0, "sample": True},
            {"input": [[1], 5], "output": 1},
            {"input": [[2, 3], 6], "output": 2, "explanation": "2+2+2 and 3+3."},
        ],
    },
    {
        "id": 155,
        "slug": "palindromic-substrings",
        "title": "Palindromic Substrings",
        "difficulty": "Medium",
        "tags": ["String", "Dynamic Programming"],
        "complexity": "O(n^2) time, O(1) space",
        "functionName": "countSubstrings",
        "params": ["s"],
        "description": """
Count the palindromic substrings of `s`. Substrings at different positions count separately even when they read the same.

**Constraints**

- `1 <= s.length <= 1000`
- Lowercase English letters
""",
        "hints": ["Expand around each of the `2n - 1` centres and count every successful expansion."],
        "tests": [
            {"input": ["abc"], "output": 3, "sample": True},
            {"input": ["aaa"], "output": 6, "sample": True},
            {"input": ["a"], "output": 1},
            {"input": ["abba"], "output": 6},
        ],
    },
    {
        "id": 156,
        "slug": "longest-repeating-character-replacement",
        "title": "Longest Repeating Character Replacement",
        "difficulty": "Medium",
        "tags": ["String", "Sliding Window", "Hash Table"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "characterReplacement",
        "params": ["s", "k"],
        "description": """
You may change at most `k` characters of `s` to any uppercase letter. Return the length of the longest run of one repeated letter you can produce.

**Constraints**

- `1 <= s.length <= 10^5`
- `0 <= k <= s.length`
- Uppercase English letters
""",
        "hints": [
            "A window is valid when `length - countOfMostFrequentLetter <= k`.",
            "The window never needs to shrink by more than one step at a time.",
        ],
        "tests": [
            {"input": ["ABAB", 2], "output": 4, "sample": True},
            {"input": ["AABABBA", 1], "output": 4, "sample": True},
            {"input": ["A", 0], "output": 1},
            {"input": ["ABBB", 0], "output": 3},
        ],
    },
    {
        "id": 157,
        "slug": "word-break-ii",
        "title": "Word Break II",
        "difficulty": "Hard",
        "tags": ["String", "Dynamic Programming", "Backtracking", "Trie"],
        "complexity": "O(n^2 * number of sentences) time",
        "functionName": "wordBreak",
        "params": ["s", "wordDict"],
        "compare": "unordered",
        "description": """
Return every sentence that can be formed by splitting `s` into a sequence of dictionary words, each separated by one space. Words may be reused, and the sentences may be returned in any order.

**Constraints**

- `1 <= s.length <= 20`
- `1 <= wordDict.length <= 1000`
- `1 <= word length <= 10`, lowercase letters, all distinct
""",
        "hints": [
            "Recurse over prefixes and memoise on the start index, or the exponential cases explode.",
            "The memo maps a start index to every sentence for the rest of the string.",
        ],
        "tests": [
            {"input": ["catsanddog", ["cat", "cats", "and", "sand", "dog"]],
             "output": ["cats and dog", "cat sand dog"], "sample": True},
            {"input": ["pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]],
             "output": ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"], "sample": True},
            {"input": ["catsandog", ["cats", "dog", "sand", "and", "cat"]], "output": []},
            {"input": ["a", ["a"]], "output": ["a"]},
        ],
    },
    {
        "id": 158,
        "slug": "minimum-characters-for-palindrome",
        "title": "Minimum Characters to Add for Palindrome",
        "difficulty": "Hard",
        "tags": ["String", "String Matching"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "minCharsForPalindrome",
        "params": ["s"],
        "description": """
Return the fewest characters that must be added **at the front** of `s` to make it a palindrome.

**Constraints**

- `1 <= s.length <= 10^5`
- Lowercase English letters
""",
        "hints": [
            "The answer is `n` minus the longest palindromic prefix.",
            "Run the KMP failure function over `s + '#' + reverse(s)` to find that prefix in linear time.",
        ],
        "tests": [
            {"input": ["aacecaaa"], "output": 1, "sample": True},
            {"input": ["abcd"], "output": 3, "sample": True},
            {"input": ["a"], "output": 0},
            {"input": ["aabb"], "output": 2},
        ],
    },
    {
        "id": 159,
        "slug": "count-and-say",
        "title": "Count and Say",
        "difficulty": "Medium",
        "tags": ["String", "Recursion"],
        "complexity": "O(n * length of the answer) time",
        "functionName": "countAndSay",
        "params": ["n"],
        "description": """
The sequence starts at `"1"`, and each term describes the previous one by reading off runs: `"1"` becomes `"11"` (one 1), which becomes `"21"` (two 1s), then `"1211"`. Return the `n`-th term.

**Constraints**

- `1 <= n <= 30`
""",
        "hints": ["Build each term from the previous one by counting equal neighbours."],
        "tests": [
            {"input": [1], "output": "1", "sample": True},
            {"input": [4], "output": "1211", "sample": True},
            {"input": [5], "output": "111221"},
            {"input": [2], "output": "11"},
        ],
    },
]
