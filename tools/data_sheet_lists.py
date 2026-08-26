"""Linked-list problems from the Blind 75 and SDE sheets."""

PROBLEMS = [
    {
        "id": 67,
        "slug": "add-two-numbers",
        "title": "Add Two Numbers",
        "difficulty": "Medium",
        "tags": ["Linked List", "Math", "Recursion"],
        "complexity": "O(m + n) time, O(1) extra space",
        "functionName": "addTwoNumbers",
        "params": ["l1", "l2"],
        "paramTypes": ["list", "list"],
        "returnType": "list",
        "description": """
Two non-empty linked lists hold the digits of two non-negative integers in reverse order, one digit per node. Add the numbers and return the sum as a linked list in the same form.

**Constraints**

- `1 <= list length <= 5000`
- `0 <= node value <= 9`, and no list has a leading zero except the number `0`
""",
        "hints": ["Carry the overflow into the next node, and remember the final carry can add one more node."],
        "tests": [
            {"input": [[2, 4, 3], [5, 6, 4]], "output": [7, 0, 8], "sample": True, "explanation": "342 + 465 = 807."},
            {"input": [[0], [0]], "output": [0], "sample": True},
            {"input": [[9, 9, 9], [1]], "output": [0, 0, 0, 1]},
            {"input": [[5], [5]], "output": [0, 1]},
        ],
    },
    {
        "id": 68,
        "slug": "middle-of-the-linked-list",
        "title": "Middle of the Linked List",
        "difficulty": "Easy",
        "tags": ["Linked List", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "middleNode",
        "params": ["head"],
        "paramTypes": ["list"],
        "returnType": "list",
        "description": """
Return the middle node of the list. With an even number of nodes, return the second of the two middle nodes.

**Constraints**

- `1 <= list length <= 5000`
""",
        "hints": ["Slow and fast pointers: when the fast one falls off the end, the slow one is in the middle."],
        "tests": [
            {"input": [[1, 2, 3, 4, 5]], "output": [3, 4, 5], "sample": True},
            {"input": [[1, 2, 3, 4, 5, 6]], "output": [4, 5, 6], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[1, 2]], "output": [2]},
        ],
    },
    {
        "id": 69,
        "slug": "remove-nth-node-from-end-of-list",
        "title": "Remove Nth Node From End of List",
        "difficulty": "Medium",
        "tags": ["Linked List", "Two Pointers"],
        "complexity": "O(n) time, O(1) space, one pass",
        "functionName": "removeNthFromEnd",
        "params": ["head", "n"],
        "paramTypes": ["list", "json"],
        "returnType": "list",
        "description": """
Remove the `n`-th node counting from the end of the list and return the head.

**Constraints**

- `1 <= list length <= 5000`
- `1 <= n <= list length`
""",
        "hints": [
            "Start one pointer `n` nodes ahead of the other; when it reaches the end, the other is at the node before the target.",
            "A dummy head keeps the case where the first node is removed from being special.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5], 2], "output": [1, 2, 3, 5], "sample": True},
            {"input": [[1], 1], "output": [], "sample": True},
            {"input": [[1, 2], 1], "output": [1]},
            {"input": [[1, 2], 2], "output": [2]},
        ],
    },
    {
        "id": 70,
        "slug": "delete-node-in-a-linked-list",
        "title": "Delete Node in a Linked List",
        "difficulty": "Medium",
        "tags": ["Linked List"],
        "complexity": "O(1) time, O(1) space",
        "functionName": "deleteNode",
        "params": ["head", "position"],
        "paramTypes": ["list", "json"],
        "returnType": "list",
        "description": """
Delete the node at index `position` (0-based) and return the head. The node is guaranteed **not** to be the last one.

The point of the exercise is that a node can be deleted with only a reference to it: copy the next node's value into it and unlink the next node. Walking from the head defeats the purpose.

**Constraints**

- `2 <= list length <= 5000`
- `0 <= position < list length - 1`
""",
        "hints": ["You cannot reach the previous node — so overwrite the current one instead of unlinking it."],
        "tests": [
            {"input": [[4, 5, 1, 9], 1], "output": [4, 1, 9], "sample": True},
            {"input": [[4, 5, 1, 9], 2], "output": [4, 5, 9], "sample": True},
            {"input": [[1, 2], 0], "output": [2]},
            {"input": [[0, 1, 2, 3], 0], "output": [1, 2, 3]},
        ],
    },
    {
        "id": 71,
        "slug": "intersection-of-two-linked-lists",
        "title": "Intersection of Two Linked Lists",
        "difficulty": "Easy",
        "tags": ["Linked List", "Two Pointers", "Hash Table"],
        "complexity": "O(m + n) time, O(1) space",
        "functionName": "getIntersectionNode",
        "params": ["headA", "headB"],
        "prepare": "linkedIntersection",
        "returnType": "listpos",
        "description": """
Two linked lists may share a suffix of nodes. Return the first shared node, or `null` when they never meet.

The test input is `[onlyA, onlyB, shared]`: the nodes unique to each list, then the nodes both lists end with. The checker reports the index of the node you return within list A.

**Constraints**

- `0 <= list length <= 5000`
- Node identity matters, not node values
""",
        "hints": [
            "Two pointers that switch lists when they run out travel the same total distance, so they meet at the join.",
            "If the lists do not intersect, both pointers reach the end at the same time.",
        ],
        "tests": [
            {"input": [[4, 1], [5, 6, 1], [8, 4, 5]], "output": 2, "sample": True,
             "explanation": "They join at the node holding 8, which is index 2 of list A."},
            {"input": [[2, 6, 4], [1, 5], []], "output": -1, "sample": True, "explanation": "No shared nodes."},
            {"input": [[], [], [1]], "output": 0},
            {"input": [[1], [], [2]], "output": 1},
        ],
    },
    {
        "id": 72,
        "slug": "linked-list-cycle",
        "title": "Linked List Cycle",
        "difficulty": "Easy",
        "tags": ["Linked List", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "hasCycle",
        "params": ["head"],
        "prepare": "linkedCycle",
        "description": """
Return `true` if the list contains a cycle.

The test input is `[values, pos]`: the node values, then the index the last node links back to (`-1` for no cycle).

**Constraints**

- `0 <= list length <= 10^4`
- `-1 <= pos < list length`
""",
        "hints": ["Floyd's tortoise and hare: a fast pointer laps a slow one exactly when a cycle exists."],
        "tests": [
            {"input": [[3, 2, 0, -4], 1], "output": True, "sample": True},
            {"input": [[1, 2], -1], "output": False, "sample": True},
            {"input": [[1], 0], "output": True},
            {"input": [[], -1], "output": False},
        ],
    },
    {
        "id": 73,
        "slug": "linked-list-cycle-ii",
        "title": "Linked List Cycle II",
        "difficulty": "Medium",
        "tags": ["Linked List", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "detectCycle",
        "params": ["head"],
        "prepare": "linkedCycle",
        "returnType": "listpos",
        "description": """
Return the node where the cycle begins, or `null` when there is no cycle. The checker reports its index from the head.

The test input is `[values, pos]`: the node values, then the index the last node links back to (`-1` for no cycle).

**Constraints**

- `0 <= list length <= 10^4`
- `-1 <= pos < list length`
""",
        "hints": [
            "After the tortoise and hare meet, reset one pointer to the head.",
            "Advancing both one step at a time from there, they meet exactly at the cycle entrance.",
        ],
        "tests": [
            {"input": [[3, 2, 0, -4], 1], "output": 1, "sample": True},
            {"input": [[1, 2], -1], "output": -1, "sample": True},
            {"input": [[1], 0], "output": 0},
            {"input": [[1, 2, 3, 4], 0], "output": 0},
        ],
    },
    {
        "id": 74,
        "slug": "palindrome-linked-list",
        "title": "Palindrome Linked List",
        "difficulty": "Easy",
        "tags": ["Linked List", "Two Pointers", "Stack"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "isPalindrome",
        "params": ["head"],
        "paramTypes": ["list"],
        "description": """
Return `true` if the list reads the same forwards and backwards.

**Constraints**

- `1 <= list length <= 10^5`
- `0 <= node value <= 9`
""",
        "hints": [
            "Copying to an array is O(n) space; the constant-space version reverses the second half.",
            "Find the middle with slow/fast pointers, reverse from there, then compare the halves.",
        ],
        "tests": [
            {"input": [[1, 2, 2, 1]], "output": True, "sample": True},
            {"input": [[1, 2]], "output": False, "sample": True},
            {"input": [[1]], "output": True},
            {"input": [[1, 2, 1]], "output": True},
        ],
    },
    {
        "id": 75,
        "slug": "reverse-nodes-in-k-group",
        "title": "Reverse Nodes in k-Group",
        "difficulty": "Hard",
        "tags": ["Linked List", "Recursion"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "reverseKGroup",
        "params": ["head", "k"],
        "paramTypes": ["list", "json"],
        "returnType": "list",
        "description": """
Reverse the nodes of the list `k` at a time and return the new head. A trailing group with fewer than `k` nodes stays as it is.

**Constraints**

- `1 <= list length <= 5000`
- `1 <= k <= list length`
""",
        "hints": [
            "Check that `k` nodes remain before reversing a group — otherwise leave the rest untouched.",
            "Keep a pointer to the tail of the previous group so the reversed pieces stay connected.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5], 2], "output": [2, 1, 4, 3, 5], "sample": True},
            {"input": [[1, 2, 3, 4, 5], 3], "output": [3, 2, 1, 4, 5], "sample": True},
            {"input": [[1], 1], "output": [1]},
            {"input": [[1, 2], 2], "output": [2, 1]},
        ],
    },
    {
        "id": 76,
        "slug": "rotate-list",
        "title": "Rotate List",
        "difficulty": "Medium",
        "tags": ["Linked List", "Two Pointers"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "rotateRight",
        "params": ["head", "k"],
        "paramTypes": ["list", "json"],
        "returnType": "list",
        "description": """
Rotate the list to the right by `k` places and return the new head.

**Constraints**

- `0 <= list length <= 5000`
- `0 <= k <= 2 * 10^9`
""",
        "hints": [
            "Close the list into a ring, then cut it at the right place.",
            "`k` can be far larger than the length — reduce it modulo the length first.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5], 2], "output": [4, 5, 1, 2, 3], "sample": True},
            {"input": [[0, 1, 2], 4], "output": [2, 0, 1], "sample": True},
            {"input": [[], 3], "output": []},
            {"input": [[1, 2], 0], "output": [1, 2]},
        ],
    },
    {
        "id": 77,
        "slug": "reorder-list",
        "title": "Reorder List",
        "difficulty": "Medium",
        "tags": ["Linked List", "Two Pointers", "Stack"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "reorderList",
        "params": ["head"],
        "paramTypes": ["list"],
        "checkArg": 0,
        "description": """
Reorder the list `L0 -> L1 -> ... -> Ln` in place into `L0 -> Ln -> L1 -> Ln-1 -> ...`, without changing any node's value.

**Constraints**

- `1 <= list length <= 5 * 10^4`
""",
        "hints": [
            "Split at the middle, reverse the second half, then weave the two halves together.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4]], "output": [1, 4, 2, 3], "sample": True},
            {"input": [[1, 2, 3, 4, 5]], "output": [1, 5, 2, 4, 3], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[1, 2]], "output": [1, 2]},
        ],
    },
    {
        "id": 78,
        "slug": "copy-list-with-random-pointer",
        "title": "Copy List with Random Pointer",
        "difficulty": "Medium",
        "tags": ["Linked List", "Hash Table"],
        "complexity": "O(n) time, O(1) extra space",
        "functionName": "copyRandomList",
        "params": ["head"],
        "prepare": "randomList",
        "returnType": "randomlist",
        "description": """
Every node has a `next` pointer and a `random` pointer that may point at any node or at `null`. Return a **deep copy**: new nodes, same values, and the same shape of links.

The test input and the expected answer are both `[[value, randomIndex], ...]`, where `randomIndex` is `null` when `random` is `null`.

**Constraints**

- `0 <= list length <= 1000`
- `-10^4 <= node value <= 10^4`
""",
        "hints": [
            "A hash map from old node to new node makes it easy; doing it in O(1) extra space is the real exercise.",
            "Interleave copies into the original list (`A -> A' -> B -> B'`), wire the randoms, then split the lists apart.",
        ],
        "tests": [
            {"input": [[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]],
             "output": [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], "sample": True},
            {"input": [[[1, 1], [2, 1]]], "output": [[1, 1], [2, 1]], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[[3, None], [3, 0], [3, None]]], "output": [[3, None], [3, 0], [3, None]]},
        ],
    },
    {
        "id": 79,
        "slug": "flatten-a-linked-list",
        "title": "Flatten a Linked List",
        "difficulty": "Medium",
        "tags": ["Linked List", "Merge Sort", "Heap"],
        "complexity": "O(total nodes * number of lists) time, O(1) space",
        "functionName": "flatten",
        "params": ["head"],
        "prepare": "bottomList",
        "returnType": "bottomlist",
        "description": """
Each node has a `next` pointer to the head of the next sorted column and a `bottom` pointer down its own sorted column. Flatten everything into one sorted list linked by `bottom`, and return its head.

The test input is a list of columns, and the expected answer is the flattened column.

**Constraints**

- `1 <= number of columns <= 1000`
- `1 <= nodes per column <= 100`
- Every column is sorted ascending
""",
        "hints": [
            "Merging two sorted columns is the same routine as merging two sorted lists — just follow `bottom`.",
            "Merge from the right so each merge folds one more column into an already-flattened tail.",
        ],
        "tests": [
            {"input": [[[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]]],
             "output": [5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50], "sample": True},
            {"input": [[[1], [2], [3]]], "output": [1, 2, 3], "sample": True},
            {"input": [[[1, 2, 3]]], "output": [1, 2, 3]},
            {"input": [[[2, 2], [1, 1]]], "output": [1, 1, 2, 2]},
        ],
    },
]
