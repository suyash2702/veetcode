"""Recursion and backtracking problems from the sheets."""

PROBLEMS = [
    {
        "id": 199,
        "slug": "permutations",
        "title": "Permutations",
        "difficulty": "Medium",
        "tags": ["Array", "Backtracking"],
        "complexity": "O(n * n!) time, O(n) extra space",
        "functionName": "permute",
        "params": ["nums"],
        "compare": "unordered",
        "description": """
Return all permutations of the distinct integers in `nums`, in any order.

**Constraints**

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`, all distinct
""",
        "hints": [
            "Swap each remaining element into the current position and recurse on the rest.",
            "Swapping in place avoids the extra used-array and the copying that comes with it.",
        ],
        "tests": [
            {"input": [[1, 2, 3]], "output": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
             "sample": True},
            {"input": [[0, 1]], "output": [[0, 1], [1, 0]], "sample": True},
            {"input": [[1]], "output": [[1]]},
            {"input": [[-1, 2]], "output": [[-1, 2], [2, -1]]},
        ],
    },
    {
        "id": 200,
        "slug": "subsets-ii",
        "title": "Subsets II",
        "difficulty": "Medium",
        "tags": ["Array", "Backtracking", "Bit Manipulation"],
        "complexity": "O(n * 2^n) time, O(n) extra space",
        "functionName": "subsetsWithDup",
        "params": ["nums"],
        "compare": "unordered2d",
        "description": """
`nums` may contain duplicates. Return all possible subsets without any duplicate subset, in any order.

**Constraints**

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
""",
        "hints": [
            "Sort first so equal values sit together.",
            "At each level, skip a value equal to its predecessor — that is what stops duplicate subsets.",
        ],
        "tests": [
            {"input": [[1, 2, 2]], "output": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], "sample": True},
            {"input": [[0]], "output": [[], [0]], "sample": True},
            {"input": [[1, 1]], "output": [[], [1], [1, 1]]},
            {"input": [[4, 4, 4, 1, 4]], "output": [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4],
                                                    [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]},
        ],
    },
    {
        "id": 201,
        "slug": "subset-sums",
        "title": "Subset Sums",
        "difficulty": "Easy",
        "tags": ["Array", "Backtracking", "Recursion"],
        "complexity": "O(2^n) time, O(n) extra space",
        "functionName": "subsetSums",
        "params": ["nums"],
        "compare": "unordered",
        "description": """
Return the sums of all `2^n` subsets of `nums`, in any order. The empty subset contributes `0`.

**Constraints**

- `1 <= nums.length <= 15`
- `0 <= nums[i] <= 10^4`
""",
        "hints": ["At each index, recurse twice: once taking the value into the running sum, once skipping it."],
        "tests": [
            {"input": [[2, 3]], "output": [0, 2, 3, 5], "sample": True},
            {"input": [[5, 2, 1]], "output": [0, 1, 2, 3, 5, 6, 7, 8], "sample": True},
            {"input": [[0]], "output": [0, 0]},
            {"input": [[1, 1]], "output": [0, 1, 1, 2]},
        ],
    },
    {
        "id": 202,
        "slug": "power-set",
        "title": "Power Set",
        "difficulty": "Medium",
        "tags": ["String", "Bit Manipulation", "Backtracking"],
        "complexity": "O(n * 2^n) time",
        "functionName": "powerSet",
        "params": ["s"],
        "compare": "unordered",
        "description": """
Return every non-empty subsequence of the string `s`, in any order. Characters keep their original relative order inside each subsequence.

**Constraints**

- `1 <= s.length <= 16`
- Lowercase English letters, all distinct
""",
        "hints": ["Every bitmask from `1` to `2^n - 1` picks one subsequence — bit `i` keeps character `i`."],
        "tests": [
            {"input": ["abc"], "output": ["a", "b", "c", "ab", "ac", "bc", "abc"], "sample": True},
            {"input": ["ab"], "output": ["a", "b", "ab"], "sample": True},
            {"input": ["a"], "output": ["a"]},
            {"input": ["xy"], "output": ["x", "y", "xy"]},
        ],
    },
    {
        "id": 203,
        "slug": "combination-sum",
        "title": "Combination Sum",
        "difficulty": "Medium",
        "tags": ["Array", "Backtracking"],
        "complexity": "O(n^(target/min)) time",
        "functionName": "combinationSum",
        "params": ["candidates", "target"],
        "compare": "unordered2d",
        "description": """
`candidates` holds distinct values, each usable any number of times. Return every unique combination that sums to `target`, in any order.

**Constraints**

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`, all distinct
- `1 <= target <= 40`
""",
        "hints": [
            "At each step, either reuse the current candidate or move past it for good.",
            "Never stepping backwards is what keeps the combinations unique.",
        ],
        "tests": [
            {"input": [[2, 3, 6, 7], 7], "output": [[2, 2, 3], [7]], "sample": True},
            {"input": [[2, 3, 5], 8], "output": [[2, 2, 2, 2], [2, 3, 3], [3, 5]], "sample": True},
            {"input": [[2], 1], "output": []},
            {"input": [[3], 9], "output": [[3, 3, 3]]},
        ],
    },
    {
        "id": 204,
        "slug": "combination-sum-ii",
        "title": "Combination Sum II",
        "difficulty": "Medium",
        "tags": ["Array", "Backtracking"],
        "complexity": "O(2^n) time",
        "functionName": "combinationSum2",
        "params": ["candidates", "target"],
        "compare": "unordered2d",
        "description": """
Each candidate may be used **once**, and `candidates` may contain duplicates. Return every unique combination summing to `target`, in any order.

**Constraints**

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`
""",
        "hints": ["Sort, then at each level skip values equal to the previous one to avoid repeating a combination."],
        "tests": [
            {"input": [[10, 1, 2, 7, 6, 1, 5], 8], "output": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], "sample": True},
            {"input": [[2, 5, 2, 1, 2], 5], "output": [[1, 2, 2], [5]], "sample": True},
            {"input": [[1], 2], "output": []},
            {"input": [[1, 1], 2], "output": [[1, 1]]},
        ],
    },
    {
        "id": 205,
        "slug": "palindrome-partitioning",
        "title": "Palindrome Partitioning",
        "difficulty": "Medium",
        "tags": ["String", "Backtracking", "Dynamic Programming"],
        "complexity": "O(n * 2^n) time",
        "functionName": "partition",
        "params": ["s"],
        "compare": "unordered",
        "description": """
Return every way to cut `s` into pieces where each piece is a palindrome, in any order. The pieces of one partition must stay in order.

**Constraints**

- `1 <= s.length <= 16`
- Lowercase English letters
""",
        "hints": ["Try every palindromic prefix, recurse on the rest, and undo the choice on the way back."],
        "tests": [
            {"input": ["aab"], "output": [["a", "a", "b"], ["aa", "b"]], "sample": True},
            {"input": ["a"], "output": [["a"]], "sample": True},
            {"input": ["ab"], "output": [["a", "b"]]},
            {"input": ["aba"], "output": [["a", "b", "a"], ["aba"]]},
        ],
    },
    {
        "id": 206,
        "slug": "permutation-sequence",
        "title": "Permutation Sequence",
        "difficulty": "Hard",
        "tags": ["Math", "Recursion"],
        "complexity": "O(n^2) time, O(n) space",
        "functionName": "getPermutation",
        "params": ["n", "k"],
        "description": """
List the permutations of `1..n` in lexicographic order and return the `k`-th one as a string. Generating them all is too slow — compute it directly.

**Constraints**

- `1 <= n <= 9`
- `1 <= k <= n!`
""",
        "hints": [
            "Fixing the first digit fixes a block of `(n - 1)!` permutations.",
            "Dividing `k - 1` by that factorial picks the digit; the remainder recurses into the rest.",
        ],
        "tests": [
            {"input": [3, 3], "output": "213", "sample": True},
            {"input": [4, 9], "output": "2314", "sample": True},
            {"input": [1, 1], "output": "1"},
            {"input": [3, 1], "output": "123"},
        ],
    },
    {
        "id": 207,
        "slug": "n-queens",
        "title": "N-Queens",
        "difficulty": "Hard",
        "tags": ["Backtracking", "Array"],
        "complexity": "O(n!) time, O(n) space",
        "functionName": "solveNQueens",
        "params": ["n"],
        "compare": "unordered",
        "description": """
Place `n` queens on an `n x n` board so no two attack each other. Return every distinct solution as a list of board rows, where `'Q'` is a queen and `'.'` is empty. Solutions may be returned in any order, but the rows of a board must be top to bottom.

**Constraints**

- `1 <= n <= 9`
""",
        "hints": [
            "Place one queen per row and track which columns and diagonals are taken.",
            "A diagonal is identified by `row - col`, an anti-diagonal by `row + col`.",
        ],
        "tests": [
            {"input": [4], "output": [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
             "sample": True},
            {"input": [1], "output": [["Q"]], "sample": True},
            {"input": [2], "output": []},
            {"input": [3], "output": []},
        ],
    },
    {
        "id": 208,
        "slug": "sudoku-solver",
        "title": "Sudoku Solver",
        "difficulty": "Hard",
        "tags": ["Backtracking", "Matrix", "Hash Table"],
        "complexity": "Exponential worst case, O(1) space",
        "functionName": "solveSudoku",
        "params": ["board"],
        "checkArg": 0,
        "description": """
Fill the `9 x 9` board in place so every row, column and `3 x 3` box holds the digits `1`-`9` exactly once. Empty cells are `'.'`, and the puzzle has exactly one solution.

**Constraints**

- The board is `9 x 9` and holds digit characters or `'.'`
""",
        "hints": [
            "Track the used digits per row, column and box so validity is a constant-time check.",
            "Filling the most constrained cell first prunes the search hard.",
        ],
        "tests": [
            {"input": [[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]],
             "output": [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]], "sample": True},
        ],
    },
    {
        "id": 209,
        "slug": "m-coloring-problem",
        "title": "M-Coloring Problem",
        "difficulty": "Medium",
        "tags": ["Graph", "Backtracking"],
        "complexity": "O(m^n) worst case, O(n) space",
        "functionName": "graphColoring",
        "params": ["n", "edges", "m"],
        "description": """
Return whether the undirected graph's nodes can be coloured with at most `m` colours so that no edge joins two nodes of the same colour.

**Constraints**

- `1 <= n <= 20`
- `1 <= m <= n`
- Nodes are numbered `0` to `n - 1`
""",
        "hints": [
            "Colour the nodes one at a time, trying every colour not used by a neighbour.",
            "Backtrack as soon as a node has no legal colour left.",
        ],
        "tests": [
            {"input": [4, [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]], 3], "output": True, "sample": True},
            {"input": [3, [[0, 1], [1, 2], [2, 0]], 2], "output": False, "sample": True},
            {"input": [1, [], 1], "output": True},
            {"input": [4, [[0, 1], [1, 2], [2, 3], [3, 0]], 2], "output": True},
        ],
    },
    {
        "id": 210,
        "slug": "rat-in-a-maze",
        "title": "Rat in a Maze",
        "difficulty": "Medium",
        "tags": ["Matrix", "Backtracking"],
        "complexity": "O(4^(n*n)) worst case, O(n*n) space",
        "functionName": "findPaths",
        "params": ["maze"],
        "compare": "unordered",
        "description": """
A rat starts at `(0, 0)` and must reach `(n - 1, n - 1)`. A cell holding `1` is open and `0` is blocked; a cell may be used once per path. Return every path as a string of moves — `'D'`, `'L'`, `'R'`, `'U'` — in any order.

Return an empty list when no path exists, including when the start or the destination is blocked.

**Constraints**

- `1 <= n <= 5`
- Cells are `0` or `1`
""",
        "hints": [
            "Try the moves in the order D, L, R, U and mark cells as you enter them.",
            "Unmark on the way back out, or later paths will see cells as blocked.",
        ],
        "tests": [
            {"input": [[[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]],
             "output": ["DDRDRR", "DRDDRR"], "sample": True},
            {"input": [[[1, 0], [1, 0]]], "output": [], "sample": True},
            {"input": [[[1]]], "output": [""]},
            {"input": [[[1, 1], [1, 1]]], "output": ["DR", "RD"]},
        ],
    },
]
