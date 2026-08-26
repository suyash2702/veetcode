"""Graph problems from the Blind 75 and SDE sheets."""

EDGE_NOTE = ("Graphs are given as a node count `n` (nodes are numbered `0` to `n - 1`) "
             "and an edge list.")

PROBLEMS = [
    {
        "id": 160,
        "slug": "clone-graph",
        "title": "Clone Graph",
        "difficulty": "Medium",
        "tags": ["Graph", "Depth-First Search", "Hash Table"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "cloneGraph",
        "params": ["node"],
        "prepare": "graphNodes",
        "returnType": "graph",
        "description": """
Return a **deep copy** of a connected undirected graph. Each `Node` has an integer `val` and a list of `neighbors`.

The test input and the expected answer are adjacency lists: entry `i` holds the neighbours of the node numbered `i + 1`. You are handed the node numbered `1`.

**Constraints**

- `0 <= number of nodes <= 100`
- The graph is connected, undirected and has no self-loops or repeated edges
""",
        "hints": [
            "Keep a map from original node to copy so a node is cloned once.",
            "Create the copy before recursing into neighbours, or cycles never terminate.",
        ],
        "tests": [
            {"input": [[[2, 4], [1, 3], [2, 4], [1, 3]]], "output": [[2, 4], [1, 3], [2, 4], [1, 3]],
             "sample": True},
            {"input": [[[]]], "output": [[]], "sample": True},
            {"input": [[]], "output": []},
            {"input": [[[2], [1]]], "output": [[2], [1]]},
        ],
    },
    {
        "id": 161,
        "slug": "bfs-of-graph",
        "title": "BFS of Graph",
        "difficulty": "Easy",
        "tags": ["Graph", "Breadth-First Search"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "bfsOfGraph",
        "params": ["adj"],
        "description": """
`adj[i]` lists the neighbours of node `i` in the order they should be visited. Return the breadth-first traversal starting at node `0`, visiting each node once.

**Constraints**

- `1 <= n <= 10^4`
- `0 <= edges <= 10^5`
""",
        "hints": ["A queue plus a visited set; mark a node when you enqueue it, not when you dequeue it."],
        "tests": [
            {"input": [[[1, 2], [0, 3], [0], [1]]], "output": [0, 1, 2, 3], "sample": True},
            {"input": [[[], []]], "output": [0], "sample": True},
            {"input": [[[]]], "output": [0]},
            {"input": [[[2], [], [0]]], "output": [0, 2]},
        ],
    },
    {
        "id": 162,
        "slug": "dfs-of-graph",
        "title": "DFS of Graph",
        "difficulty": "Easy",
        "tags": ["Graph", "Depth-First Search"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "dfsOfGraph",
        "params": ["adj"],
        "description": """
`adj[i]` lists the neighbours of node `i` in the order they should be visited. Return the depth-first traversal starting at node `0`, visiting each node once.

**Constraints**

- `1 <= n <= 10^4`
- `0 <= edges <= 10^5`
""",
        "hints": ["Recurse into the first unvisited neighbour before moving on to the next one."],
        "tests": [
            {"input": [[[1, 2], [0, 3], [0], [1]]], "output": [0, 1, 3, 2], "sample": True},
            {"input": [[[], []]], "output": [0], "sample": True},
            {"input": [[[]]], "output": [0]},
            {"input": [[[2], [], [0]]], "output": [0, 2]},
        ],
    },
    {
        "id": 163,
        "slug": "detect-cycle-in-undirected-graph",
        "title": "Detect Cycle in an Undirected Graph",
        "difficulty": "Medium",
        "tags": ["Graph", "Breadth-First Search", "Union Find"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "hasCycle",
        "params": ["n", "edges"],
        "description": """
Return whether the undirected graph contains a cycle. The graph may be disconnected.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": [
            "During a traversal, an edge back to an already visited node that is not the one you came from closes a cycle.",
            "Union-find gives the same answer: an edge whose endpoints already share a root closes a cycle.",
        ],
        "tests": [
            {"input": [4, [[0, 1], [1, 2], [2, 3], [3, 0]]], "output": True, "sample": True},
            {"input": [4, [[0, 1], [1, 2], [2, 3]]], "output": False, "sample": True},
            {"input": [1, []], "output": False},
            {"input": [3, [[0, 1], [0, 1]]], "output": True},
        ],
    },
    {
        "id": 164,
        "slug": "detect-cycle-in-directed-graph",
        "title": "Detect Cycle in a Directed Graph",
        "difficulty": "Medium",
        "tags": ["Graph", "Depth-First Search", "Topological Sort"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "hasCycle",
        "params": ["n", "edges"],
        "description": """
Each edge `[a, b]` points from `a` to `b`. Return whether the directed graph contains a cycle.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": [
            "A cycle is an edge back into a node still on the current DFS stack — visited alone is not enough.",
            "Kahn's algorithm answers it too: leftover nodes after the queue empties sit on cycles.",
        ],
        "tests": [
            {"input": [4, [[0, 1], [1, 2], [2, 3], [3, 1]]], "output": True, "sample": True},
            {"input": [4, [[0, 1], [1, 2], [2, 3]]], "output": False, "sample": True},
            {"input": [1, [[0, 0]]], "output": True},
            {"input": [3, [[0, 1], [0, 2], [1, 2]]], "output": False},
        ],
    },
    {
        "id": 165,
        "slug": "topological-sort",
        "title": "Topological Sort",
        "difficulty": "Medium",
        "tags": ["Graph", "Topological Sort", "Breadth-First Search"],
        "complexity": "O(n log n + e) time, O(n) space",
        "functionName": "topologicalSort",
        "params": ["n", "edges"],
        "description": """
Each edge `[a, b]` means `a` must come before `b`. Return the **lexicographically smallest** topological order, or an empty list when the graph has a cycle.

Asking for the smallest order makes the answer unique — any valid order would otherwise do.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": [
            "Kahn's algorithm, but pull the smallest available node instead of any node — that is a min-heap.",
            "Ending with fewer than `n` nodes emitted means a cycle.",
        ],
        "tests": [
            {"input": [4, [[0, 1], [1, 2], [2, 3]]], "output": [0, 1, 2, 3], "sample": True},
            {"input": [4, [[2, 3], [0, 1]]], "output": [0, 1, 2, 3], "sample": True},
            {"input": [2, [[0, 1], [1, 0]]], "output": []},
            {"input": [3, []], "output": [0, 1, 2]},
        ],
    },
    {
        "id": 166,
        "slug": "is-graph-bipartite",
        "title": "Is Graph Bipartite?",
        "difficulty": "Medium",
        "tags": ["Graph", "Breadth-First Search", "Union Find"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "isBipartite",
        "params": ["n", "edges"],
        "description": """
Return whether the nodes of the undirected graph can be split into two sets so that every edge joins one set to the other. The graph may be disconnected.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": [
            "Two-colour the graph during a traversal; a conflict means it is not bipartite.",
            "Equivalently: a graph is bipartite exactly when it has no odd-length cycle.",
        ],
        "tests": [
            {"input": [4, [[0, 1], [1, 2], [2, 3], [3, 0]]], "output": True, "sample": True},
            {"input": [3, [[0, 1], [1, 2], [2, 0]]], "output": False, "sample": True},
            {"input": [1, []], "output": True},
            {"input": [2, [[0, 1]]], "output": True},
        ],
    },
    {
        "id": 167,
        "slug": "number-of-connected-components-in-an-undirected-graph",
        "title": "Number of Connected Components in an Undirected Graph",
        "difficulty": "Medium",
        "tags": ["Graph", "Union Find", "Depth-First Search"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "countComponents",
        "params": ["n", "edges"],
        "description": """
Return the number of connected components in the undirected graph.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": ["Start a traversal from every unvisited node, or union every edge and count distinct roots."],
        "tests": [
            {"input": [5, [[0, 1], [1, 2], [3, 4]]], "output": 2, "sample": True},
            {"input": [5, [[0, 1], [1, 2], [2, 3], [3, 4]]], "output": 1, "sample": True},
            {"input": [3, []], "output": 3},
            {"input": [1, []], "output": 1},
        ],
    },
    {
        "id": 168,
        "slug": "graph-valid-tree",
        "title": "Graph Valid Tree",
        "difficulty": "Medium",
        "tags": ["Graph", "Union Find", "Breadth-First Search"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "validTree",
        "params": ["n", "edges"],
        "description": """
Return whether the undirected graph is a tree: connected and free of cycles.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": ["A tree on `n` nodes has exactly `n - 1` edges and is connected — check both."],
        "tests": [
            {"input": [5, [[0, 1], [0, 2], [0, 3], [1, 4]]], "output": True, "sample": True},
            {"input": [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]], "output": False, "sample": True},
            {"input": [1, []], "output": True},
            {"input": [2, []], "output": False},
        ],
    },
    {
        "id": 169,
        "slug": "flood-fill",
        "title": "Flood Fill",
        "difficulty": "Easy",
        "tags": ["Array", "Matrix", "Depth-First Search"],
        "complexity": "O(m * n) time, O(m * n) space",
        "functionName": "floodFill",
        "params": ["image", "sr", "sc", "color"],
        "description": """
Repaint the pixel at `(sr, sc)` and every pixel connected to it through up/down/left/right neighbours of the same original colour. Return the image.

**Constraints**

- `1 <= m, n <= 100`
- `0 <= pixel value, color < 2^16`
""",
        "hints": ["Return early when the start pixel is already the target colour, or the fill never stops."],
        "tests": [
            {"input": [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2],
             "output": [[2, 2, 2], [2, 2, 0], [2, 0, 1]], "sample": True},
            {"input": [[[0, 0], [0, 0]], 0, 0, 0], "output": [[0, 0], [0, 0]], "sample": True},
            {"input": [[[1]], 0, 0, 2], "output": [[2]]},
            {"input": [[[1, 2], [2, 1]], 0, 0, 3], "output": [[3, 2], [2, 1]]},
        ],
    },
    {
        "id": 170,
        "slug": "rotting-oranges",
        "title": "Rotting Oranges",
        "difficulty": "Medium",
        "tags": ["Array", "Matrix", "Breadth-First Search"],
        "complexity": "O(m * n) time, O(m * n) space",
        "functionName": "orangesRotting",
        "params": ["grid"],
        "description": """
`0` is empty, `1` is a fresh orange and `2` is a rotten one. Every minute, a rotten orange rots each fresh orange directly beside it. Return the minutes until no fresh orange is left, or `-1` if that never happens.

**Constraints**

- `1 <= m, n <= 300`
- Values are `0`, `1` or `2`
""",
        "hints": [
            "Start the BFS from every rotten orange at once — a multi-source BFS.",
            "Count the fresh oranges up front so you can tell whether any survive.",
        ],
        "tests": [
            {"input": [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], "output": 4, "sample": True},
            {"input": [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]], "output": -1, "sample": True},
            {"input": [[[0, 2]]], "output": 0},
            {"input": [[[1]]], "output": -1},
        ],
    },
    {
        "id": 171,
        "slug": "pacific-atlantic-water-flow",
        "title": "Pacific Atlantic Water Flow",
        "difficulty": "Medium",
        "tags": ["Array", "Matrix", "Depth-First Search"],
        "complexity": "O(m * n) time, O(m * n) space",
        "functionName": "pacificAtlantic",
        "params": ["heights"],
        "compare": "unordered2d",
        "description": """
The Pacific touches the top and left edges, the Atlantic the bottom and right edges. Water flows from a cell to a neighbour of equal or lower height. Return every cell `[row, col]` from which water can reach both oceans, in any order.

**Constraints**

- `1 <= m, n <= 200`
- `0 <= height <= 10^5`
""",
        "hints": [
            "Searching forward from every cell is too slow — search backwards from the edges instead.",
            "Flood inland from each ocean, moving only to cells of equal or greater height, then intersect.",
        ],
        "tests": [
            {"input": [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]],
             "output": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], "sample": True},
            {"input": [[[1]]], "output": [[0, 0]], "sample": True},
            {"input": [[[1, 1], [1, 1]]], "output": [[0, 0], [0, 1], [1, 0], [1, 1]]},
            {"input": [[[3, 3, 3], [3, 1, 3], [3, 3, 3]]],
             "output": [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]},
        ],
    },
    {
        "id": 172,
        "slug": "alien-dictionary",
        "title": "Alien Dictionary",
        "difficulty": "Hard",
        "tags": ["Graph", "Topological Sort", "String"],
        "complexity": "O(total characters) time, O(1) space",
        "functionName": "alienOrder",
        "params": ["words"],
        "description": """
`words` is sorted according to an unknown alphabet that uses lowercase English letters. Return that alphabet as a string, or `""` when the ordering is contradictory.

When several alphabets fit, return the **lexicographically smallest** one, so the answer is unique.

**Constraints**

- `1 <= words.length <= 100`
- `1 <= word length <= 20`
""",
        "hints": [
            "Compare each adjacent pair of words: the first differing letter gives one ordering edge.",
            "A word followed by a strict prefix of itself is contradictory — return `\"\"`.",
        ],
        "tests": [
            {"input": [["wrt", "wrf", "er", "ett", "rftt"]], "output": "wertf", "sample": True},
            {"input": [["z", "x", "z"]], "output": "", "sample": True},
            {"input": [["abc", "ab"]], "output": ""},
            {"input": [["z", "x"]], "output": "zx"},
        ],
    },
    {
        "id": 173,
        "slug": "dijkstras-algorithm",
        "title": "Dijkstra's Algorithm",
        "difficulty": "Medium",
        "tags": ["Graph", "Heap", "Shortest Path"],
        "complexity": "O((n + e) log n) time, O(n) space",
        "functionName": "dijkstra",
        "params": ["n", "edges", "source"],
        "description": """
Each edge is `[a, b, weight]` in an undirected weighted graph with non-negative weights. Return the shortest distance from `source` to every node, using `-1` for nodes that cannot be reached.

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `0 <= weight <= 10^4`
""",
        "hints": [
            "A min-heap keyed by distance; skip an entry when it is already worse than the recorded distance.",
            "With non-negative weights, the first time a node comes off the heap its distance is final.",
        ],
        "tests": [
            {"input": [3, [[0, 1, 1], [1, 2, 3], [0, 2, 6]], 0], "output": [0, 1, 4], "sample": True},
            {"input": [3, [[0, 1, 5]], 0], "output": [0, 5, -1], "sample": True},
            {"input": [1, [], 0], "output": [0]},
            {"input": [2, [[0, 1, 0]], 1], "output": [0, 0]},
        ],
    },
    {
        "id": 174,
        "slug": "bellman-ford-algorithm",
        "title": "Bellman-Ford Algorithm",
        "difficulty": "Medium",
        "tags": ["Graph", "Dynamic Programming", "Shortest Path"],
        "complexity": "O(n * e) time, O(n) space",
        "functionName": "bellmanFord",
        "params": ["n", "edges", "source"],
        "description": """
Each edge is `[a, b, weight]` in a **directed** graph, and weights may be negative. Return the shortest distance from `source` to every node, using `-1` for unreachable nodes — or `[-1]` when the graph contains a negative cycle reachable from the source.

**Constraints**

- `1 <= n <= 500`
- `0 <= edges.length <= 5000`
- `-1000 <= weight <= 1000`
""",
        "hints": [
            "Relax every edge `n - 1` times; that is enough for any shortest path without a negative cycle.",
            "One more round that still improves something proves a negative cycle exists.",
        ],
        "tests": [
            {"input": [3, [[0, 1, 5], [1, 2, -2], [0, 2, 10]], 0], "output": [0, 5, 3], "sample": True},
            {"input": [3, [[0, 1, 1], [1, 2, -1], [2, 1, -1]], 0], "output": [-1], "sample": True},
            {"input": [2, [], 0], "output": [0, -1]},
            {"input": [1, [], 0], "output": [0]},
        ],
    },
    {
        "id": 175,
        "slug": "floyd-warshall-algorithm",
        "title": "Floyd-Warshall Algorithm",
        "difficulty": "Medium",
        "tags": ["Graph", "Dynamic Programming", "Shortest Path"],
        "complexity": "O(n^3) time, O(n^2) space",
        "functionName": "floydWarshall",
        "params": ["matrix"],
        "checkArg": 0,
        "description": """
`matrix[i][j]` is the weight of the edge from `i` to `j`, with `-1` meaning there is no edge and `matrix[i][i] == 0`. Rewrite the matrix in place so each entry holds the shortest distance, keeping `-1` where no path exists.

**Constraints**

- `1 <= n <= 120`
- `-1000 <= weight <= 1000`, and no negative cycles
""",
        "hints": [
            "Three nested loops with the intermediate node `k` on the **outside**.",
            "Swap `-1` for infinity while you work and put it back at the end.",
        ],
        "tests": [
            {"input": [[[0, 1, 43], [1, 0, 6], [-1, -1, 0]]], "output": [[0, 1, 7], [1, 0, 6], [-1, -1, 0]],
             "sample": True},
            {"input": [[[0, -1], [-1, 0]]], "output": [[0, -1], [-1, 0]], "sample": True},
            {"input": [[[0]]], "output": [[0]]},
            {"input": [[[0, 5, -1], [-1, 0, 2], [-1, -1, 0]]], "output": [[0, 5, 7], [-1, 0, 2], [-1, -1, 0]]},
        ],
    },
    {
        "id": 176,
        "slug": "minimum-spanning-tree-prims",
        "title": "Minimum Spanning Tree (Prim's)",
        "difficulty": "Medium",
        "tags": ["Graph", "Heap", "Minimum Spanning Tree"],
        "complexity": "O((n + e) log n) time, O(n) space",
        "functionName": "spanningTree",
        "params": ["n", "edges"],
        "description": """
Each edge is `[a, b, weight]` in a connected undirected graph. Return the total weight of a minimum spanning tree.

**Constraints**

- `1 <= n <= 10^5`
- `n - 1 <= edges.length <= 2 * 10^5`
- `0 <= weight <= 10^4`
- The graph is connected
""",
        "hints": [
            "Grow one tree: repeatedly take the cheapest edge leaving the nodes already added.",
            "A min-heap of candidate edges keyed by weight does exactly that.",
        ],
        "tests": [
            {"input": [3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]], "output": 4, "sample": True},
            {"input": [2, [[0, 1, 7]]], "output": 7, "sample": True},
            {"input": [1, []], "output": 0},
            {"input": [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]]], "output": 3},
        ],
    },
    {
        "id": 177,
        "slug": "minimum-spanning-tree-kruskals",
        "title": "Minimum Spanning Tree (Kruskal's)",
        "difficulty": "Medium",
        "tags": ["Graph", "Union Find", "Minimum Spanning Tree", "Sorting"],
        "complexity": "O(e log e) time, O(n) space",
        "functionName": "kruskalMST",
        "params": ["n", "edges"],
        "description": """
Each edge is `[a, b, weight]` in a connected undirected graph. Return the total weight of a minimum spanning tree, built by taking edges in increasing weight.

**Constraints**

- `1 <= n <= 10^5`
- `n - 1 <= edges.length <= 2 * 10^5`
- `0 <= weight <= 10^4`
- The graph is connected
""",
        "hints": [
            "Sort the edges and keep each one whose endpoints are not already connected.",
            "Union-find with path compression makes the connectivity test near constant time.",
        ],
        "tests": [
            {"input": [3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]], "output": 4, "sample": True},
            {"input": [2, [[0, 1, 7]]], "output": 7, "sample": True},
            {"input": [1, []], "output": 0},
            {"input": [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]]], "output": 3},
        ],
    },
    {
        "id": 178,
        "slug": "strongly-connected-components",
        "title": "Strongly Connected Components",
        "difficulty": "Hard",
        "tags": ["Graph", "Depth-First Search"],
        "complexity": "O(n + e) time, O(n) space",
        "functionName": "countSCC",
        "params": ["n", "edges"],
        "description": """
Each edge `[a, b]` points from `a` to `b`. Return the number of strongly connected components — maximal groups in which every node can reach every other.

""" + EDGE_NOTE + """

**Constraints**

- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
""",
        "hints": [
            "Kosaraju: order nodes by DFS finish time, then DFS the reversed graph in that order.",
            "Each traversal of the reversed graph collects exactly one component.",
        ],
        "tests": [
            {"input": [5, [[0, 2], [2, 1], [1, 0], [0, 3], [3, 4]]], "output": 3, "sample": True},
            {"input": [3, [[0, 1], [1, 2], [2, 0]]], "output": 1, "sample": True},
            {"input": [3, []], "output": 3},
            {"input": [1, [[0, 0]]], "output": 1},
        ],
    },
    {
        "id": 179,
        "slug": "word-search-ii",
        "title": "Word Search II",
        "difficulty": "Hard",
        "tags": ["Array", "Matrix", "Trie", "Backtracking"],
        "complexity": "O(m * n * 4^L) worst case, O(total word length) space",
        "functionName": "findWords",
        "params": ["board", "words"],
        "compare": "unordered",
        "description": """
Return every word from `words` that can be spelled by walking the board through up/down/left/right neighbours without reusing a cell. Any order is fine.

**Constraints**

- `1 <= m, n <= 12`
- `1 <= words.length <= 3 * 10^4`
- `1 <= word length <= 10`, lowercase letters
""",
        "hints": [
            "Searching each word separately re-walks the board; put the words in a trie and search once.",
            "Prune trie branches once they are exhausted so long searches stop early.",
        ],
        "tests": [
            {"input": [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                       ["oath", "pea", "eat", "rain"]], "output": ["oath", "eat"], "sample": True},
            {"input": [[["a", "b"], ["c", "d"]], ["abcb"]], "output": [], "sample": True},
            {"input": [[["a"]], ["a"]], "output": ["a"]},
            {"input": [[["a", "b"]], ["ab", "ba", "b"]], "output": ["ab", "ba", "b"],
             "explanation": "\"ba\" walks right-to-left."},
        ],
    },
]
