"""Stack, queue, heap and design problems from the sheets."""

PROBLEMS = [
    {
        "id": 180,
        "slug": "implement-stack-using-arrays",
        "title": "Implement Stack using Arrays",
        "difficulty": "Easy",
        "tags": ["Stack", "Design", "Array"],
        "complexity": "O(1) per operation",
        "functionName": "ArrayStack",
        "params": [],
        "design": {
            "className": "ArrayStack",
            "methods": [
                {"name": "ArrayStack", "params": ["capacity"]},
                {"name": "push", "params": ["x"]},
                {"name": "pop", "params": []},
                {"name": "top", "params": []},
                {"name": "size", "params": []},
            ],
        },
        "description": """
Implement a stack on top of a fixed-size array:

- `ArrayStack(capacity)` — create a stack that holds at most `capacity` items.
- `push(x)` — add `x`; do nothing when the stack is full.
- `pop()` — remove and return the top, or `-1` when empty.
- `top()` — return the top without removing it, or `-1` when empty.
- `size()` — number of items held.

**Constraints**

- `1 <= capacity <= 10^5`
- At most `10^5` calls
""",
        "hints": ["One index pointing at the top is all the state you need."],
        "tests": [
            {"input": [["ArrayStack", "push", "push", "top", "pop", "size", "pop", "pop"],
                       [[2], [1], [2], [], [], [], [], []]],
             "output": [None, None, None, 2, 2, 1, 1, -1], "sample": True},
            {"input": [["ArrayStack", "pop", "top", "size"], [[1], [], [], []]],
             "output": [None, -1, -1, 0], "sample": True},
            {"input": [["ArrayStack", "push", "push", "size"], [[1], [5], [6], []]],
             "output": [None, None, None, 1], "explanation": "The second push is dropped: the stack is full."},
        ],
    },
    {
        "id": 181,
        "slug": "implement-queue-using-arrays",
        "title": "Implement Queue using Arrays",
        "difficulty": "Easy",
        "tags": ["Queue", "Design", "Array"],
        "complexity": "O(1) per operation",
        "functionName": "ArrayQueue",
        "params": [],
        "design": {
            "className": "ArrayQueue",
            "methods": [
                {"name": "ArrayQueue", "params": ["capacity"]},
                {"name": "push", "params": ["x"]},
                {"name": "pop", "params": []},
                {"name": "front", "params": []},
                {"name": "size", "params": []},
            ],
        },
        "description": """
Implement a queue on top of a fixed-size array:

- `ArrayQueue(capacity)` — hold at most `capacity` items.
- `push(x)` — enqueue `x`; do nothing when full.
- `pop()` — dequeue and return the front, or `-1` when empty.
- `front()` — the front item without removing it, or `-1` when empty.
- `size()` — number of items held.

**Constraints**

- `1 <= capacity <= 10^5`
- At most `10^5` calls
""",
        "hints": ["Wrap the head and tail indices around the array so pops stay O(1)."],
        "tests": [
            {"input": [["ArrayQueue", "push", "push", "front", "pop", "size", "pop", "pop"],
                       [[2], [1], [2], [], [], [], [], []]],
             "output": [None, None, None, 1, 1, 1, 2, -1], "sample": True},
            {"input": [["ArrayQueue", "pop", "front", "size"], [[1], [], [], []]],
             "output": [None, -1, -1, 0], "sample": True},
            {"input": [["ArrayQueue", "push", "push", "push", "pop", "push", "front"],
                       [[2], [1], [2], [3], [], [4], []]],
             "output": [None, None, None, None, 1, None, 2]},
        ],
    },
    {
        "id": 182,
        "slug": "implement-stack-using-queues",
        "title": "Implement Stack using Queues",
        "difficulty": "Easy",
        "tags": ["Stack", "Queue", "Design"],
        "complexity": "O(n) push or O(n) pop, O(n) space",
        "functionName": "MyStack",
        "params": [],
        "design": {
            "className": "MyStack",
            "methods": [
                {"name": "MyStack", "params": []},
                {"name": "push", "params": ["x"]},
                {"name": "pop", "params": []},
                {"name": "top", "params": []},
                {"name": "empty", "params": []},
            ],
        },
        "description": """
Implement a last-in-first-out stack using only queue operations (push to back, pop from front, peek at front, size, is-empty).

- `push(x)`, `pop()`, `top()`, `empty()`

**Constraints**

- `1 <= x <= 9`
- At most `100` calls, and `pop`/`top` are only called on a non-empty stack
""",
        "hints": ["Rotate the queue after each push so the newest element sits at the front."],
        "tests": [
            {"input": [["MyStack", "push", "push", "top", "pop", "empty"],
                       [[], [1], [2], [], [], []]],
             "output": [None, None, None, 2, 2, False], "sample": True},
            {"input": [["MyStack", "empty"], [[], []]], "output": [None, True], "sample": True},
            {"input": [["MyStack", "push", "pop", "empty"], [[], [3], [], []]],
             "output": [None, None, 3, True]},
        ],
    },
    {
        "id": 183,
        "slug": "implement-queue-using-stacks",
        "title": "Implement Queue using Stacks",
        "difficulty": "Easy",
        "tags": ["Stack", "Queue", "Design"],
        "complexity": "O(1) amortised per operation",
        "functionName": "MyQueue",
        "params": [],
        "design": {
            "className": "MyQueue",
            "methods": [
                {"name": "MyQueue", "params": []},
                {"name": "push", "params": ["x"]},
                {"name": "pop", "params": []},
                {"name": "peek", "params": []},
                {"name": "empty", "params": []},
            ],
        },
        "description": """
Implement a first-in-first-out queue using only stack operations (push, pop, peek at top, is-empty).

- `push(x)`, `pop()`, `peek()`, `empty()`

**Constraints**

- `1 <= x <= 9`
- At most `100` calls, and `pop`/`peek` are only called on a non-empty queue
""",
        "hints": [
            "Two stacks: one for arrivals, one for departures.",
            "Only move elements across when the departure stack runs dry — that keeps it O(1) amortised.",
        ],
        "tests": [
            {"input": [["MyQueue", "push", "push", "peek", "pop", "empty"],
                       [[], [1], [2], [], [], []]],
             "output": [None, None, None, 1, 1, False], "sample": True},
            {"input": [["MyQueue", "empty"], [[], []]], "output": [None, True], "sample": True},
            {"input": [["MyQueue", "push", "pop", "empty"], [[], [3], [], []]],
             "output": [None, None, 3, True]},
        ],
    },
    {
        "id": 184,
        "slug": "min-stack",
        "title": "Min Stack",
        "difficulty": "Medium",
        "tags": ["Stack", "Design"],
        "complexity": "O(1) per operation",
        "functionName": "MinStack",
        "params": [],
        "design": {
            "className": "MinStack",
            "methods": [
                {"name": "MinStack", "params": []},
                {"name": "push", "params": ["val"]},
                {"name": "pop", "params": []},
                {"name": "top", "params": []},
                {"name": "getMin", "params": []},
            ],
        },
        "description": """
Design a stack that also reports its minimum in constant time.

- `push(val)`, `pop()`, `top()`, `getMin()`

**Constraints**

- `-2^31 <= val <= 2^31 - 1`
- At most `3 * 10^4` calls, and `pop`, `top` and `getMin` are only called on a non-empty stack
""",
        "hints": ["Store the minimum-so-far alongside each element, or keep a second stack of minima."],
        "tests": [
            {"input": [["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
                       [[], [-2], [0], [-3], [], [], [], []]],
             "output": [None, None, None, None, -3, None, 0, -2], "sample": True},
            {"input": [["MinStack", "push", "getMin", "top"], [[], [5], [], []]],
             "output": [None, None, 5, 5], "sample": True},
            {"input": [["MinStack", "push", "push", "pop", "getMin"], [[], [2], [1], [], []]],
             "output": [None, None, None, None, 2]},
        ],
    },
    {
        "id": 185,
        "slug": "lru-cache",
        "title": "LRU Cache",
        "difficulty": "Medium",
        "tags": ["Hash Table", "Linked List", "Design"],
        "complexity": "O(1) per operation",
        "functionName": "LRUCache",
        "params": [],
        "design": {
            "className": "LRUCache",
            "methods": [
                {"name": "LRUCache", "params": ["capacity"]},
                {"name": "get", "params": ["key"]},
                {"name": "put", "params": ["key", "value"]},
            ],
        },
        "description": """
Design a cache that evicts the least recently used key when it is full. Both operations must run in `O(1)`.

- `LRUCache(capacity)`
- `get(key)` — the value, or `-1` when the key is absent
- `put(key, value)` — insert or overwrite, evicting the least recently used key when over capacity

Both `get` and `put` count as a use.

**Constraints**

- `1 <= capacity <= 3000`
- `0 <= key, value <= 10^4`
- At most `2 * 10^5` calls
""",
        "hints": [
            "A hash map gives O(1) lookup; a doubly linked list gives O(1) reordering.",
            "Keep the most recent entry at the head, so eviction is always the tail.",
        ],
        "tests": [
            {"input": [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                       [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]],
             "output": [None, None, None, 1, None, -1, None, -1, 3, 4], "sample": True},
            {"input": [["LRUCache", "put", "get", "get"], [[1], [1, 5], [1], [2]]],
             "output": [None, None, 5, -1], "sample": True},
            {"input": [["LRUCache", "put", "put", "put", "get"], [[2], [1, 1], [2, 2], [1, 9], [1]]],
             "output": [None, None, None, None, 9]},
        ],
    },
    {
        "id": 186,
        "slug": "lfu-cache",
        "title": "LFU Cache",
        "difficulty": "Hard",
        "tags": ["Hash Table", "Linked List", "Design"],
        "complexity": "O(1) per operation",
        "functionName": "LFUCache",
        "params": [],
        "design": {
            "className": "LFUCache",
            "methods": [
                {"name": "LFUCache", "params": ["capacity"]},
                {"name": "get", "params": ["key"]},
                {"name": "put", "params": ["key", "value"]},
            ],
        },
        "description": """
Design a cache that evicts the least frequently used key, breaking ties by evicting the least recently used among them. Both operations must run in `O(1)`.

- `LFUCache(capacity)`
- `get(key)` — the value, or `-1` when the key is absent
- `put(key, value)` — insert or overwrite; a `capacity` of `0` stores nothing

Both `get` and `put` increase a key's use count.

**Constraints**

- `0 <= capacity <= 10^4`
- `0 <= key, value <= 10^5`
- At most `2 * 10^5` calls
""",
        "hints": [
            "Bucket the keys by use count, keeping each bucket in most-recent-first order.",
            "Track the smallest non-empty count so eviction stays O(1).",
        ],
        "tests": [
            {"input": [["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
                       [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]],
             "output": [None, None, None, 1, None, -1, 3, None, -1, 3, 4], "sample": True},
            {"input": [["LFUCache", "put", "get"], [[0], [1, 1], [1]]],
             "output": [None, None, -1], "sample": True, "explanation": "Capacity 0 stores nothing."},
            {"input": [["LFUCache", "put", "put", "put", "get", "get"], [[2], [1, 1], [2, 2], [3, 3], [1], [3]]],
             "output": [None, None, None, None, -1, 3]},
        ],
    },
    {
        "id": 187,
        "slug": "online-stock-span",
        "title": "Online Stock Span",
        "difficulty": "Medium",
        "tags": ["Stack", "Design", "Monotonic Stack"],
        "complexity": "O(1) amortised per call",
        "functionName": "StockSpanner",
        "params": [],
        "design": {
            "className": "StockSpanner",
            "methods": [
                {"name": "StockSpanner", "params": []},
                {"name": "next", "params": ["price"]},
            ],
        },
        "description": """
`next(price)` returns the span of today's price: the number of consecutive days up to today whose price was less than or equal to today's.

**Constraints**

- `1 <= price <= 10^5`
- At most `10^4` calls
""",
        "hints": [
            "Keep a stack of `(price, span)` pairs in decreasing price order.",
            "Popping a smaller price folds its span into the current one, so each day is popped once.",
        ],
        "tests": [
            {"input": [["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
                       [[], [100], [80], [60], [70], [60], [75], [85]]],
             "output": [None, 1, 1, 1, 2, 1, 4, 6], "sample": True},
            {"input": [["StockSpanner", "next", "next"], [[], [5], [5]]],
             "output": [None, 1, 2], "sample": True},
            {"input": [["StockSpanner", "next", "next", "next"], [[], [3], [2], [1]]],
             "output": [None, 1, 1, 1]},
        ],
    },
    {
        "id": 188,
        "slug": "kth-largest-element-in-a-stream",
        "title": "Kth Largest Element in a Stream",
        "difficulty": "Easy",
        "tags": ["Heap", "Design"],
        "complexity": "O(log k) per call",
        "functionName": "KthLargest",
        "params": [],
        "design": {
            "className": "KthLargest",
            "methods": [
                {"name": "KthLargest", "params": ["k", "nums"]},
                {"name": "add", "params": ["val"]},
            ],
        },
        "description": """
- `KthLargest(k, nums)` — start from an initial stream.
- `add(val)` — append `val` and return the `k`-th largest value seen so far.

**Constraints**

- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- At least `k` values exist by the time `add` returns
""",
        "hints": ["Keep a min-heap of exactly `k` elements; its root is the answer."],
        "tests": [
            {"input": [["KthLargest", "add", "add", "add", "add", "add"],
                       [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]],
             "output": [None, 4, 5, 5, 8, 8], "sample": True},
            {"input": [["KthLargest", "add", "add"], [[1, []], [-1], [1]]],
             "output": [None, -1, 1], "sample": True},
            {"input": [["KthLargest", "add"], [[2, [1, 2]], [3]]], "output": [None, 2]},
        ],
    },
    {
        "id": 189,
        "slug": "find-median-from-data-stream",
        "title": "Find Median from Data Stream",
        "difficulty": "Hard",
        "tags": ["Heap", "Design", "Two Pointers"],
        "complexity": "O(log n) insert, O(1) query",
        "functionName": "MedianFinder",
        "params": [],
        "compare": "approx",
        "design": {
            "className": "MedianFinder",
            "methods": [
                {"name": "MedianFinder", "params": []},
                {"name": "addNum", "params": ["num"]},
                {"name": "findMedian", "params": []},
            ],
        },
        "description": """
- `addNum(num)` — add a value to the stream.
- `findMedian()` — the median of everything added so far; with an even count, the mean of the two middle values.

A tolerance of `1e-5` is allowed.

**Constraints**

- `-10^5 <= num <= 10^5`
- `findMedian` is only called after at least one `addNum`
- At most `5 * 10^4` calls
""",
        "hints": [
            "Two heaps: a max-heap for the lower half and a min-heap for the upper half.",
            "Keep their sizes within one of each other and the median is at the tops.",
        ],
        "tests": [
            {"input": [["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
                       [[], [1], [2], [], [3], []]],
             "output": [None, None, None, 1.5, None, 2.0], "sample": True},
            {"input": [["MedianFinder", "addNum", "findMedian"], [[], [5], []]],
             "output": [None, None, 5.0], "sample": True},
            {"input": [["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
                       [[], [4], [1], [3], [2], []]],
             "output": [None, None, None, None, None, 2.5]},
        ],
    },
    {
        "id": 190,
        "slug": "next-greater-element-i",
        "title": "Next Greater Element I",
        "difficulty": "Easy",
        "tags": ["Array", "Stack", "Hash Table", "Monotonic Stack"],
        "complexity": "O(n + m) time, O(n) space",
        "functionName": "nextGreaterElement",
        "params": ["nums1", "nums2"],
        "description": """
`nums1` is a subset of `nums2` and all values are distinct. For each value in `nums1`, return the first value to its right in `nums2` that is greater than it, or `-1` when there is none.

**Constraints**

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= values <= 10^4`, distinct within each array
""",
        "hints": ["Sweep `nums2` with a decreasing stack; popping a value means the current one is its next greater."],
        "tests": [
            {"input": [[4, 1, 2], [1, 3, 4, 2]], "output": [-1, 3, -1], "sample": True},
            {"input": [[2, 4], [1, 2, 3, 4]], "output": [3, -1], "sample": True},
            {"input": [[1], [1]], "output": [-1]},
            {"input": [[3, 1], [3, 1, 5]], "output": [5, 5]},
        ],
    },
    {
        "id": 191,
        "slug": "next-smaller-element",
        "title": "Next Smaller Element",
        "difficulty": "Easy",
        "tags": ["Array", "Stack", "Monotonic Stack"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "nextSmallerElement",
        "params": ["nums"],
        "description": """
For each position, return the first value to its right that is strictly smaller, or `-1` when there is none.

**Constraints**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
""",
        "hints": ["Sweep from the right with an increasing stack, popping everything at least as large as the current value."],
        "tests": [
            {"input": [[4, 8, 5, 2, 25]], "output": [2, 5, 2, -1, -1], "sample": True},
            {"input": [[1, 2, 3]], "output": [-1, -1, -1], "sample": True},
            {"input": [[3, 2, 1]], "output": [2, 1, -1]},
            {"input": [[5]], "output": [-1]},
        ],
    },
    {
        "id": 192,
        "slug": "sort-a-stack",
        "title": "Sort a Stack",
        "difficulty": "Easy",
        "tags": ["Stack", "Recursion", "Sorting"],
        "complexity": "O(n^2) time, O(n) space",
        "functionName": "sortStack",
        "params": ["stack"],
        "description": """
`stack` is given bottom-first, so the last element is the top. Sort it so the largest value ends on top, using only stack operations and recursion — no arrays or library sorts.

Return the sorted stack in the same bottom-first form.

**Constraints**

- `0 <= stack length <= 2000`
- `-10^9 <= value <= 10^9`
""",
        "hints": ["Pop everything, then insert each value back into the already sorted remainder."],
        "tests": [
            {"input": [[11, 2, 32, 3, 41]], "output": [2, 3, 11, 32, 41], "sample": True},
            {"input": [[-3, 14, 18, -5, 30]], "output": [-5, -3, 14, 18, 30], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1]], "output": [1]},
        ],
    },
    {
        "id": 193,
        "slug": "largest-rectangle-in-histogram",
        "title": "Largest Rectangle in Histogram",
        "difficulty": "Hard",
        "tags": ["Array", "Stack", "Monotonic Stack"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "largestRectangleArea",
        "params": ["heights"],
        "description": """
Each bar has width `1` and height `heights[i]`. Return the area of the largest rectangle that fits inside the histogram.

**Constraints**

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
""",
        "hints": [
            "For each bar, the rectangle it defines runs until a strictly shorter bar on either side.",
            "An increasing stack finds both boundaries in one sweep.",
        ],
        "tests": [
            {"input": [[2, 1, 5, 6, 2, 3]], "output": 10, "sample": True},
            {"input": [[2, 4]], "output": 4, "sample": True},
            {"input": [[0]], "output": 0},
            {"input": [[1, 1, 1, 1]], "output": 4},
        ],
    },
    {
        "id": 194,
        "slug": "sliding-window-maximum",
        "title": "Sliding Window Maximum",
        "difficulty": "Hard",
        "tags": ["Array", "Queue", "Sliding Window", "Heap"],
        "complexity": "O(n) time, O(k) space",
        "functionName": "maxSlidingWindow",
        "params": ["nums", "k"],
        "description": """
Return the maximum of every window of `k` consecutive values as the window slides from left to right.

**Constraints**

- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`
- `-10^4 <= nums[i] <= 10^4`
""",
        "hints": [
            "Keep a deque of indices whose values decrease.",
            "Drop indices that fall out of the window from the front, and smaller values from the back.",
        ],
        "tests": [
            {"input": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "output": [3, 3, 5, 5, 6, 7], "sample": True},
            {"input": [[1], 1], "output": [1], "sample": True},
            {"input": [[1, -1], 1], "output": [1, -1]},
            {"input": [[9, 8, 7, 6], 2], "output": [9, 8, 7]},
        ],
    },
    {
        "id": 195,
        "slug": "maximum-of-minimum-every-window-size",
        "title": "Maximum of Minimum for Every Window Size",
        "difficulty": "Hard",
        "tags": ["Array", "Stack", "Monotonic Stack"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "maxOfMin",
        "params": ["nums"],
        "description": """
For every window size `k` from `1` to `n`, find the minimum of each window of that size and take the largest of those minima. Return the results for all `k` in order.

**Constraints**

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
""",
        "hints": [
            "For each element, find the widest window in which it is the minimum — previous and next smaller elements.",
            "That gives a best value per window size; a right-to-left sweep fills the gaps.",
        ],
        "tests": [
            {"input": [[10, 20, 30, 50, 10, 70, 30]], "output": [70, 30, 20, 10, 10, 10, 10], "sample": True},
            {"input": [[10, 20, 30]], "output": [30, 20, 10], "sample": True},
            {"input": [[5]], "output": [5]},
            {"input": [[1, 1]], "output": [1, 1]},
        ],
    },
    {
        "id": 196,
        "slug": "the-celebrity-problem",
        "title": "The Celebrity Problem",
        "difficulty": "Medium",
        "tags": ["Array", "Stack", "Two Pointers", "Graph"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "findCelebrity",
        "params": ["knows"],
        "description": """
`knows[i][j] == 1` means person `i` knows person `j`. A celebrity is known by everyone else and knows nobody. Return that person's index, or `-1` when there is no celebrity.

**Constraints**

- `1 <= n <= 3000`
- `knows[i][i] == 1`
""",
        "hints": [
            "One pass narrows `n` candidates to one: if `a` knows `b`, `a` is out; otherwise `b` is out.",
            "Then verify the survivor against every other person.",
        ],
        "tests": [
            {"input": [[[1, 1, 0], [0, 1, 0], [1, 1, 1]]], "output": 1, "sample": True},
            {"input": [[[1, 0, 1], [1, 1, 0], [0, 1, 1]]], "output": -1, "sample": True},
            {"input": [[[1]]], "output": 0},
            {"input": [[[1, 1], [0, 1]]], "output": 1},
        ],
    },
    {
        "id": 197,
        "slug": "distinct-numbers-in-every-window",
        "title": "Distinct Numbers in Every Window",
        "difficulty": "Medium",
        "tags": ["Array", "Hash Table", "Sliding Window"],
        "complexity": "O(n) time, O(k) space",
        "functionName": "countDistinct",
        "params": ["nums", "k"],
        "description": """
Return the number of distinct values in each window of `k` consecutive elements, as the window slides left to right.

**Constraints**

- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`
- `-10^9 <= nums[i] <= 10^9`
""",
        "hints": ["Maintain counts as the window moves; a count hitting zero drops the distinct total."],
        "tests": [
            {"input": [[1, 2, 1, 3, 4, 2, 3], 4], "output": [3, 4, 4, 3], "sample": True},
            {"input": [[1, 1, 1], 2], "output": [1, 1], "sample": True},
            {"input": [[1], 1], "output": [1]},
            {"input": [[1, 2, 3], 3], "output": [3]},
        ],
    },
    {
        "id": 198,
        "slug": "maximum-sum-combinations",
        "title": "Maximum Sum Combinations",
        "difficulty": "Medium",
        "tags": ["Array", "Heap", "Sorting"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "maxCombinations",
        "params": ["a", "b", "k"],
        "description": """
Form every sum `a[i] + b[j]` and return the `k` largest of them, in decreasing order. The same pair may not be reused, but equal sums from different pairs each count.

**Constraints**

- `1 <= n <= 10^4`
- `1 <= k <= n * n`, and `k <= 10^4`
- `-10^5 <= values <= 10^5`
""",
        "hints": [
            "Sort both arrays; the largest sum is the last of each.",
            "A max-heap over candidate pairs, with a visited set, pulls out the next largest each time.",
        ],
        "tests": [
            {"input": [[3, 2], [1, 4], 2], "output": [7, 6], "sample": True},
            {"input": [[1, 4, 2, 3], [2, 5, 1, 6], 3], "output": [10, 9, 9], "sample": True},
            {"input": [[1], [1], 1], "output": [2]},
            {"input": [[1, 2], [3, 4], 4], "output": [6, 5, 5, 4]},
        ],
    },
]
