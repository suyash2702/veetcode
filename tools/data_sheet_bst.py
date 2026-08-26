"""Binary search tree and tree-construction problems from the sheets."""

TREE_NOTE = "Trees are given in level order with `null` for a missing child, the way LeetCode writes them."

PROBLEMS = [
    {
        "id": 105,
        "slug": "search-in-a-binary-search-tree",
        "title": "Search in a Binary Search Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Binary Search Tree"],
        "complexity": "O(h) time, O(1) space",
        "functionName": "searchBST",
        "params": ["root", "val"],
        "paramTypes": ["tree", "json"],
        "returnType": "tree",
        "description": """
Return the subtree rooted at the node whose value is `val`, or an empty tree when no such node exists.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 5000`
- `1 <= node value <= 10^7`, all distinct
""",
        "hints": ["The BST property means one comparison per level — no need to search both sides."],
        "tests": [
            {"input": [[4, 2, 7, 1, 3], 2], "output": [2, 1, 3], "sample": True},
            {"input": [[4, 2, 7, 1, 3], 5], "output": [], "sample": True},
            {"input": [[1], 1], "output": [1]},
            {"input": [[8, 3, 10, 1, 6], 10], "output": [10]},
        ],
    },
    {
        "id": 106,
        "slug": "convert-sorted-array-to-binary-search-tree",
        "title": "Convert Sorted Array to Binary Search Tree",
        "difficulty": "Easy",
        "tags": ["Tree", "Binary Search Tree", "Divide and Conquer"],
        "complexity": "O(n) time, O(log n) space",
        "functionName": "sortedArrayToBST",
        "params": ["nums"],
        "returnType": "tree",
        "description": """
Build a height-balanced BST from a sorted array and return the root.

Several trees are valid, so this checker fixes one: **always take the middle element `(lo + hi) // 2` as the root**, which picks the left of the two middles when the range has an even length.

**Constraints**

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`, sorted ascending and distinct
""",
        "hints": ["The middle element becomes the root; recurse on the two halves."],
        "tests": [
            {"input": [[-10, -3, 0, 5, 9]], "output": [0, -10, 5, None, -3, None, 9], "sample": True},
            {"input": [[1, 3]], "output": [1, None, 3], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[1, 2, 3, 4]], "output": [2, 1, 3, None, None, None, 4]},
        ],
    },
    {
        "id": 107,
        "slug": "construct-bst-from-preorder-traversal",
        "title": "Construct BST from Preorder Traversal",
        "difficulty": "Medium",
        "tags": ["Tree", "Binary Search Tree", "Stack"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "bstFromPreorder",
        "params": ["preorder"],
        "returnType": "tree",
        "description": """
`preorder` is the preorder traversal of a BST with distinct values. Rebuild the tree and return its root.

**Constraints**

- `1 <= preorder.length <= 10^4`
- `1 <= preorder[i] <= 10^8`, all distinct
""",
        "hints": [
            "Sorting gives you the inorder traversal, but there is an O(n) way.",
            "Carry an upper bound down the recursion: a value above it belongs to an ancestor's right subtree.",
        ],
        "tests": [
            {"input": [[8, 5, 1, 7, 10, 12]], "output": [8, 5, 10, 1, 7, None, 12], "sample": True},
            {"input": [[1, 3]], "output": [1, None, 3], "sample": True},
            {"input": [[4, 2]], "output": [4, 2]},
            {"input": [[1]], "output": [1]},
        ],
    },
    {
        "id": 108,
        "slug": "lowest-common-ancestor-of-a-binary-search-tree",
        "title": "Lowest Common Ancestor of a Binary Search Tree",
        "difficulty": "Medium",
        "tags": ["Tree", "Binary Search Tree"],
        "complexity": "O(h) time, O(1) space",
        "functionName": "lowestCommonAncestor",
        "params": ["root", "p", "q"],
        "paramTypes": ["tree", "json", "json"],
        "description": """
`p` and `q` are values in the BST. Return the value of their lowest common ancestor.

""" + TREE_NOTE + """

**Constraints**

- `2 <= number of nodes <= 10^5`
- Values are distinct, and both `p` and `q` exist
""",
        "hints": ["Walk down: while both values sit on the same side, follow that side. The first split is the answer."],
        "tests": [
            {"input": [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8], "output": 6, "sample": True},
            {"input": [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4], "output": 2, "sample": True},
            {"input": [[2, 1], 2, 1], "output": 2},
            {"input": [[5, 3, 8, 1, 4], 1, 4], "output": 3},
        ],
    },
    {
        "id": 109,
        "slug": "inorder-predecessor-and-successor",
        "title": "Inorder Predecessor and Successor in BST",
        "difficulty": "Medium",
        "tags": ["Tree", "Binary Search Tree"],
        "complexity": "O(h) time, O(1) space",
        "functionName": "findPreSuc",
        "params": ["root", "key"],
        "paramTypes": ["tree", "json"],
        "description": """
Return `[predecessor, successor]` for `key`: the largest value strictly smaller than `key` and the smallest value strictly larger. Use `-1` when one does not exist. `key` may itself be absent from the tree.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^5`
- Values are distinct and positive
""",
        "hints": ["Two independent descents: remember the last node you passed going right, and the last going left."],
        "tests": [
            {"input": [[8, 1, 9, None, 4, None, 10, 3], 8], "output": [4, 9], "sample": True},
            {"input": [[8, 1, 9, None, 4, None, 10, 3], 10], "output": [9, -1], "sample": True},
            {"input": [[2, 1, 3], 1], "output": [-1, 2]},
            {"input": [[2, 1, 3], 5], "output": [3, -1]},
        ],
    },
    {
        "id": 110,
        "slug": "floor-and-ceil-in-bst",
        "title": "Floor and Ceil in BST",
        "difficulty": "Easy",
        "tags": ["Tree", "Binary Search Tree"],
        "complexity": "O(h) time, O(1) space",
        "functionName": "floorCeil",
        "params": ["root", "key"],
        "paramTypes": ["tree", "json"],
        "description": """
Return `[floor, ceil]`: the largest value `<= key` and the smallest value `>= key` in the BST. Use `-1` when one does not exist.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^5`
- Values are distinct and positive
""",
        "hints": ["One descent each: record the candidate whenever you move away from it."],
        "tests": [
            {"input": [[8, 4, 12, 2, 6, 10, 14], 7], "output": [6, 8], "sample": True},
            {"input": [[8, 4, 12, 2, 6, 10, 14], 8], "output": [8, 8], "sample": True},
            {"input": [[5], 1], "output": [-1, 5]},
            {"input": [[5], 9], "output": [5, -1]},
        ],
    },
    {
        "id": 111,
        "slug": "kth-smallest-element-in-a-bst",
        "title": "Kth Smallest Element in a BST",
        "difficulty": "Medium",
        "tags": ["Tree", "Binary Search Tree", "Depth-First Search"],
        "complexity": "O(h + k) time, O(h) space",
        "functionName": "kthSmallest",
        "params": ["root", "k"],
        "paramTypes": ["tree", "json"],
        "description": """
Return the `k`-th smallest value in the BST (1-indexed).

""" + TREE_NOTE + """

**Constraints**

- `1 <= k <= number of nodes <= 10^4`
""",
        "hints": ["Inorder visits values in sorted order — stop as soon as you have seen `k` of them."],
        "tests": [
            {"input": [[3, 1, 4, None, 2], 1], "output": 1, "sample": True},
            {"input": [[5, 3, 6, 2, 4, None, None, 1], 3], "output": 3, "sample": True},
            {"input": [[1], 1], "output": 1},
            {"input": [[2, 1, 3], 3], "output": 3},
        ],
    },
    {
        "id": 112,
        "slug": "two-sum-iv-input-is-a-bst",
        "title": "Two Sum IV - Input is a BST",
        "difficulty": "Easy",
        "tags": ["Tree", "Binary Search Tree", "Two Pointers"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "findTarget",
        "params": ["root", "k"],
        "paramTypes": ["tree", "json"],
        "description": """
Return `true` if two different nodes of the BST hold values that sum to `k`.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^4`
- `-10^5 <= node value, k <= 10^5`
""",
        "hints": [
            "A hash set of seen values works in O(n) space.",
            "Two iterators — one running inorder, one reverse-inorder — give the two-pointer version.",
        ],
        "tests": [
            {"input": [[5, 3, 6, 2, 4, None, 7], 9], "output": True, "sample": True},
            {"input": [[5, 3, 6, 2, 4, None, 7], 28], "output": False, "sample": True},
            {"input": [[2, 1, 3], 4], "output": True},
            {"input": [[1], 2], "output": False},
        ],
    },
    {
        "id": 113,
        "slug": "binary-search-tree-iterator",
        "title": "Binary Search Tree Iterator",
        "difficulty": "Medium",
        "tags": ["Tree", "Binary Search Tree", "Stack", "Design"],
        "complexity": "O(1) amortised per call, O(h) space",
        "functionName": "BSTIterator",
        "params": [],
        "design": {
            "className": "BSTIterator",
            "constructorTypes": ["tree"],
            "methods": [
                {"name": "BSTIterator", "params": ["root"]},
                {"name": "next", "params": []},
                {"name": "hasNext", "params": []},
            ],
        },
        "description": """
Implement an iterator over the inorder traversal of a BST:

- `BSTIterator(root)` — start the iterator; the pointer sits before the smallest value.
- `next()` — move to the next value and return it.
- `hasNext()` — whether a next value exists.

`next()` and `hasNext()` must run in average `O(1)` and the iterator may use only `O(h)` memory, so flattening the tree in the constructor is not allowed.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^5`
- `next()` is only called when `hasNext()` is true
""",
        "hints": [
            "Keep a stack holding the path down the leftmost spine.",
            "After popping a node, push the left spine of its right subtree.",
        ],
        "tests": [
            {"input": [["BSTIterator", "next", "next", "hasNext", "next", "hasNext"],
                       [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], []]],
             "output": [None, 3, 7, True, 9, True], "sample": True},
            {"input": [["BSTIterator", "hasNext", "next", "hasNext"], [[[1]], [], [], []]],
             "output": [None, True, 1, False], "sample": True},
            {"input": [["BSTIterator", "next", "next", "next"], [[[2, 1, 3]], [], [], []]],
             "output": [None, 1, 2, 3]},
        ],
    },
    {
        "id": 114,
        "slug": "largest-bst-in-a-binary-tree",
        "title": "Largest BST in a Binary Tree",
        "difficulty": "Hard",
        "tags": ["Tree", "Binary Search Tree", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "largestBst",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the number of nodes in the largest subtree that is itself a valid BST.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^5`
- `-10^9 <= node value <= 10^9`
""",
        "hints": [
            "Each node should report `(size, min, max, isBst)` about its subtree in one pass.",
            "A node forms a BST when both children do and its value sits strictly between their extremes.",
        ],
        "tests": [
            {"input": [[10, 5, 15, 1, 8, None, 7]], "output": 3, "sample": True},
            {"input": [[5, 2, 4, 1, 3]], "output": 3, "sample": True,
             "explanation": "The subtree 1 < 2 < 3 is a BST; the root is not."},
            {"input": [[]], "output": 0},
            {"input": [[2, 1, 3]], "output": 3},
        ],
    },
    {
        "id": 115,
        "slug": "maximum-sum-bst-in-binary-tree",
        "title": "Maximum Sum BST in Binary Tree",
        "difficulty": "Hard",
        "tags": ["Tree", "Binary Search Tree", "Dynamic Programming"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "maxSumBST",
        "params": ["root"],
        "paramTypes": ["tree"],
        "description": """
Return the largest sum of values in any subtree that is a valid BST. An empty subtree counts as a BST with sum `0`, so the answer is never negative.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 4 * 10^4`
- `-4 * 10^4 <= node value <= 4 * 10^4`
""",
        "hints": ["Same single pass as the largest BST, but carry the subtree sum alongside the bounds."],
        "tests": [
            {"input": [[1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6]], "output": 20, "sample": True},
            {"input": [[4, 3, None, 1, 2]], "output": 2, "sample": True},
            {"input": [[-4, -2, -5]], "output": 0},
            {"input": [[2, 1, 3]], "output": 6},
        ],
    },
    {
        "id": 116,
        "slug": "binary-tree-to-doubly-linked-list",
        "title": "Binary Tree to Doubly Linked List",
        "difficulty": "Medium",
        "tags": ["Tree", "Linked List", "Depth-First Search"],
        "complexity": "O(n) time, O(h) space",
        "functionName": "bToDLL",
        "params": ["root"],
        "paramTypes": ["tree"],
        "returnType": "dllist",
        "description": """
Convert the tree in place into a sorted doubly linked list following the inorder traversal: `left` becomes the previous pointer, `right` becomes the next pointer. Return the head.

The checker walks your list through `right`, so the nodes must actually be relinked.

""" + TREE_NOTE + """

**Constraints**

- `1 <= number of nodes <= 10^5`
""",
        "hints": ["Do an inorder walk while keeping the previously visited node, and wire the two pointers as you go."],
        "tests": [
            {"input": [[10, 12, 15, 25, 30, 36]], "output": [25, 12, 30, 10, 36, 15], "sample": True},
            {"input": [[1, 3, 5, 7, 9]], "output": [7, 3, 9, 1, 5], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[2, 1, 3]], "output": [1, 2, 3]},
        ],
    },
    {
        "id": 117,
        "slug": "construct-binary-tree-from-preorder-and-inorder-traversal",
        "title": "Construct Binary Tree from Preorder and Inorder Traversal",
        "difficulty": "Medium",
        "tags": ["Tree", "Divide and Conquer", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "buildTree",
        "params": ["preorder", "inorder"],
        "returnType": "tree",
        "description": """
Rebuild the binary tree from its preorder and inorder traversals and return the root. All values are distinct.

**Constraints**

- `1 <= preorder.length <= 3000`
- `inorder` is a permutation of `preorder`
""",
        "hints": [
            "The first preorder value is the root; its position in the inorder splits the left and right subtrees.",
            "A map from value to inorder index turns the O(n^2) scan into O(n).",
        ],
        "tests": [
            {"input": [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], "output": [3, 9, 20, None, None, 15, 7], "sample": True},
            {"input": [[-1], [-1]], "output": [-1], "sample": True},
            {"input": [[1, 2], [2, 1]], "output": [1, 2]},
            {"input": [[1, 2], [1, 2]], "output": [1, None, 2]},
        ],
    },
    {
        "id": 118,
        "slug": "construct-binary-tree-from-inorder-and-postorder-traversal",
        "title": "Construct Binary Tree from Inorder and Postorder Traversal",
        "difficulty": "Medium",
        "tags": ["Tree", "Divide and Conquer", "Hash Table"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "buildTree",
        "params": ["inorder", "postorder"],
        "returnType": "tree",
        "description": """
Rebuild the binary tree from its inorder and postorder traversals and return the root. All values are distinct.

**Constraints**

- `1 <= inorder.length <= 3000`
- `postorder` is a permutation of `inorder`
""",
        "hints": ["Postorder ends with the root, so consume it from the back and build the right subtree first."],
        "tests": [
            {"input": [[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]], "output": [3, 9, 20, None, None, 15, 7], "sample": True},
            {"input": [[-1], [-1]], "output": [-1], "sample": True},
            {"input": [[2, 1], [2, 1]], "output": [1, 2]},
            {"input": [[1, 2], [2, 1]], "output": [1, None, 2]},
        ],
    },
    {
        "id": 119,
        "slug": "serialize-and-deserialize-binary-tree",
        "title": "Serialize and Deserialize Binary Tree",
        "difficulty": "Hard",
        "tags": ["Tree", "Design", "Breadth-First Search"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "codec",
        "params": ["root"],
        "paramTypes": ["tree"],
        "returnType": "tree",
        "pyBody": """    # Write serialize(root) -> str and deserialize(data) -> TreeNode below,
    # then leave this line as the round trip the checker runs.
    return deserialize(serialize(root))


def serialize(root):
    # TODO: turn the tree into a string
    pass


def deserialize(data):
    # TODO: rebuild the tree from that string
    pass""",
        "jsBody": """  // Write serialize(root) and deserialize(data) below, then leave this line
  // as the round trip the checker runs.
  return deserialize(serialize(root));""",
        "description": """
Design a way to turn a binary tree into a string and back. Write two functions — `serialize(root)` and `deserialize(data)` — and leave `codec(root)` returning `deserialize(serialize(root))`, which is what the checker calls.

Your format is entirely up to you; only the round trip is checked.

""" + TREE_NOTE + """

**Constraints**

- `0 <= number of nodes <= 10^4`
- `-1000 <= node value <= 1000`
""",
        "hints": [
            "Preorder with an explicit marker for null children is enough to rebuild the shape.",
            "Deserialising is easiest with an index or an iterator over the tokens.",
        ],
        "tests": [
            {"input": [[1, 2, 3, None, None, 4, 5]], "output": [1, 2, 3, None, None, 4, 5], "sample": True},
            {"input": [[]], "output": [], "sample": True},
            {"input": [[1]], "output": [1]},
            {"input": [[1, None, 2, None, 3]], "output": [1, None, 2, None, 3]},
        ],
    },
]
