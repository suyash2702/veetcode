"""Bit manipulation, binary-search-on-answer and greedy problems from the sheets."""

PROBLEMS = [
    {
        "id": 120,
        "slug": "sum-of-two-integers",
        "title": "Sum of Two Integers",
        "difficulty": "Medium",
        "tags": ["Math", "Bit Manipulation"],
        "complexity": "O(1) time, O(1) space",
        "functionName": "getSum",
        "params": ["a", "b"],
        "description": """
Return `a + b` without using `+` or `-`.

**Constraints**

- `-1000 <= a, b <= 1000`
""",
        "hints": [
            "`a ^ b` adds without carrying; `(a & b) << 1` is the carry.",
            "Repeat until the carry is zero. In languages with big integers, mask to 32 bits and sign-extend at the end.",
        ],
        "tests": [
            {"input": [1, 2], "output": 3, "sample": True},
            {"input": [2, 3], "output": 5, "sample": True},
            {"input": [-1, 1], "output": 0},
            {"input": [-5, -7], "output": -12},
        ],
    },
    {
        "id": 121,
        "slug": "number-of-1-bits",
        "title": "Number of 1 Bits",
        "difficulty": "Easy",
        "tags": ["Bit Manipulation"],
        "complexity": "O(number of set bits) time, O(1) space",
        "functionName": "hammingWeight",
        "params": ["n"],
        "description": """
Return how many bits are set in the 32-bit unsigned integer `n`.

**Constraints**

- `0 <= n <= 2^32 - 1`
""",
        "hints": ["`n & (n - 1)` clears the lowest set bit, so the loop runs once per set bit."],
        "tests": [
            {"input": [11], "output": 3, "sample": True},
            {"input": [128], "output": 1, "sample": True},
            {"input": [4294967293], "output": 31},
            {"input": [0], "output": 0},
        ],
    },
    {
        "id": 122,
        "slug": "counting-bits",
        "title": "Counting Bits",
        "difficulty": "Easy",
        "tags": ["Dynamic Programming", "Bit Manipulation"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "countBits",
        "params": ["n"],
        "description": """
Return an array of length `n + 1` where entry `i` is the number of set bits in `i`.

**Constraints**

- `0 <= n <= 10^5`
""",
        "hints": ["`bits[i] = bits[i >> 1] + (i & 1)` — every number is a shifted smaller one plus its last bit."],
        "tests": [
            {"input": [2], "output": [0, 1, 1], "sample": True},
            {"input": [5], "output": [0, 1, 1, 2, 1, 2], "sample": True},
            {"input": [0], "output": [0]},
            {"input": [1], "output": [0, 1]},
        ],
    },
    {
        "id": 123,
        "slug": "reverse-bits",
        "title": "Reverse Bits",
        "difficulty": "Easy",
        "tags": ["Bit Manipulation"],
        "complexity": "O(1) time, O(1) space",
        "functionName": "reverseBits",
        "params": ["n"],
        "description": """
Reverse the bits of the 32-bit unsigned integer `n` and return the result.

**Constraints**

- `0 <= n <= 2^32 - 1`
""",
        "hints": ["Shift the answer left and push in the lowest bit of `n`, 32 times."],
        "tests": [
            {"input": [43261596], "output": 964176192, "sample": True},
            {"input": [4294967293], "output": 3221225471, "sample": True},
            {"input": [0], "output": 0},
            {"input": [1], "output": 2147483648},
        ],
    },
    {
        "id": 124,
        "slug": "missing-number",
        "title": "Missing Number",
        "difficulty": "Easy",
        "tags": ["Array", "Math", "Bit Manipulation"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "missingNumber",
        "params": ["nums"],
        "description": """
`nums` holds `n` distinct values taken from `[0, n]`. Return the one that is missing.

**Constraints**

- `1 <= nums.length <= 10^5`
- Values are distinct and in `[0, n]`
""",
        "hints": ["XOR every index and every value together — the pairs cancel and the missing number is left."],
        "tests": [
            {"input": [[3, 0, 1]], "output": 2, "sample": True},
            {"input": [[0, 1]], "output": 2, "sample": True},
            {"input": [[9, 6, 4, 2, 3, 5, 7, 0, 1]], "output": 8},
            {"input": [[0]], "output": 1},
        ],
    },
    {
        "id": 125,
        "slug": "powx-n",
        "title": "Pow(x, n)",
        "difficulty": "Medium",
        "tags": ["Math", "Recursion"],
        "complexity": "O(log n) time, O(1) space",
        "functionName": "myPow",
        "params": ["x", "n"],
        "compare": "approx",
        "description": """
Return `x` raised to the power `n`. A tolerance of `1e-5` is allowed.

**Constraints**

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- Either `x` is non-zero or `n > 0`
""",
        "hints": [
            "Square the base and halve the exponent — `x^n = (x^2)^(n/2)`.",
            "A negative exponent is the reciprocal of the positive one.",
        ],
        "tests": [
            {"input": [2.0, 10], "output": 1024.0, "sample": True},
            {"input": [2.1, 3], "output": 9.261, "sample": True},
            {"input": [2.0, -2], "output": 0.25},
            {"input": [1.0, 2147483647], "output": 1.0},
        ],
    },
    {
        "id": 126,
        "slug": "nth-root-of-a-number",
        "title": "Nth Root of a Number",
        "difficulty": "Medium",
        "tags": ["Math", "Binary Search"],
        "complexity": "O(n log m) time, O(1) space",
        "functionName": "nthRoot",
        "params": ["n", "m"],
        "description": """
Return the integer `k` with `k^n == m`, or `-1` when `m` is not a perfect `n`-th power.

**Constraints**

- `1 <= n <= 30`
- `1 <= m <= 10^9`
""",
        "hints": [
            "Binary search `k` in `[1, m]` and compare `k^n` with `m`.",
            "Stop multiplying as soon as the running power passes `m`, or it will overflow in some languages.",
        ],
        "tests": [
            {"input": [3, 27], "output": 3, "sample": True},
            {"input": [4, 69], "output": -1, "sample": True},
            {"input": [2, 100], "output": 10},
            {"input": [1, 7], "output": 7},
        ],
    },
    {
        "id": 127,
        "slug": "single-element-in-a-sorted-array",
        "title": "Single Element in a Sorted Array",
        "difficulty": "Medium",
        "tags": ["Array", "Binary Search"],
        "complexity": "O(log n) time, O(1) space",
        "functionName": "singleNonDuplicate",
        "params": ["nums"],
        "description": """
Every value in the sorted array appears exactly twice, except one that appears once. Return it in `O(log n)`.

**Constraints**

- `1 <= nums.length <= 10^5`, odd
- `0 <= nums[i] <= 10^5`, sorted ascending
""",
        "hints": [
            "Before the single element, pairs start at even indices; after it, they start at odd ones.",
            "Binary search on that parity to find where the pattern breaks.",
        ],
        "tests": [
            {"input": [[1, 1, 2, 3, 3, 4, 4, 8, 8]], "output": 2, "sample": True},
            {"input": [[3, 3, 7, 7, 10, 11, 11]], "output": 10, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[1, 1, 2]], "output": 2},
        ],
    },
    {
        "id": 128,
        "slug": "kth-element-of-two-sorted-arrays",
        "title": "Kth Element of Two Sorted Arrays",
        "difficulty": "Hard",
        "tags": ["Array", "Binary Search", "Divide and Conquer"],
        "complexity": "O(log(min(m, n))) time, O(1) space",
        "functionName": "kthElement",
        "params": ["a", "b", "k"],
        "description": """
Both arrays are sorted ascending. Return the `k`-th smallest value of their union (1-indexed).

**Constraints**

- `0 <= a.length, b.length <= 10^5`
- `1 <= k <= a.length + b.length`
- `-10^9 <= values <= 10^9`
""",
        "hints": [
            "Merging is O(k); the interview answer binary searches the split point in the shorter array.",
            "A split is correct when both left halves stay below both right halves.",
        ],
        "tests": [
            {"input": [[2, 3, 6, 7, 9], [1, 4, 8, 10], 5], "output": 6, "sample": True},
            {"input": [[100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7], "output": 256, "sample": True},
            {"input": [[], [1, 2, 3], 2], "output": 2},
            {"input": [[1], [2], 2], "output": 2},
        ],
    },
    {
        "id": 129,
        "slug": "allocate-minimum-pages",
        "title": "Allocate Minimum Number of Pages",
        "difficulty": "Hard",
        "tags": ["Array", "Binary Search", "Greedy"],
        "complexity": "O(n log(sum)) time, O(1) space",
        "functionName": "findPages",
        "params": ["books", "students"],
        "description": """
`books[i]` is the page count of book `i`. Hand the books out to `students` readers so that each reader gets a **contiguous** block and every book is given out. Return the smallest possible value of the largest block, or `-1` when there are fewer books than readers.

**Constraints**

- `1 <= books.length <= 10^5`
- `1 <= books[i] <= 10^4`
- `1 <= students <= 10^5`
""",
        "hints": [
            "Binary search the answer between the largest single book and the total.",
            "For a candidate limit, greedily fill readers and count how many you need.",
        ],
        "tests": [
            {"input": [[12, 34, 67, 90], 2], "output": 113, "sample": True},
            {"input": [[15, 17, 20], 2], "output": 32, "sample": True},
            {"input": [[10, 20], 3], "output": -1},
            {"input": [[5], 1], "output": 5},
        ],
    },
    {
        "id": 130,
        "slug": "aggressive-cows",
        "title": "Aggressive Cows",
        "difficulty": "Hard",
        "tags": ["Array", "Binary Search", "Greedy"],
        "complexity": "O(n log(max)) time, O(1) space",
        "functionName": "aggressiveCows",
        "params": ["stalls", "cows"],
        "description": """
`stalls` holds the positions of stalls along a line. Place `cows` cows in distinct stalls so that the smallest distance between any two of them is as large as possible, and return that distance.

**Constraints**

- `2 <= stalls.length <= 10^5`
- `2 <= cows <= stalls.length`
- `0 <= position <= 10^9`
""",
        "hints": [
            "Sort the stalls, then binary search the answer: can the cows be placed at least `d` apart?",
            "Checking a distance is a greedy left-to-right sweep.",
        ],
        "tests": [
            {"input": [[1, 2, 4, 8, 9], 3], "output": 3, "sample": True},
            {"input": [[10, 1, 2, 7, 5], 3], "output": 4, "sample": True},
            {"input": [[1, 2], 2], "output": 1},
            {"input": [[0, 3, 4, 7, 10, 9], 4], "output": 3},
        ],
    },
    {
        "id": 131,
        "slug": "matrix-median",
        "title": "Matrix Median",
        "difficulty": "Hard",
        "tags": ["Array", "Binary Search", "Matrix"],
        "complexity": "O(32 * r * log c) time, O(1) space",
        "functionName": "matrixMedian",
        "params": ["matrix"],
        "description": """
Every row of the matrix is sorted ascending, and `r * c` is odd. Return the median of all the values without building the flattened array.

**Constraints**

- `1 <= r, c <= 300`
- `r * c` is odd
- `1 <= matrix[i][j] <= 10^9`
""",
        "hints": [
            "Binary search the value, not the index: count how many entries are `<= mid`.",
            "Counting in a sorted row is one upper-bound search each.",
        ],
        "tests": [
            {"input": [[[1, 3, 5], [2, 6, 9], [3, 6, 9]]], "output": 5, "sample": True},
            {"input": [[[1, 5, 7, 9, 11], [1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]], "output": 5, "sample": True},
            {"input": [[[1]]], "output": 1},
            {"input": [[[1, 2, 3]]], "output": 2},
        ],
    },
    {
        "id": 132,
        "slug": "n-meetings-in-one-room",
        "title": "N Meetings in One Room",
        "difficulty": "Easy",
        "tags": ["Array", "Greedy", "Sorting"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "maxMeetings",
        "params": ["start", "end"],
        "description": """
One room, `n` meetings with start and end times. A meeting can begin only **strictly after** the previous one has finished, so a meeting starting exactly when another ends cannot follow it. Return the largest number of meetings that fit.

**Constraints**

- `1 <= n <= 10^5`
- `0 <= start[i] < end[i] <= 10^9`
""",
        "hints": ["Sort by finishing time and take every meeting that starts after the last one ended."],
        "tests": [
            {"input": [[1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]], "output": 4, "sample": True},
            {"input": [[10, 12, 20], [20, 25, 30]], "output": 1, "sample": True},
            {"input": [[1], [2]], "output": 1},
            {"input": [[1, 2, 3], [2, 3, 4]], "output": 2, "explanation": "The meeting starting at 2 cannot follow one ending at 2."},
        ],
    },
    {
        "id": 133,
        "slug": "minimum-platforms",
        "title": "Minimum Platforms",
        "difficulty": "Medium",
        "tags": ["Array", "Greedy", "Sorting"],
        "complexity": "O(n log n) time, O(1) space",
        "functionName": "findPlatform",
        "params": ["arrival", "departure"],
        "description": """
Given the arrival and departure times of trains at a station, return the fewest platforms needed so no train waits. A train departing at the same moment another arrives still occupies its platform.

**Constraints**

- `1 <= n <= 10^5`
- `0 <= arrival[i] <= departure[i] <= 10^9`
""",
        "hints": [
            "Sort arrivals and departures separately and sweep them like a merge.",
            "Every arrival before the next departure needs one more platform.",
        ],
        "tests": [
            {"input": [[900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]],
             "output": 3, "sample": True},
            {"input": [[900, 1100, 1235], [1000, 1200, 1240]], "output": 1, "sample": True},
            {"input": [[1], [2]], "output": 1},
            {"input": [[1, 1, 1], [2, 2, 2]], "output": 3},
        ],
    },
    {
        "id": 134,
        "slug": "job-sequencing-problem",
        "title": "Job Sequencing Problem",
        "difficulty": "Medium",
        "tags": ["Array", "Greedy", "Sorting", "Union Find"],
        "complexity": "O(n log n) time, O(max deadline) space",
        "functionName": "jobScheduling",
        "params": ["deadlines", "profits"],
        "description": """
Each job takes one unit of time and earns `profits[i]` if it finishes by `deadlines[i]`. Only one job runs at a time, starting at time `1`. Return `[jobsDone, totalProfit]` for the schedule with the highest profit.

**Constraints**

- `1 <= n <= 10^5`
- `1 <= deadline[i] <= n`
- `1 <= profit[i] <= 10^4`
""",
        "hints": [
            "Take jobs in decreasing profit and place each in the latest free slot before its deadline.",
            "A disjoint-set over slots finds that free slot quickly.",
        ],
        "tests": [
            {"input": [[4, 1, 1, 1], [20, 10, 40, 30]], "output": [2, 60], "sample": True},
            {"input": [[2, 1, 2, 1, 1], [100, 19, 27, 25, 15]], "output": [2, 127], "sample": True},
            {"input": [[1], [5]], "output": [1, 5]},
            {"input": [[1, 1], [5, 7]], "output": [1, 7]},
        ],
    },
    {
        "id": 135,
        "slug": "fractional-knapsack",
        "title": "Fractional Knapsack",
        "difficulty": "Medium",
        "tags": ["Array", "Greedy", "Sorting"],
        "complexity": "O(n log n) time, O(1) space",
        "functionName": "fractionalKnapsack",
        "params": ["weights", "values", "capacity"],
        "compare": "approx",
        "description": """
You may take fractions of items. Return the maximum value that fits in a knapsack of the given capacity. A tolerance of `1e-5` is allowed.

**Constraints**

- `1 <= n <= 10^5`
- `1 <= weight[i], value[i] <= 10^4`
- `1 <= capacity <= 10^9`
""",
        "hints": ["Sort by value per unit weight and fill greedily; only the last item is ever split."],
        "tests": [
            {"input": [[10, 20, 30], [60, 100, 120], 50], "output": 240.0, "sample": True},
            {"input": [[10], [60], 5], "output": 30.0, "sample": True},
            {"input": [[1, 1], [10, 20], 1], "output": 20.0},
            {"input": [[4, 5], [10, 20], 100], "output": 30.0},
        ],
    },
    {
        "id": 136,
        "slug": "assign-cookies",
        "title": "Assign Cookies",
        "difficulty": "Easy",
        "tags": ["Array", "Greedy", "Two Pointers"],
        "complexity": "O(n log n) time, O(1) space",
        "functionName": "findContentChildren",
        "params": ["g", "s"],
        "description": """
`g[i]` is the appetite of child `i` and `s[j]` is the size of cookie `j`. A child is content when given one cookie of size at least their appetite. Return the largest number of content children.

**Constraints**

- `1 <= g.length, s.length <= 5 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`
""",
        "hints": ["Sort both, then match the smallest sufficient cookie to the least hungry child."],
        "tests": [
            {"input": [[1, 2, 3], [1, 1]], "output": 1, "sample": True},
            {"input": [[1, 2], [1, 2, 3]], "output": 2, "sample": True},
            {"input": [[10], [1]], "output": 0},
            {"input": [[1, 1, 1], [1, 1]], "output": 2},
        ],
    },
    {
        "id": 137,
        "slug": "minimum-coins",
        "title": "Minimum Coins (Greedy)",
        "difficulty": "Easy",
        "tags": ["Array", "Greedy", "Math"],
        "complexity": "O(amount / largest coin) time, O(1) space",
        "functionName": "minimumCoins",
        "params": ["amount"],
        "description": """
With the Indian denominations `[1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]`, return the fewest notes and coins that make `amount`. These denominations are canonical, so taking the largest that fits is always optimal.

**Constraints**

- `0 <= amount <= 10^9`
""",
        "hints": ["Walk the denominations from largest to smallest and take as many of each as fit."],
        "tests": [
            {"input": [70], "output": 2, "sample": True},
            {"input": [121], "output": 3, "sample": True, "explanation": "100 + 20 + 1."},
            {"input": [0], "output": 0},
            {"input": [2000], "output": 1},
        ],
    },
    {
        "id": 138,
        "slug": "meeting-rooms",
        "title": "Meeting Rooms",
        "difficulty": "Easy",
        "tags": ["Array", "Sorting", "Interval"],
        "complexity": "O(n log n) time, O(1) space",
        "functionName": "canAttendMeetings",
        "params": ["intervals"],
        "description": """
Given meeting time intervals `[start, end]`, return whether one person could attend all of them — that is, whether no two overlap. Meetings that only touch at an endpoint do not overlap.

**Constraints**

- `0 <= intervals.length <= 10^4`
- `0 <= start < end <= 10^6`
""",
        "hints": ["Sort by start and check each meeting against the previous end."],
        "tests": [
            {"input": [[[0, 30], [5, 10], [15, 20]]], "output": False, "sample": True},
            {"input": [[[7, 10], [2, 4]]], "output": True, "sample": True},
            {"input": [[]], "output": True},
            {"input": [[[1, 2], [2, 3]]], "output": True},
        ],
    },
    {
        "id": 139,
        "slug": "meeting-rooms-ii",
        "title": "Meeting Rooms II",
        "difficulty": "Medium",
        "tags": ["Array", "Heap", "Sorting", "Interval"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "minMeetingRooms",
        "params": ["intervals"],
        "description": """
Return the fewest rooms needed so that every meeting can happen. Meetings that only touch at an endpoint can share a room.

**Constraints**

- `1 <= intervals.length <= 10^4`
- `0 <= start < end <= 10^6`
""",
        "hints": [
            "A min-heap of end times tells you whether a room frees up before the next meeting starts.",
            "The sweep-line version sorts starts and ends separately and tracks the running overlap.",
        ],
        "tests": [
            {"input": [[[0, 30], [5, 10], [15, 20]]], "output": 2, "sample": True},
            {"input": [[[7, 10], [2, 4]]], "output": 1, "sample": True},
            {"input": [[[1, 2]]], "output": 1},
            {"input": [[[1, 5], [2, 6], [3, 7]]], "output": 3},
        ],
    },
]
