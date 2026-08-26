"""Binary tree problems from the Blind 75 and SDE sheets."""

TREE_NOTE = "Trees are given in level order with `null` for a missing child, the way LeetCode writes them."

PROBLEMS = [
    {
        "id": 80,
        "slug": "binary-tree-inorder-traversal",
        "title": "Binary Tree Inorder Traversal",
        "difficulty": "Easy",
        "tags": ["Tree", "Stack", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "inorderTraversal",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the values of the tree in inorder (left, node, right).

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "hints": ["The iterative version pushes left children onto a stack, then pops and turns right."],
        "tests": [
            {"input": [[1, None, 2, 3]], "output": [1, 3, 2], "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[4, 2, 6, 1, 3, 5, 7]], "output": [1, 2, 3, 4, 5, 6, 7]},
        ],
    },
    {
        "id": 81,
        "slug": "binary-tree-preorder-traversal",
        "title": "Binary Tree Preorder Traversal",
        "difficulty": "Easy",
        "tags": ["Tree", "Stack", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "preorderTraversal",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the values of the tree in preorder (node, left, right).

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "hints": ["With a stack, push the right child before the left so the left comes off first."],
        "tests": [
            {"input": [[1, None, 2, 3]], "output": [1, 2, 3], "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[4, 2, 6, 1, 3, 5, 7]], "output": [4, 2, 1, 3, 6, 5, 7]},
        ],
    },
    {
        "id": 82,
        "slug": "binary-tree-postorder-traversal",
        "title": "Binary Tree Postorder Traversal",
        "difficulty": "Easy",
        "tags": ["Tree", "Stack", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "postorderTraversal",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the values of the tree in postorder (left, right, node).

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "hints": ["Preorder with the children swapped, reversed, is postorder — one stack is enough."],
        "tests": [
            {"input": [[1, None, 2, 3]], "output": [3, 2, 1], "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[4, 2, 6, 1, 3, 5, 7]], "output": [1, 3, 2, 5, 7, 6, 4]},
        ],
    },
    {
        "id": 83,
        "slug": "binary-tree-zigzag-level-order-traversal",
        "title": "Binary Tree Zigzag Level Order Traversal",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "zigzagLevelOrder",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the level order traversal, but alternate direction: the first level left to right, the next right to left, and so on.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 2000`
""",
        "hints": ["Do a normal BFS and reverse every other level — no need for a deque of deques."],
        "tests": [
            {"input": [[3, 9, 20, None, None, 15, 7]], "output": [[3], [20, 9], [15, 7]], "sample": True},
            {"input": [[1]], "output": [[1]], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1, 2, 3, 4, None, None, 5]], "output": [[1], [3, 2], [4, 5]]},
        ],
    },
    {
        "id": 84,
        "slug": "binary-tree-right-side-view",
        "title": "Binary Tree Right Side View",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search", "Depth-First Search"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "rightSideView",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Standing to the right of the tree, return the values you can see, top to bottom.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 100`
""",
        "hints": ["The last node of every BFS level, or the first node reached at each depth going right-first."],
        "tests": [
            {"input": [[1, 2, 3, None, 5, None, 4]], "output": [1, 3, 4], "sample": True},
            {"input": [[1, None, 3]], "output": [1, 3], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1, 2]], "output": [1, 2]},
        ],
    },
    {
        "id": 85,
        "slug": "top-view-of-binary-tree",
        "title": "Top View of Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "topView",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Looking down on the tree, return the visible values from left to right. A node is visible when it is the first one at its horizontal distance from the root — the root is at distance `0`, a left child at `d - 1`, a right child at `d + 1`.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "hints": [
            "BFS visits nodes top-down, so the first node seen at each horizontal distance is the visible one.",
            "A DFS would need to compare depths, because it can reach a deeper node first.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, 6, 7]], "output": [4, 2, 1, 3, 7], "sample": True},
            {"input": [[1, 2, 3]], "output": [2, 1, 3], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1]], "output": [1]},
        ],
    },
    {
        "id": 86,
        "slug": "bottom-view-of-binary-tree",
        "title": "Bottom View of Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "bottomView",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Looking up at the tree from below, return the visible values from left to right: for each horizontal distance, the value of the last node BFS reaches there.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "hints": ["Same BFS as the top view, but overwrite the entry for a horizontal distance instead of keeping the first."],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, 6, 7]], "output": [4, 2, 6, 3, 7], "sample": True},
            {"input": [[1, 2, 3]], "output": [2, 1, 3], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1]], "output": [1]},
        ],
    },
    {
        "id": 87,
        "slug": "vertical-order-traversal-of-a-binary-tree",
        "title": "Vertical Order Traversal of a Binary Tree",
        "difficulty": "Hard",
        "tags": ["Tree", "Breadth-First Search", "Sorting"],
        "complexity": "O(n log n) time, O(n) space",
        "functionName": "verticalTraversal",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Group the nodes by horizontal distance (root `0`, left `d - 1`, right `d + 1`) and return the groups left to right. Inside a group, order by depth; nodes at the same position are ordered by value.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 1000`
- `0 <= node value <= 1000`
""",
        "hints": ["Collect `(column, row, value)` triples, sort them, then group by column."],
        "tests": [
            {"input": [[3, 9, 20, None, None, 15, 7]], "output": [[9], [3, 15], [20], [7]], "sample": True},
            {"input": [[1, 2, 3, 4, 5, 6, 7]], "output": [[4], [2], [1, 5, 6], [3], [7]], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1, 2, 3, 4, 6, 5, 7]], "output": [[4], [2], [1, 5, 6], [3], [7]]},
        ],
    },
    {
        "id": 88,
        "slug": "boundary-traversal-of-binary-tree",
        "title": "Boundary Traversal of Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "boundaryTraversal",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the boundary of the tree anti-clockwise, starting at the root: the left boundary (excluding leaves), then every leaf left to right, then the right boundary (excluding leaves) bottom-up. Each node appears once.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^4`
""",
        "hints": [
            "Three separate walks — left edge, leaves, right edge — are easier to get right than one clever traversal.",
            "The root counts as part of the left boundary, and a leaf must never be added twice.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, 6, 7]], "output": [1, 2, 4, 5, 6, 7, 3], "sample": True},
            {"input": [[1]], "output": [1], "sample": True},
            {"input": [[1, 2, None, 3]], "output": [1, 2, 3]},
            {"input": [[1, None, 2, None, 3]], "output": [1, 3, 2]},
        ],
    },
    {
        "id": 89,
        "slug": "binary-tree-maximum-path-sum",
        "title": "Binary Tree Maximum Path Sum",
        "difficulty": "Hard",
        "tags": ["Tree", "Depth-First Search", "Dynamic Programming"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "maxPathSum",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
A path is any sequence of nodes connected by edges, appearing at most once each, and it does not have to pass through the root. Return the largest sum of node values along any path.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 3 * 10^4`
- `-1000 <= node value <= 1000`
""",
        "hints": [
            "Each node returns the best downward path through it; a negative branch is worth dropping.",
            "The answer at a node is `value + max(left, 0) + max(right, 0)`, tracked globally.",
        ],
        "tests": [
            {"input": [[1, 2, 3]], "output": 6, "sample": True},
            {"input": [[-10, 9, 20, None, None, 15, 7]], "output": 42, "sample": True},
            {"input": [[-3]], "output": -3},
            {"input": [[2, -1]], "output": 2},
        ],
    },
    {
        "id": 90,
        "slug": "diameter-of-binary-tree",
        "title": "Diameter of Binary Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "diameterOfBinaryTree",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the length of the longest path between any two nodes, measured in edges. The path may or may not pass through the root.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^4`
""",
        "hints": ["While computing heights, the best answer at a node is `leftHeight + rightHeight`."],
        "tests": [
            {"input": [[1, 2, 3, 4, 5]], "output": 3, "sample": True},
            {"input": [[1, 2]], "output": 1, "sample": True},
            {"input": [[1]], "output": 0},
            {"input": [[1, 2, 3, 4, None, None, 5, 6, None, None, 7]], "output": 6},
        ],
    },
    {
        "id": 91,
        "slug": "balanced-binary-tree",
        "title": "Balanced Binary Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "isBalanced",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
A tree is height-balanced when every node's two subtrees differ in height by at most one. Return whether the tree is balanced.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 5000`
""",
        "hints": ["Return the height and a balanced flag together — recomputing heights per node is O(n^2)."],
        "tests": [
            {"input": [[3, 9, 20, None, None, 15, 7]], "output": True, "sample": True},
            {"input": [[1, 2, 2, 3, 3, None, None, 4, 4]], "output": False, "sample": True},
            {"input": [[]], "output": True},
            {"input": [[1, 2, None, 3]], "output": False},
        ],
    },
    {
        "id": 92,
        "slug": "lowest-common-ancestor-of-a-binary-tree",
        "title": "Lowest Common Ancestor of a Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "lowestCommonAncestor",
        "params": ["root", "p", "q"],
        "paramTypes": ["tree", "json", "json"],
        "description": """
`p` and `q` are values of two nodes in the tree, and all values are distinct. Return the value of their lowest common ancestor — the deepest node that has both as descendants (a node counts as its own descendant).

""" + TREE_NOTE + """

**Constraints**

- `2 <= number of nodes <= 10^5`
- Node values are distinct, and both `p` and `q` exist in the tree
""",
        "hints": [
            "Recurse: if a subtree contains `p` on one side and `q` on the other, its root is the answer.",
            "Finding either value can stop the descent — the shallower match wins.",
        ],
        "tests": [
            {"input": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1], "output": 3, "sample": True},
            {"input": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4], "output": 5, "sample": True},
            {"input": [[1, 2], 1, 2], "output": 1},
            {"input": [[1, 2, 3, 4, 5], 4, 5], "output": 2},
        ],
    },
    {
        "id": 93,
        "slug": "same-tree",
        "title": "Same Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "isSameTree",
        "params": ["p", "q"],
        "paramTypes": ["tree", "tree"],
        "description": """
Return whether two binary trees have the same structure and the same values.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 100`
""",
        "hints": ["Two trees match when the roots match and both pairs of subtrees match."],
        "tests": [
            {"input": [[1, 2, 3], [1, 2, 3]], "output": True, "sample": True},
            {"input": [[1, 2], [1, None, 2]], "output": False, "sample": True},
            {"input": [[], []], "output": True},
            {"input": [[1, 2, 1], [1, 1, 2]], "output": False},
        ],
    },
    {
        "id": 94,
        "slug": "symmetric-tree",
        "title": "Symmetric Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Depth-First Search", "Breadth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "isSymmetric",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return whether the tree is a mirror of itself around its centre.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 1000`
""",
        "hints": ["Compare the left subtree with the right one, walking them in opposite directions."],
        "tests": [
            {"input": [[1, 2, 2, 3, 4, 4, 3]], "output": True, "sample": True},
            {"input": [[1, 2, 2, None, 3, None, 3]], "output": False, "sample": True},
            {"input": [[1]], "output": True},
            {"input": [[1, 2, 2]], "output": True},
        ],
    },
    {
        "id": 95,
        "slug": "subtree-of-another-tree",
        "title": "Subtree of Another Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Depth-First Search", "String Matching"],
        "complexity": "O(m * n) time, O(h) space",
        "functionName": "isSubtree",
        "params": ["root", "subRoot"],
        "paramTypes": ["tree", "tree"],
        "description": """
Return whether `subRoot` appears in `root` as a subtree — some node of `root` together with all of its descendants must equal `subRoot`.

""" + TREE_NOTE + """

**Constraints**

- `1 <= nodes in root <= 2000`
- `1 <= nodes in subRoot <= 1000`
""",
        "hints": ["At every node of `root`, run the same-tree check against `subRoot`."],
        "tests": [
            {"input": [[3, 4, 5, 1, 2], [4, 1, 2]], "output": True, "sample": True},
            {"input": [[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]], "output": False, "sample": True},
            {"input": [[1], [1]], "output": True},
            {"input": [[1, 1], [1]], "output": True},
        ],
    },
    {
        "id": 96,
        "slug": "root-to-node-path-in-binary-tree",
        "title": "Root to Node Path in Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Depth-First Search", "Backtracking"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "rootToNodePath",
        "params": ["root", "target"],
        "paramTypes": ["tree", "json"],
        "description": """
Return the values on the path from the root down to the node holding `target`, inclusive. Node values are distinct; return an empty list when the value is absent.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
- Node values are distinct
""",
        "hints": ["Push on the way down, pop when a subtree fails — plain backtracking."],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, 6, 7], 5], "output": [1, 2, 5], "sample": True},
            {"input": [[1, 2, 3], 9], "output": [], "sample": True},
            {"input": [[1], 1], "output": [1]},
            {"input": [[1, 2, 3, 4, 5, 6, 7], 7], "output": [1, 3, 7]},
        ],
    },
    {
        "id": 97,
        "slug": "maximum-width-of-binary-tree",
        "title": "Maximum Width of Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "widthOfBinaryTree",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
The width of a level is the distance between its leftmost and rightmost non-null nodes, counting the null slots between them as if the tree were complete. Return the maximum width over all levels.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 3000`
""",
        "hints": [
            "Index nodes as in a heap: a node at `i` has children `2i` and `2i + 1`.",
            "Subtract the first index of each level to keep the numbers small.",
        ],
        "tests": [
            {"input": [[1, 3, 2, 5, 3, None, 9]], "output": 4, "sample": True},
            {"input": [[1, 3, 2, 5]], "output": 2, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[1, 3, 2, 5, None, None, 9, 6, None, None, 7]], "output": 8},
        ],
    },
    {
        "id": 98,
        "slug": "children-sum-property",
        "title": "Children Sum Property",
        "difficulty": "Medium",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "changeTree",
        "params": ["root"],
        "paramTypes": ["tree"],
        "returnType": "tree",
        "description": """
Change the tree so every node's value equals the sum of its children's values, and return the root. You may only **increase** node values, never decrease them, and you may not change the structure. A leaf keeps its value.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
- `0 <= node value <= 10^5`
""",
        "hints": [
            "On the way down, push the parent's value into whichever child is smaller.",
            "On the way back up, set the parent to the sum of its children.",
        ],
        "tests": [
            {"input": [[2, 35, 10, 2, 3, 5, 2]], "output": [90, 70, 20, 35, 35, 10, 10], "sample": True,
             "explanation": "Every parent grows to the sum of its children, bottom-up."},
            {"input": [[50, 7, 2, 3, 5, 1, 30]], "output": [200, 100, 100, 50, 50, 50, 50], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[1, 5]], "output": [5, 5]},
        ],
    },
    {
        "id": 99,
        "slug": "all-nodes-distance-k-in-binary-tree",
        "title": "All Nodes Distance K in Binary Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "distanceK",
        "params": ["root", "target", "k"],
        "paramTypes": ["tree", "json", "json"],
        "compare": "unordered",
        "description": """
`target` is the value of a node in the tree. Return the values of every node exactly `k` edges away from it, in any order. Node values are distinct.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 500`
- `0 <= k <= 1000`
- Node values are distinct, and `target` exists
""",
        "hints": [
            "Distance runs upwards too, so record each node's parent first.",
            "With parent links the tree becomes an undirected graph — then it is just BFS from the target.",
        ],
        "tests": [
            {"input": [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2], "output": [7, 4, 1], "sample": True},
            {"input": [[1], 1, 3], "output": [], "sample": True},
            {"input": [[1, 2, 3], 1, 1], "output": [2, 3]},
            {"input": [[1, 2, 3], 2, 0], "output": [2]},
        ],
    },
    {
        "id": 100,
        "slug": "minimum-time-to-burn-a-tree",
        "title": "Minimum Time to Burn a Tree",
        "difficulty": "Hard",
        "tags": ["Tree", "Breadth-First Search", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "timeToBurnTree",
        "params": ["root", "start"],
        "paramTypes": ["tree", "json"],
        "description": """
A fire starts at the node holding `start` and spreads to every adjacent node — parent and children — once per second. Return how many seconds it takes to burn the whole tree.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^4`
- Node values are distinct, and `start` exists
""",
        "hints": ["Record parents, then BFS outward from the start node counting levels; the answer is the last level."],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, None, 6, None, None, 7, 8], 8], "output": 5, "sample": True,
             "explanation": "8 -> 5 -> 2,7 -> 1,4 -> 3 -> 6."},
            {"input": [[1], 1], "output": 0, "sample": True},
            {"input": [[1, 2, 3], 1], "output": 1},
            {"input": [[1, 2, None, 3, None, 4], 4], "output": 3},
        ],
    },
    {
        "id": 101,
        "slug": "count-complete-tree-nodes",
        "title": "Count Complete Tree Nodes",
        "difficulty": "Easy",
        "tags": ["Tree", "Binary Search"],
        "complexity": "O(log^2 n) time, O(log n) space",
        "functionName": "countNodes",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
The tree is complete: every level except possibly the last is full, and the last level is filled from the left. Return the number of nodes in better than `O(n)` time.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 5 * 10^4`
""",
        "hints": [
            "If the leftmost and rightmost depths match, the subtree is perfect and holds `2^h - 1` nodes.",
            "Otherwise recurse into both children — only one of them is ever incomplete.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, 6]], "output": 6, "sample": True},
            {"input": [[]], "output": 0, "sample": True},
            {"input": [[1]], "output": 1},
            {"input": [[1, 2, 3, 4, 5, 6, 7]], "output": 7},
        ],
    },
    {
        "id": 102,
        "slug": "flatten-binary-tree-to-linked-list",
        "title": "Flatten Binary Tree to Linked List",
        "difficulty": "Medium",
        "tags": ["Tree", "Depth-First Search", "Linked List"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "flatten",
        "params": ["root"],
        "paramTypes": ["tree"],
        "checkArg": 0,
        "description": """
Flatten the tree in place into a "linked list": every node's `left` becomes `null` and its `right` points at the next node in **preorder**.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 2000`
""",
        "hints": [
            "Reverse preorder (right, left, node) lets you rewire each node with one previous pointer.",
            "The Morris-style version threads the left subtree's rightmost node to the right subtree.",
        ],
        "tests": [
            {"input": [[1, 2, 5, 3, 4, None, 6]], "output": [1, None, 2, None, 3, None, 4, None, 5, None, 6],
             "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[0]], "output": [0]},
            {"input": [[1, 2]], "output": [1, None, 2]},
        ],
    },
    {
        "id": 103,
        "slug": "morris-inorder-traversal",
        "title": "Morris Inorder Traversal",
        "difficulty": "Medium",
        "tags": ["Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "morrisInorder",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the inorder traversal using `O(1)` extra space — no stack and no recursion. Threading is the point of the exercise.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
""",
        "hints": [
            "Link the rightmost node of the left subtree back to the current node, then move left.",
            "Meeting that thread again means the left subtree is done — record the value and remove the thread.",
        ],
        "tests": [
            {"input": [[1, None, 2, 3]], "output": [1, 3, 2], "sample": True},
            {"input": [[4, 2, 6, 1, 3, 5, 7]], "output": [1, 2, 3, 4, 5, 6, 7], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[1]], "output": [1]},
        ],
    },
    {
        "id": 104,
        "slug": "populating-next-right-pointers-in-each-node",
        "title": "Populating Next Right Pointers in Each Node",
        "difficulty": "Medium",
        "tags": ["Tree", "Breadth-First Search", "Linked List"],
        "complexity": "O(n) time, O(1) space",
        "functionName": "connect",
        "params": ["root"],
        "paramTypes": ["tree"],
        "returnType": "nextlevels",
        "description": """
Set every node's `next` pointer to the node immediately to its right on the same level, and `null` for the last node of a level. Return the root.

The checker reads the levels back through the `next` pointers you set, so a level order traversal alone will not pass.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 6000`
""",
        "hints": [
            "A BFS solves it in O(n) space; the constant-space version uses the `next` pointers of the level above.",
            "While walking a level, wire up the children of each node before moving on.",
        ],
        "tests": [
            {"input": [[1, 2, 3, 4, 5, 6, 7]], "output": [[1], [2, 3], [4, 5, 6, 7]], "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[1, 2, 3, 4, None, None, 7]], "output": [[1], [2, 3], [4, 7]]},
            {"input": [[1]], "output": [[1]]},
        ],
    },
]
