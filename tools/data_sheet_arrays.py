"""Array, interval and string problems from the Blind 75 and SDE sheets."""

PROBLEMS = [
    {
        "id": 42,
        "slug": "set-matrix-zeroes",
        "title": "Set Matrix Zeroes",
        "difficulty": "Medium",
        "tags": ["Array", "Matrix", "Hash Table"],
        "complexity": "O(m * n) time, O(1) space",
        "functionName": "setZeroes",
        "params": ["matrix"],
        "checkArg": 0,
        "description": """
Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`. Do it in place.

**Constraints**

- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
""",
        "hints": [
            "Marking as you go corrupts the cells you have not read yet — collect the rows and columns first.",
            "The first row and first column can store those marks, which removes the extra O(m + n) space.",
        ],
        "tests": [
            {"input": [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]], "output": [[1, 0, 1], [0, 0, 0], [1, 0, 1]], "sample": True},
            {"input": [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]],
             "output": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], "sample": True},
            {"input": [[[1]]], "output": [[1]]},
            {"input": [[[0]]], "output": [[0]]},
        ],
    },
    {
        "id": 43,
        "slug": "pascals-triangle",
        "title": "Pascal's Triangle",
        "difficulty": "Easy",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n^2) time, O(n^2) space",
        "functionName": "generate",
        "params": ["numRows"],
        "description": """
Return the first `numRows` rows of Pascal's triangle. Each number is the sum of the two directly above it.

**Constraints**

- `1 <= numRows <= 34`
""",
        "hints": ["Row `i` starts and ends with 1; every inner value comes from the row above."],
        "tests": [
            {"input": [5], "output": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], "sample": True},
            {"input": [1], "output": [[1]], "sample": True},
            {"input": [2], "output": [[1], [1, 1]]},
        ],
    },
    {
        "id": 44,
        "slug": "next-permutation",
        "title": "Next Permutation",
        "difficulty": "Medium",
        "tags": ["Array", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "nextPermutation",
        "params": ["nums"],
        "checkArg": 0,
        "description": """
Rearrange `nums` into the next lexicographically greater permutation, in place. If no greater permutation exists, rearrange it into the lowest order (sorted ascending).

**Constraints**

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 100`
""",
        "hints": [
            "Scan from the right for the first index `i` with `nums[i] < nums[i + 1]` — everything after it is non-increasing.",
            "Swap `nums[i]` with the rightmost value greater than it, then reverse the suffix.",
        ],
        "tests": [
            {"input": [[1, 2, 3]], "output": [1, 3, 2], "sample": True},
            {"input": [[3, 2, 1]], "output": [1, 2, 3], "sample": True, "explanation": "Already the largest permutation."},
            {"input": [[1, 1, 5]], "output": [1, 5, 1]},
            {"input": [[1]], "output": [1]},
        ],
    },
    {
        "id": 45,
        "slug": "sort-colors",
        "title": "Sort Colors",
        "difficulty": "Medium",
        "tags": ["Array", "Two Pointers", "Sorting"],
        "complexity": "O(n) time, O(1) space, one pass",
        "functionName": "sortColors",
        "params": ["nums"],
        "checkArg": 0,
        "description": """
`nums` holds only `0`, `1` and `2`, representing red, white and blue. Sort them in place so equal colours are adjacent and ordered `0, 1, 2` — without using a library sort.

**Constraints**

- `1 <= nums.length <= 10^5`
- `nums[i]` is `0`, `1` or `2`
""",
        "hints": ["Dutch national flag: keep a low pointer for 0s, a high pointer for 2s, and scan with a third."],
        "tests": [
            {"input": [[2, 0, 2, 1, 1, 0]], "output": [0, 0, 1, 1, 2, 2], "sample": True},
            {"input": [[2, 0, 1]], "output": [0, 1, 2], "sample": True},
            {"input": [[0]], "output": [0]},
            {"input": [[2, 2, 2]], "output": [2, 2, 2]},
        ],
    },
    {
        "id": 46,
        "slug": "merge-intervals",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "tags": ["Array", "Sorting", "Interval"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "merge",
        "params": ["intervals"],
        "description": """
Given an array of intervals `[start, end]`, merge all overlapping intervals and return the non-overlapping intervals that cover all the input, sorted by start.

**Constraints**

- `1 <= intervals.length <= 10^5`
- `0 <= start <= end <= 10^6`
""",
        "hints": ["Sort by start, then extend the last kept interval whenever the next one starts before it ends."],
        "tests": [
            {"input": [[[1, 3], [2, 6], [8, 10], [15, 18]]], "output": [[1, 6], [8, 10], [15, 18]], "sample": True},
            {"input": [[[1, 4], [4, 5]]], "output": [[1, 5]], "sample": True, "explanation": "Touching intervals merge."},
            {"input": [[[1, 4], [0, 4]]], "output": [[0, 4]]},
            {"input": [[[1, 4], [2, 3]]], "output": [[1, 4]]},
        ],
    },
    {
        "id": 47,
        "slug": "insert-interval",
        "title": "Insert Interval",
        "difficulty": "Medium",
        "tags": ["Array", "Interval"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "insert",
        "params": ["intervals", "newInterval"],
        "description": """
`intervals` is sorted by start and holds no overlaps. Insert `newInterval`, merging where needed, and return the result — still sorted and overlap-free.

**Constraints**

- `0 <= intervals.length <= 10^5`
- `0 <= start <= end <= 10^6`
""",
        "hints": [
            "Three phases: intervals ending before the new one, intervals that overlap it, intervals starting after it.",
            "The overlapping run collapses into one interval spanning the minimum start and maximum end.",
        ],
        "tests": [
            {"input": [[[1, 3], [6, 9]], [2, 5]], "output": [[1, 5], [6, 9]], "sample": True},
            {"input": [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]],
             "output": [[1, 2], [3, 10], [12, 16]], "sample": True},
            {"input": [[], [5, 7]], "output": [[5, 7]]},
            {"input": [[[1, 5]], [2, 3]], "output": [[1, 5]]},
        ],
    },
    {
        "id": 48,
        "slug": "non-overlapping-intervals",
        "title": "Non-overlapping Intervals",
        "difficulty": "Medium",
        "tags": ["Array", "Greedy", "Interval"],
        "complexity": "O(n log n) time, O(1) space",
        "functionName": "eraseOverlapIntervals",
        "params": ["intervals"],
        "description": """
Return the minimum number of intervals to remove so that the rest do not overlap. Intervals that only touch at an endpoint do not overlap.

**Constraints**

- `1 <= intervals.length <= 10^5`
- `-10^6 <= start < end <= 10^6`
""",
        "hints": ["Sort by end. Greedily keep the interval that finishes earliest — it leaves the most room."],
        "tests": [
            {"input": [[[1, 2], [2, 3], [3, 4], [1, 3]]], "output": 1, "sample": True},
            {"input": [[[1, 2], [1, 2], [1, 2]]], "output": 2, "sample": True},
            {"input": [[[1, 2], [2, 3]]], "output": 0},
            {"input": [[[1, 100], [11, 22], [1, 11], [2, 12]]], "output": 2},
        ],
    },
    {
        "id": 49,
        "slug": "find-the-duplicate-number",
        "title": "Find the Duplicate Number",
        "difficulty": "Medium",
        "tags": ["Array", "Two Pointers", "Binary Search"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "findDuplicate",
        "params": ["nums"],
        "description": """
`nums` holds `n + 1` integers in the range `[1, n]`. Exactly one value is repeated (possibly many times). Return it without modifying the array and using constant extra space.

**Constraints**

- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= nums.length - 1`
""",
        "hints": [
            "`i -> nums[i]` is a function on indices; a repeated value means two indices land on the same place.",
            "That makes the sequence a linked list with a cycle — Floyd's tortoise and hare finds its entrance.",
        ],
        "tests": [
            {"input": [[1, 3, 4, 2, 2]], "output": 2, "sample": True},
            {"input": [[3, 1, 3, 4, 2]], "output": 3, "sample": True},
            {"input": [[1, 1]], "output": 1},
            {"input": [[2, 2, 2, 2, 2]], "output": 2},
        ],
    },
    {
        "id": 50,
        "slug": "missing-and-repeating-number",
        "title": "Missing and Repeating Number",
        "difficulty": "Medium",
        "tags": ["Array", "Math", "Bit Manipulation"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "findMissingRepeating",
        "params": ["nums"],
        "description": """
`nums` should hold every integer from `1` to `n` exactly once, but one value appears twice and another is missing. Return `[repeating, missing]`.

**Constraints**

- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= nums.length`
""",
        "hints": [
            "The difference of sums gives `repeating - missing`; the difference of squared sums gives `repeating + missing`.",
            "Two equations, two unknowns — no extra array needed.",
        ],
        "tests": [
            {"input": [[3, 1, 2, 5, 3]], "output": [3, 4], "sample": True},
            {"input": [[1, 1]], "output": [1, 2], "sample": True},
            {"input": [[2, 2]], "output": [2, 1]},
            {"input": [[4, 3, 6, 2, 1, 1]], "output": [1, 5]},
        ],
    },
    {
        "id": 51,
        "slug": "count-inversions",
        "title": "Count Inversions",
        "difficulty": "Hard",
        "tags": ["Array", "Divide and Conquer", "Merge Sort"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "countInversions",
        "params": ["nums"],
        "description": """
An inversion is a pair `i < j` with `nums[i] > nums[j]`. Return how many inversions `nums` contains — that is, how far it is from sorted.

**Constraints**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
""",
        "hints": [
            "The brute force is O(n^2); merge sort gets it to O(n log n).",
            "While merging, every time you take an element from the right half, it is smaller than all remaining left-half elements.",
        ],
        "tests": [
            {"input": [[2, 4, 1, 3, 5]], "output": 3, "sample": True},
            {"input": [[5, 4, 3, 2, 1]], "output": 10, "sample": True, "explanation": "Every pair is inverted."},
            {"input": [[1, 2, 3]], "output": 0},
            {"input": [[1]], "output": 0},
        ],
    },
    {
        "id": 52,
        "slug": "search-a-2d-matrix",
        "title": "Search a 2D Matrix",
        "difficulty": "Medium",
        "tags": ["Array", "Binary Search", "Matrix"],
        "complexity": "O(log(m * n)) time, O(1) space",
        "functionName": "searchMatrix",
        "params": ["matrix", "target"],
        "description": """
Each row of `matrix` is sorted ascending, and the first value of each row is greater than the last value of the row above. Return `true` if `target` is present.

**Constraints**

- `1 <= m, n <= 300`
- `-10^9 <= matrix[i][j], target <= 10^9`
""",
        "hints": ["Read the matrix as one sorted array of length `m * n` and binary search the index."],
        "tests": [
            {"input": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3], "output": True, "sample": True},
            {"input": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13], "output": False, "sample": True},
            {"input": [[[1]], 1], "output": True},
            {"input": [[[1]], 2], "output": False},
        ],
    },
    {
        "id": 53,
        "slug": "majority-element-ii",
        "title": "Majority Element II",
        "difficulty": "Medium",
        "tags": ["Array", "Hash Table", "Sorting"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "majorityElement",
        "params": ["nums"],
        "compare": "unordered",
        "description": """
Return every element that appears more than `n / 3` times, in any order.

**Constraints**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
""",
        "hints": [
            "At most two values can appear more than a third of the time.",
            "Extend Boyer-Moore voting to two candidates, then verify both with a second pass.",
        ],
        "tests": [
            {"input": [[3, 2, 3]], "output": [3], "sample": True},
            {"input": [[1, 1, 1, 3, 3, 2, 2, 2]], "output": [1, 2], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[1, 2]], "output": [1, 2]},
        ],
    },
    {
        "id": 54,
        "slug": "reverse-pairs",
        "title": "Reverse Pairs",
        "difficulty": "Hard",
        "tags": ["Array", "Divide and Conquer", "Merge Sort"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "reversePairs",
        "params": ["nums"],
        "description": """
Count the pairs `i < j` where `nums[i] > 2 * nums[j]`.

**Constraints**

- `1 <= nums.length <= 5 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
""",
        "hints": [
            "Same shape as counting inversions: split, count across the halves, then merge.",
            "With both halves sorted, a two-pointer sweep counts the pairs in linear time.",
        ],
        "tests": [
            {"input": [[1, 3, 2, 3, 1]], "output": 2, "sample": True},
            {"input": [[2, 4, 3, 5, 1]], "output": 3, "sample": True},
            {"input": [[1]], "output": 0},
            {"input": [[5, 4, 3, 2, 1]], "output": 4},
        ],
    },
    {
        "id": 55,
        "slug": "4sum",
        "title": "4Sum",
        "difficulty": "Medium",
        "tags": ["Array", "Two Pointers", "Sorting"],
        "complexity": "O(n^3) time, O(1) extra space",
        "functionName": "fourSum",
        "params": ["nums", "target"],
        "compare": "unordered2d",
        "description": """
Return all unique quadruplets `[a, b, c, d]` from `nums` that sum to `target`. The quadruplets may be returned in any order, but no quadruplet may repeat.

**Constraints**

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i], target <= 10^9`
""",
        "hints": [
            "Sort first — then two nested loops plus a two-pointer sweep covers every quadruplet in order.",
            "Skip equal neighbours at every level to keep the output free of duplicates.",
        ],
        "tests": [
            {"input": [[1, 0, -1, 0, -2, 2], 0], "output": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], "sample": True},
            {"input": [[2, 2, 2, 2, 2], 8], "output": [[2, 2, 2, 2]], "sample": True},
            {"input": [[1, 2, 3], 6], "output": []},
            {"input": [[0, 0, 0, 0], 0], "output": [[0, 0, 0, 0]]},
        ],
    },
    {
        "id": 56,
        "slug": "longest-subarray-with-sum-zero",
        "title": "Longest Subarray with Sum Zero",
        "difficulty": "Medium",
        "tags": ["Array", "Hash Table", "Prefix Sum"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "maxLen",
        "params": ["nums"],
        "description": """
Return the length of the longest contiguous subarray whose elements sum to `0`.

**Constraints**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
""",
        "hints": [
            "Two equal prefix sums mean the stretch between them sums to zero.",
            "Store the first index at which each prefix sum appears — the first one gives the longest span.",
        ],
        "tests": [
            {"input": [[15, -2, 2, -8, 1, 7, 10, 23]], "output": 5, "sample": True},
            {"input": [[1, 2, 3]], "output": 0, "sample": True},
            {"input": [[0]], "output": 1},
            {"input": [[1, -1, 1, -1]], "output": 4},
        ],
    },
    {
        "id": 57,
        "slug": "count-subarrays-with-given-xor",
        "title": "Count Subarrays with Given XOR",
        "difficulty": "Medium",
        "tags": ["Array", "Hash Table", "Bit Manipulation", "Prefix Sum"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "countSubarrays",
        "params": ["nums", "k"],
        "description": """
Count the contiguous subarrays whose XOR equals `k`.

**Constraints**

- `1 <= nums.length <= 10^5`
- `0 <= nums[i], k <= 10^9`
""",
        "hints": [
            "Prefix XOR: the XOR of `nums[i..j]` is `prefix[j] ^ prefix[i - 1]`.",
            "For each prefix `x`, the subarrays ending here with XOR `k` start where the prefix was `x ^ k`.",
        ],
        "tests": [
            {"input": [[4, 2, 2, 6, 4], 6], "output": 4, "sample": True},
            {"input": [[5, 6, 7, 8, 9], 5], "output": 2, "sample": True},
            {"input": [[1], 1], "output": 1},
            {"input": [[0, 0, 0], 0], "output": 6},
        ],
    },
    {
        "id": 58,
        "slug": "container-with-most-water",
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "tags": ["Array", "Two Pointers", "Greedy"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "maxArea",
        "params": ["height"],
        "description": """
`height[i]` is the height of a vertical line at position `i`. Pick two lines so the container they form with the x-axis holds the most water, and return that amount.

**Constraints**

- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`
""",
        "hints": [
            "Start with the widest pair and walk inwards.",
            "Moving the taller line can never help — the shorter one caps the area.",
        ],
        "tests": [
            {"input": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "output": 49, "sample": True},
            {"input": [[1, 1]], "output": 1, "sample": True},
            {"input": [[4, 3, 2, 1, 4]], "output": 16},
            {"input": [[1, 2, 1]], "output": 2},
        ],
    },
    {
        "id": 59,
        "slug": "max-consecutive-ones",
        "title": "Max Consecutive Ones",
        "difficulty": "Easy",
        "tags": ["Array"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "findMaxConsecutiveOnes",
        "params": ["nums"],
        "description": """
Given a binary array, return the length of the longest run of consecutive `1`s.

**Constraints**

- `1 <= nums.length <= 10^5`
- `nums[i]` is `0` or `1`
""",
        "hints": ["One counter for the current run, one for the best seen; reset on every zero."],
        "tests": [
            {"input": [[1, 1, 0, 1, 1, 1]], "output": 3, "sample": True},
            {"input": [[1, 0, 1, 1, 0, 1]], "output": 2, "sample": True},
            {"input": [[0]], "output": 0},
            {"input": [[1]], "output": 1},
        ],
    },
    {
        "id": 60,
        "slug": "remove-duplicates-from-sorted-array",
        "title": "Remove Duplicates from Sorted Array",
        "difficulty": "Easy",
        "tags": ["Array", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "removeDuplicates",
        "params": ["nums"],
        "description": """
`nums` is sorted ascending. Remove the duplicates in place so each value appears once, keeping the relative order, and return the number of unique values `k`.

Only the returned count is checked here, but write the unique values into the first `k` slots as the real problem asks.

**Constraints**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`, sorted ascending
""",
        "hints": ["A write pointer trails the read pointer and only advances on a new value."],
        "tests": [
            {"input": [[1, 1, 2]], "output": 2, "sample": True},
            {"input": [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], "output": 5, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[1, 1, 1]], "output": 1},
        ],
    },
    {
        "id": 61,
        "slug": "maximum-product-subarray",
        "title": "Maximum Product Subarray",
        "difficulty": "Medium",
        "tags": ["Array", "Dynamic Programming"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "maxProduct",
        "params": ["nums"],
        "description": """
Return the largest product of any contiguous subarray of `nums`. The answer fits in a 32-bit integer.

**Constraints**

- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
""",
        "hints": [
            "A large negative product becomes the best one as soon as another negative arrives.",
            "Track both the maximum and the minimum product ending at each index.",
        ],
        "tests": [
            {"input": [[2, 3, -2, 4]], "output": 6, "sample": True},
            {"input": [[-2, 0, -1]], "output": 0, "sample": True},
            {"input": [[-2]], "output": -2},
            {"input": [[-2, 3, -4]], "output": 24},
        ],
    },
    {
        "id": 62,
        "slug": "find-minimum-in-rotated-sorted-array",
        "title": "Find Minimum in Rotated Sorted Array",
        "difficulty": "Medium",
        "tags": ["Array", "Binary Search"],
        "complexity": "O(log n) time, O(1) space",
        "functionName": "findMin",
        "params": ["nums"],
        "description": """
`nums` holds distinct values, sorted ascending and then rotated some number of times. Return the minimum element in `O(log n)`.

**Constraints**

- `1 <= nums.length <= 5000`
- `-5000 <= nums[i] <= 5000`, all distinct
""",
        "hints": ["Compare the middle with the right end: it tells you which half still contains the rotation point."],
        "tests": [
            {"input": [[3, 4, 5, 1, 2]], "output": 1, "sample": True},
            {"input": [[4, 5, 6, 7, 0, 1, 2]], "output": 0, "sample": True},
            {"input": [[11, 13, 15, 17]], "output": 11},
            {"input": [[1]], "output": 1},
        ],
    },
    {
        "id": 63,
        "slug": "valid-palindrome",
        "title": "Valid Palindrome",
        "difficulty": "Easy",
        "tags": ["String", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "isPalindrome",
        "params": ["s"],
        "description": """
Ignoring case and every character that is not a letter or digit, decide whether `s` reads the same forwards and backwards.

**Constraints**

- `1 <= s.length <= 2 * 10^5`
- `s` holds printable ASCII
""",
        "hints": ["Two pointers walking inwards, each skipping non-alphanumeric characters."],
        "tests": [
            {"input": ["A man, a plan, a canal: Panama"], "output": True, "sample": True},
            {"input": ["race a car"], "output": False, "sample": True},
            {"input": [" "], "output": True},
            {"input": ["0P"], "output": False},
        ],
    },
    {
        "id": 64,
        "slug": "longest-common-prefix",
        "title": "Longest Common Prefix",
        "difficulty": "Easy",
        "tags": ["String"],
        "complexity": "O(total characters) time, O(1) space",
        "functionName": "longestCommonPrefix",
        "params": ["strs"],
        "description": """
Return the longest common prefix of every string in `strs`, or `""` when there is none.

**Constraints**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`, lowercase letters
""",
        "hints": ["Compare column by column and stop at the first mismatch or the first string that runs out."],
        "tests": [
            {"input": [["flower", "flow", "flight"]], "output": "fl", "sample": True},
            {"input": [["dog", "racecar", "car"]], "output": "", "sample": True},
            {"input": [["a"]], "output": "a"},
            {"input": [["", "b"]], "output": ""},
        ],
    },
    {
        "id": 65,
        "slug": "roman-to-integer",
        "title": "Roman to Integer",
        "difficulty": "Easy",
        "tags": ["String", "Hash Table", "Math"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "romanToInt",
        "params": ["s"],
        "description": """
Convert a Roman numeral to an integer. A smaller numeral placed before a larger one is subtracted (`IV` is 4, `CM` is 900).

**Constraints**

- `1 <= s.length <= 15`
- `s` is a valid Roman numeral in `[1, 3999]`
""",
        "hints": ["Walk left to right and subtract a value whenever the next one is larger."],
        "tests": [
            {"input": ["III"], "output": 3, "sample": True},
            {"input": ["MCMXCIV"], "output": 1994, "sample": True, "explanation": "M + CM + XC + IV."},
            {"input": ["LVIII"], "output": 58},
            {"input": ["IX"], "output": 9},
        ],
    },
    {
        "id": 66,
        "slug": "string-to-integer-atoi",
        "title": "String to Integer (atoi)",
        "difficulty": "Medium",
        "tags": ["String"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "myAtoi",
        "params": ["s"],
        "description": """
Convert `s` to a 32-bit signed integer: skip leading spaces, read an optional `+`/`-`, then read digits until a non-digit. Ignore the rest. If no digits were read, return `0`. Clamp the result to `[-2^31, 2^31 - 1]`.

**Constraints**

- `0 <= s.length <= 200`
- `s` holds printable ASCII
""",
        "hints": ["The clamp is the whole exercise — check the bound before it overflows, not after."],
        "tests": [
            {"input": ["42"], "output": 42, "sample": True},
            {"input": ["   -042"], "output": -42, "sample": True},
            {"input": ["1337c0d3"], "output": 1337},
            {"input": ["words and 987"], "output": 0},
            {"input": ["-91283472332"], "output": -2147483648},
        ],
    },
]
