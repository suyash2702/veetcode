"""Easy problem definitions."""

PROBLEMS = [
    {
        "id": 1,
        "slug": "two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "tags": ["Array", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "twoSum",
        "params": ["nums", "target"],
        "compare": "unordered",
        "description": """
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

Exactly one valid answer exists, and you may not use the same element twice. Return the indices in any order.

**Constraints**

- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i], target <= 10^9`
""",
        "hints": [
            "Brute force is two nested loops. What has to be true about `target - nums[i]`?",
            "Store every value you have seen in a hash map from value to index, then each lookup is O(1).",
        ],
        "tests": [
            {"input": [[2, 7, 11, 15], 9], "output": [0, 1], "sample": True, "explanation": "nums[0] + nums[1] == 9"},
            {"input": [[3, 2, 4], 6], "output": [1, 2], "sample": True},
            {"input": [[3, 3], 6], "output": [0, 1]},
            {"input": [[-1, -2, -3, -4, -5], -8], "output": [2, 4]},
            {"input": [[0, 4, 3, 0], 0], "output": [0, 3]},
            {"input": [[1000000000, 2, -1000000000], 0], "output": [0, 2]},
        ],
    },
    {
        "id": 2,
        "slug": "valid-parentheses",
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "tags": ["String", "Stack"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "isValid",
        "params": ["s"],
        "description": """
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, decide whether the input is valid.

A string is valid when every open bracket is closed by the same type of bracket, and brackets close in the correct order.

**Constraints**

- `1 <= s.length <= 2 * 10^5`
""",
        "hints": ["A closing bracket must match the most recently opened one — that is a stack."],
        "tests": [
            {"input": ["()"], "output": True, "sample": True},
            {"input": ["()[]{}"], "output": True, "sample": True},
            {"input": ["(]"], "output": False},
            {"input": ["([)]"], "output": False},
            {"input": ["{[]}"], "output": True},
            {"input": ["]"], "output": False},
            {"input": ["((("], "output": False},
            {"input": ["{[()()]}"], "output": True},
        ],
    },
    {
        "id": 3,
        "slug": "best-time-to-buy-and-sell-stock",
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "maxProfit",
        "params": ["prices"],
        "description": """
`prices[i]` is the price of a stock on day `i`. Buy on one day and sell on a later day to maximise profit.

Return the maximum profit you can achieve. If no profit is possible, return `0`.

**Constraints**

- `1 <= prices.length <= 2 * 10^5`
- `0 <= prices[i] <= 10^4`
""",
        "hints": ["Track the cheapest price seen so far while scanning left to right."],
        "tests": [
            {"input": [[7, 1, 5, 3, 6, 4]], "output": 5, "sample": True, "explanation": "Buy at 1, sell at 6."},
            {"input": [[7, 6, 4, 3, 1]], "output": 0, "sample": True, "explanation": "Prices only fall."},
            {"input": [[1]], "output": 0},
            {"input": [[2, 4, 1]], "output": 2},
            {"input": [[3, 3, 3, 3]], "output": 0},
            {"input": [[1, 2, 3, 4, 5]], "output": 4},
        ],
    },
    {
        "id": 4,
        "slug": "contains-duplicate",
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "tags": ["Array", "Hash Table", "Sorting"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "containsDuplicate",
        "params": ["nums"],
        "description": """
Return `true` if any value appears at least twice in `nums`, and `false` if every element is distinct.

**Constraints**

- `1 <= nums.length <= 2 * 10^5`
""",
        "tests": [
            {"input": [[1, 2, 3, 1]], "output": True, "sample": True},
            {"input": [[1, 2, 3, 4]], "output": False, "sample": True},
            {"input": [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], "output": True},
            {"input": [[0]], "output": False},
            {"input": [[-1, -1]], "output": True},
        ],
    },
    {
        "id": 5,
        "slug": "valid-anagram",
        "title": "Valid Anagram",
        "difficulty": "Easy",
        "tags": ["String", "Hash Table", "Sorting"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "isAnagram",
        "params": ["s", "t"],
        "description": """
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`.

An anagram uses exactly the same letters with the same multiplicities, in any order.

**Constraints**

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.
""",
        "tests": [
            {"input": ["anagram", "nagaram"], "output": True, "sample": True},
            {"input": ["rat", "car"], "output": False, "sample": True},
            {"input": ["a", "ab"], "output": False},
            {"input": ["aacc", "ccac"], "output": False},
            {"input": ["listen", "silent"], "output": True},
        ],
    },
    {
        "id": 6,
        "slug": "binary-search",
        "title": "Binary Search",
        "difficulty": "Easy",
        "tags": ["Array", "Binary Search"],
        "complexity": "O(log n) time, O(1) space",
        "functionName": "search",
        "params": ["nums", "target"],
        "description": """
Given a sorted array of distinct integers `nums` and an integer `target`, return the index of `target`, or `-1` if it is not present.

Your solution must run in `O(log n)` time.

**Constraints**

- `1 <= nums.length <= 10^5`
- `nums` is sorted in ascending order.
""",
        "hints": ["Keep a half-open window `[lo, hi)` and shrink it by half each step. Watch the loop condition."],
        "tests": [
            {"input": [[-1, 0, 3, 5, 9, 12], 9], "output": 4, "sample": True},
            {"input": [[-1, 0, 3, 5, 9, 12], 2], "output": -1, "sample": True},
            {"input": [[5], 5], "output": 0},
            {"input": [[5], -5], "output": -1},
            {"input": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1], "output": 0},
            {"input": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10], "output": 9},
        ],
    },
    {
        "id": 7,
        "slug": "maximum-subarray",
        "title": "Maximum Subarray",
        "difficulty": "Easy",
        "tags": ["Array", "Dynamic Programming", "Divide and Conquer"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "maxSubArray",
        "params": ["nums"],
        "description": """
Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

The subarray must contain at least one element.

**Constraints**

- `1 <= nums.length <= 2 * 10^5`
- `-10^4 <= nums[i] <= 10^4`
""",
        "hints": [
            "At each index, either extend the previous subarray or start a new one there.",
            "That decision is Kadane's algorithm: `best_ending_here = max(x, best_ending_here + x)`.",
        ],
        "tests": [
            {"input": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "output": 6, "sample": True, "explanation": "[4,-1,2,1] sums to 6."},
            {"input": [[1]], "output": 1, "sample": True},
            {"input": [[5, 4, -1, 7, 8]], "output": 23},
            {"input": [[-1]], "output": -1},
            {"input": [[-2, -1, -3]], "output": -1},
            {"input": [[8, -19, 5, -4, 20]], "output": 21},
        ],
    },
    {
        "id": 8,
        "slug": "climbing-stairs",
        "title": "Climbing Stairs",
        "difficulty": "Easy",
        "tags": ["Dynamic Programming", "Math"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "climbStairs",
        "params": ["n"],
        "description": """
You are climbing a staircase with `n` steps. Each move takes you 1 or 2 steps up.

In how many distinct ways can you reach the top?

**Constraints**

- `1 <= n <= 45`
""",
        "hints": ["Ways(n) only depends on Ways(n-1) and Ways(n-2). That is Fibonacci."],
        "tests": [
            {"input": [2], "output": 2, "sample": True, "explanation": "1+1 or 2."},
            {"input": [3], "output": 3, "sample": True},
            {"input": [1], "output": 1},
            {"input": [10], "output": 89},
            {"input": [45], "output": 1836311903},
        ],
    },
    {
        "id": 9,
        "slug": "move-zeroes",
        "title": "Move Zeroes",
        "difficulty": "Easy",
        "tags": ["Array", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "moveZeroes",
        "params": ["nums"],
        "checkArg": 0,
        "description": """
Move every `0` in `nums` to the end while keeping the relative order of the non-zero elements.

Modify `nums` **in place** — the checker inspects the array you were given, not your return value.

**Constraints**

- `1 <= nums.length <= 10^4`
""",
        "hints": ["Keep a write pointer for the next non-zero slot, then fill the tail with zeroes."],
        "tests": [
            {"input": [[0, 1, 0, 3, 12]], "output": [1, 3, 12, 0, 0], "sample": True},
            {"input": [[0]], "output": [0], "sample": True},
            {"input": [[1, 0]], "output": [1, 0]},
            {"input": [[0, 0, 1]], "output": [1, 0, 0]},
            {"input": [[4, 2, 4, 0, 0, 3, 0, 5, 1, 0]], "output": [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]},
        ],
    },
    {
        "id": 10,
        "slug": "merge-sorted-array",
        "title": "Merge Sorted Array",
        "difficulty": "Easy",
        "tags": ["Array", "Two Pointers", "Sorting"],
        "complexity": "O(m + n) time, O(1) space",
        "functionName": "merge",
        "params": ["nums1", "m", "nums2", "n"],
        "checkArg": 0,
        "description": """
`nums1` has length `m + n`: the first `m` slots hold sorted values and the last `n` slots are zero padding. `nums2` holds `n` sorted values.

Merge `nums2` into `nums1` **in place** so that `nums1` ends up sorted. The checker inspects `nums1`.

**Constraints**

- `0 <= m, n <= 1200`
- `m + n == nums1.length`
""",
        "hints": ["Filling from the front forces shifting. Fill from the back instead, largest first."],
        "tests": [
            {"input": [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], "output": [1, 2, 2, 3, 5, 6], "sample": True},
            {"input": [[1], 1, [], 0], "output": [1], "sample": True},
            {"input": [[0], 0, [1], 1], "output": [1]},
            {"input": [[4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3], "output": [1, 2, 3, 4, 5, 6]},
            {"input": [[-1, 3, 0, 0], 2, [-2, 2], 2], "output": [-2, -1, 2, 3]},
        ],
    },
    {
        "id": 11,
        "slug": "reverse-linked-list",
        "title": "Reverse Linked List",
        "difficulty": "Easy",
        "tags": ["Linked List", "Recursion"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "reverseList",
        "params": ["head"],
        "paramTypes": ["list"],
        "returnType": "list",
        "description": """
Reverse a singly linked list and return the new head.

`ListNode` is predefined for you (`val`, `next`); the test input is given to you as a real linked list and your returned list is serialised back to an array.

**Constraints**

- `0 <= list length <= 5000`
""",
        "hints": ["Walk the list carrying `prev`; rewire each node's `next` before advancing."],
        "tests": [
            {"input": [[1, 2, 3, 4, 5]], "output": [5, 4, 3, 2, 1], "sample": True},
            {"input": [[1, 2]], "output": [2, 1], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[7]], "output": [7]},
        ],
    },
    {
        "id": 12,
        "slug": "merge-two-sorted-lists",
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy",
        "tags": ["Linked List", "Recursion"],
        "complexity": "O(m + n) time, O(1) space",
        "functionName": "mergeTwoLists",
        "params": ["list1", "list2"],
        "paramTypes": ["list", "list"],
        "returnType": "list",
        "description": """
Merge two sorted linked lists into one sorted list, splicing the existing nodes together, and return its head.

`ListNode` is predefined for you.

**Constraints**

- Both lists are sorted ascending and hold at most 2000 nodes each.
""",
        "hints": ["A dummy head node removes every special case around the first element."],
        "tests": [
            {"input": [[1, 2, 4], [1, 3, 4]], "output": [1, 1, 2, 3, 4, 4], "sample": True},
            {"input": [[], []], "output": [], "sample": True},
            {"input": [[], [0]], "output": [0]},
            {"input": [[5], [1, 2, 3]], "output": [1, 2, 3, 5]},
            {"input": [[-9, 3], [5, 7]], "output": [-9, 3, 5, 7]},
        ],
    },
    {
        "id": 13,
        "slug": "invert-binary-tree",
        "title": "Invert Binary Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "DFS", "BFS"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "invertTree",
        "params": ["root"],
        "paramTypes": ["tree"],
        "returnType": "tree",
        "description": """
Invert a binary tree: swap the left and right child of every node, then return the root.

Trees are written as level-order arrays with `null` for missing children. `TreeNode` is predefined (`val`, `left`, `right`).

**Constraints**

- `0 <= number of nodes <= 2000`
""",
        "tests": [
            {"input": [[4, 2, 7, 1, 3, 6, 9]], "output": [4, 7, 2, 9, 6, 3, 1], "sample": True},
            {"input": [[2, 1, 3]], "output": [2, 3, 1], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1, None, 2]], "output": [1, 2]},
        ],
    },
    {
        "id": 14,
        "slug": "maximum-depth-of-binary-tree",
        "title": "Maximum Depth of Binary Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "DFS", "BFS"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "maxDepth",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the maximum depth of a binary tree — the number of nodes along the longest path from the root down to a leaf.

`TreeNode` is predefined for you.

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "tests": [
            {"input": [[3, 9, 20, None, None, 15, 7]], "output": 3, "sample": True},
            {"input": [[1, None, 2]], "output": 2, "sample": True},
            {"input": [[]], "output": 0},
            {"input": [[0]], "output": 1},
            {"input": [[1, 2, 3, 4, None, None, 5, 6]], "output": 4},
        ],
    },
    {
        "id": 15,
        "slug": "majority-element",
        "title": "Majority Element",
        "difficulty": "Easy",
        "tags": ["Array", "Hash Table", "Divide and Conquer"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "majorityElement",
        "params": ["nums"],
        "description": """
Return the element that appears more than `n / 2` times in `nums`. You may assume such an element always exists.

Bonus: solve it in `O(n)` time and `O(1)` extra space.

**Constraints**

- `1 <= nums.length <= 10^5`
""",
        "hints": ["Boyer-Moore voting: keep a candidate and a counter; matching votes add, differing votes cancel."],
        "tests": [
            {"input": [[3, 2, 3]], "output": 3, "sample": True},
            {"input": [[2, 2, 1, 1, 1, 2, 2]], "output": 2, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[6, 5, 5]], "output": 5},
            {"input": [[-1, -1, -1, 2, 2]], "output": -1},
        ],
    },
]
