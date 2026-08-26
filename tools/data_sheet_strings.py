"""Trie and string-algorithm problems from the sheets."""

PROBLEMS = [
    {
        "id": 211,
        "slug": "implement-trie-prefix-tree",
        "title": "Implement Trie (Prefix Tree)",
        "difficulty": "Medium",
        "tags": ["Trie", "Design", "String"],
        "complexity": "O(length) per operation",
        "functionName": "Trie",
        "params": [],
        "design": {
            "className": "Trie",
            "methods": [
                {"name": "Trie", "params": []},
                {"name": "insert", "params": ["word"]},
                {"name": "search", "params": ["word"]},
                {"name": "startsWith", "params": ["prefix"]},
            ],
        },
        "description": """
Implement a prefix tree:

- `insert(word)` — add a word.
- `search(word)` — whether the exact word was inserted.
- `startsWith(prefix)` — whether any inserted word starts with `prefix`.

**Constraints**

- `1 <= word.length, prefix.length <= 2000`
- Lowercase English letters
- At most `3 * 10^4` calls
""",
        "hints": ["Each node holds a child per letter plus a flag marking the end of a word."],
        "tests": [
            {"input": [["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
                       [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]],
             "output": [None, None, True, False, True, None, True], "sample": True},
            {"input": [["Trie", "search", "startsWith"], [[], ["a"], ["a"]]],
             "output": [None, False, False], "sample": True},
            {"input": [["Trie", "insert", "startsWith", "startsWith"], [[], ["ab"], ["abc"], ["a"]]],
             "output": [None, None, False, True]},
        ],
    },
    {
        "id": 212,
        "slug": "implement-trie-ii",
        "title": "Implement Trie II",
        "difficulty": "Medium",
        "tags": ["Trie", "Design", "String"],
        "complexity": "O(length) per operation",
        "functionName": "Trie",
        "params": [],
        "design": {
            "className": "Trie",
            "methods": [
                {"name": "Trie", "params": []},
                {"name": "insert", "params": ["word"]},
                {"name": "countWordsEqualTo", "params": ["word"]},
                {"name": "countWordsStartingWith", "params": ["prefix"]},
                {"name": "erase", "params": ["word"]},
            ],
        },
        "description": """
A trie that counts duplicates:

- `insert(word)` — add one copy.
- `countWordsEqualTo(word)` — how many copies of that exact word are stored.
- `countWordsStartingWith(prefix)` — how many stored words start with `prefix`.
- `erase(word)` — remove one copy; the word is guaranteed to be present.

**Constraints**

- `1 <= word.length, prefix.length <= 2000`
- Lowercase English letters
- At most `3 * 10^4` calls
""",
        "hints": ["Keep two counters per node: words ending here and words passing through."],
        "tests": [
            {"input": [["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith",
                        "erase", "countWordsEqualTo", "countWordsStartingWith"],
                       [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"]]],
             "output": [None, None, None, 2, 2, None, 1, 1], "sample": True},
            {"input": [["Trie", "countWordsEqualTo", "countWordsStartingWith"], [[], ["a"], ["a"]]],
             "output": [None, 0, 0], "sample": True},
            {"input": [["Trie", "insert", "insert", "erase", "countWordsStartingWith"],
                       [[], ["ab"], ["abc"], ["ab"], ["a"]]],
             "output": [None, None, None, None, 1]},
        ],
    },
    {
        "id": 213,
        "slug": "design-add-and-search-words-data-structure",
        "title": "Design Add and Search Words Data Structure",
        "difficulty": "Medium",
        "tags": ["Trie", "Design", "Depth-First Search"],
        "complexity": "O(length) to add, O(26^dots * length) to search",
        "functionName": "WordDictionary",
        "params": [],
        "design": {
            "className": "WordDictionary",
            "methods": [
                {"name": "WordDictionary", "params": []},
                {"name": "addWord", "params": ["word"]},
                {"name": "search", "params": ["word"]},
            ],
        },
        "description": """
- `addWord(word)` — store a word.
- `search(word)` — whether any stored word matches. A `'.'` in the query matches any single letter.

**Constraints**

- `1 <= word.length <= 25`
- Lowercase letters, and `'.'` only in queries (at most `3` per query)
- At most `10^4` calls
""",
        "hints": ["On a `'.'`, branch into every child; on a letter, follow the single edge."],
        "tests": [
            {"input": [["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
                       [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]],
             "output": [None, None, None, None, False, True, True, True], "sample": True},
            {"input": [["WordDictionary", "search"], [[], ["a"]]], "output": [None, False], "sample": True},
            {"input": [["WordDictionary", "addWord", "search", "search"], [[], ["a"], ["."], ["a."]]],
             "output": [None, None, True, False]},
        ],
    },
    {
        "id": 214,
        "slug": "longest-string-with-all-prefixes",
        "title": "Longest String with All Prefixes",
        "difficulty": "Medium",
        "tags": ["Trie", "String"],
        "complexity": "O(total characters) time",
        "functionName": "longestWordWithAllPrefixes",
        "params": ["words"],
        "description": """
Return the longest word from `words` such that every one of its prefixes is also present in `words`. When several words tie, return the lexicographically smallest; when none qualifies, return `""`.

**Constraints**

- `1 <= words.length <= 10^5`
- `1 <= word length <= 30`, lowercase letters
""",
        "hints": [
            "Insert everything into a trie, then walk down only through nodes that end a word.",
            "Visiting children in alphabetical order makes the tie-break fall out for free.",
        ],
        "tests": [
            {"input": [["n", "ni", "nin", "ninj", "ninja", "nil"]], "output": "ninja", "sample": True},
            {"input": [["ab", "a", "abc", "abcd"]], "output": "abcd", "sample": True},
            {"input": [["b", "ba", "bal"]], "output": "bal"},
            {"input": [["ab"]], "output": ""},
        ],
    },
    {
        "id": 215,
        "slug": "number-of-distinct-substrings",
        "title": "Number of Distinct Substrings",
        "difficulty": "Hard",
        "tags": ["Trie", "String", "Hash Table"],
        "complexity": "O(n^2) time with a trie",
        "functionName": "countDistinctSubstrings",
        "params": ["s"],
        "description": """
Count the distinct non-empty substrings of `s`.

**Constraints**

- `1 <= s.length <= 1000`
- Lowercase English letters
""",
        "hints": [
            "Insert every suffix into a trie; each new node created is one new substring.",
            "That counts every distinct substring exactly once without storing them.",
        ],
        "tests": [
            {"input": ["ababa"], "output": 9, "sample": True},
            {"input": ["ccfdf"], "output": 13, "sample": True,
             "explanation": "15 substrings in total, minus the repeats of \"c\" and \"f\"."},
            {"input": ["a"], "output": 1},
            {"input": ["aa"], "output": 2},
        ],
    },
    {
        "id": 216,
        "slug": "maximum-xor-of-two-numbers-in-an-array",
        "title": "Maximum XOR of Two Numbers in an Array",
        "difficulty": "Medium",
        "tags": ["Trie", "Bit Manipulation", "Array"],
        "complexity": "O(32 n) time, O(32 n) space",
        "functionName": "findMaximumXOR",
        "params": ["nums"],
        "description": """
Return the largest value of `nums[i] ^ nums[j]` over all pairs.

**Constraints**

- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 2^31 - 1`
""",
        "hints": [
            "Store the numbers in a binary trie, most significant bit first.",
            "For each number, walk the trie preferring the opposite bit at every step.",
        ],
        "tests": [
            {"input": [[3, 10, 5, 25, 2, 8]], "output": 28, "sample": True},
            {"input": [[0]], "output": 0, "sample": True},
            {"input": [[8, 10, 2]], "output": 10},
            {"input": [[2147483647, 0]], "output": 2147483647},
        ],
    },
    {
        "id": 217,
        "slug": "maximum-xor-with-an-element-from-array",
        "title": "Maximum XOR With an Element From Array",
        "difficulty": "Hard",
        "tags": ["Trie", "Bit Manipulation", "Sorting"],
        "complexity": "O((n + q) log n + 32(n + q)) time",
        "functionName": "maximizeXor",
        "params": ["nums", "queries"],
        "description": """
Each query is `[x, m]`: return the largest `nums[j] ^ x` over the elements of `nums` that are at most `m`, or `-1` when no element qualifies. Return one answer per query, in the order given.

**Constraints**

- `1 <= nums.length, queries.length <= 10^5`
- `0 <= nums[j], x, m <= 10^9`
""",
        "hints": [
            "Sort the numbers and the queries by their limit, then add numbers to the trie as the limit grows.",
            "That way every query sees exactly the elements it is allowed to use — offline processing.",
        ],
        "tests": [
            {"input": [[0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]], "output": [3, 3, 7], "sample": True},
            {"input": [[5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]], "output": [15, -1, 5], "sample": True},
            {"input": [[1], [[1, 0]]], "output": [-1]},
            {"input": [[1], [[1, 1]]], "output": [0]},
        ],
    },
    {
        "id": 218,
        "slug": "reverse-words-in-a-string",
        "title": "Reverse Words in a String",
        "difficulty": "Medium",
        "tags": ["String", "Two Pointers"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "reverseWords",
        "params": ["s"],
        "description": """
Return the words of `s` in reverse order, separated by a single space, with no leading or trailing spaces.

**Constraints**

- `1 <= s.length <= 10^4`
- `s` holds letters, digits and spaces
""",
        "hints": ["Split on runs of spaces, drop the empty pieces, reverse and join with one space."],
        "tests": [
            {"input": ["the sky is blue"], "output": "blue is sky the", "sample": True},
            {"input": ["  hello world  "], "output": "world hello", "sample": True},
            {"input": ["a good   example"], "output": "example good a"},
            {"input": ["single"], "output": "single"},
        ],
    },
    {
        "id": 219,
        "slug": "compare-version-numbers",
        "title": "Compare Version Numbers",
        "difficulty": "Medium",
        "tags": ["String", "Two Pointers"],
        "complexity": "O(n + m) time, O(1) space",
        "functionName": "compareVersion",
        "params": ["version1", "version2"],
        "description": """
Versions are dot-separated integers, and leading zeros are ignored (`1.01` equals `1.001`). A missing part counts as `0` (`1.0` equals `1`). Return `1` when `version1` is larger, `-1` when it is smaller, and `0` when they are equal.

**Constraints**

- `1 <= version.length <= 500`
- Digits and dots only, no leading or trailing dot
""",
        "hints": ["Walk both versions part by part, treating a missing part as zero."],
        "tests": [
            {"input": ["1.01", "1.001"], "output": 0, "sample": True},
            {"input": ["1.0", "1.0.0"], "output": 0, "sample": True},
            {"input": ["0.1", "1.1"], "output": -1},
            {"input": ["1.2", "1.10"], "output": -1},
        ],
    },
    {
        "id": 220,
        "slug": "rabin-karp",
        "title": "Rabin-Karp Pattern Search",
        "difficulty": "Medium",
        "tags": ["String", "String Matching", "Hashing"],
        "complexity": "O(n + m) expected time, O(1) space",
        "functionName": "searchPattern",
        "params": ["text", "pattern"],
        "description": """
Return every start index where `pattern` occurs in `text`, in increasing order. Occurrences may overlap.

The point of the exercise is the rolling hash: hash the pattern once, then slide a window over the text updating the hash in constant time and only comparing characters on a hash match.

**Constraints**

- `1 <= text.length <= 10^5`
- `1 <= pattern.length <= text.length`
- Lowercase English letters
""",
        "hints": [
            "Removing the leading character and appending the next one updates the hash in O(1).",
            "Always verify a hash match character by character — collisions happen.",
        ],
        "tests": [
            {"input": ["abcabcabc", "abc"], "output": [0, 3, 6], "sample": True},
            {"input": ["aaaa", "aa"], "output": [0, 1, 2], "sample": True},
            {"input": ["abcd", "e"], "output": []},
            {"input": ["a", "a"], "output": [0]},
        ],
    },
    {
        "id": 221,
        "slug": "z-algorithm",
        "title": "Z-Algorithm",
        "difficulty": "Medium",
        "tags": ["String", "String Matching"],
        "complexity": "O(n) time, O(n) space",
        "functionName": "zArray",
        "params": ["s"],
        "description": """
Return the Z-array of `s`: entry `i` is the length of the longest substring starting at `i` that is also a prefix of `s`. By convention entry `0` is the length of the whole string.

**Constraints**

- `1 <= s.length <= 10^5`
- Lowercase English letters
""",
        "hints": [
            "Keep the rightmost matching segment `[l, r]` seen so far.",
            "Inside that segment, the answer can be seeded from an earlier entry before extending.",
        ],
        "tests": [
            {"input": ["aabxaabxcaabxaabxay"],
             "output": [19, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0], "sample": True},
            {"input": ["aaaa"], "output": [4, 3, 2, 1], "sample": True},
            {"input": ["a"], "output": [1]},
            {"input": ["abc"], "output": [3, 0, 0]},
        ],
    },
    {
        "id": 222,
        "slug": "kmp-algorithm",
        "title": "KMP Pattern Search",
        "difficulty": "Medium",
        "tags": ["String", "String Matching"],
        "complexity": "O(n + m) time, O(m) space",
        "functionName": "kmpSearch",
        "params": ["text", "pattern"],
        "description": """
Return every start index where `pattern` occurs in `text`, in increasing order, using the KMP failure function. Occurrences may overlap.

**Constraints**

- `1 <= text.length <= 10^5`
- `1 <= pattern.length <= text.length`
- Lowercase English letters
""",
        "hints": [
            "The failure function stores, for each prefix, the length of its longest proper prefix that is also a suffix.",
            "On a mismatch, fall back through that table instead of restarting the scan.",
        ],
        "tests": [
            {"input": ["abcabcabc", "abc"], "output": [0, 3, 6], "sample": True},
            {"input": ["aaaa", "aa"], "output": [0, 1, 2], "sample": True},
            {"input": ["abcd", "e"], "output": []},
            {"input": ["a", "a"], "output": [0]},
        ],
    },
    {
        "id": 223,
        "slug": "encode-and-decode-strings",
        "title": "Encode and Decode Strings",
        "difficulty": "Medium",
        "tags": ["String", "Design"],
        "complexity": "O(total characters) time",
        "functionName": "codec",
        "params": ["strs"],
        "pyBody": """    # Write encode(strs) -> str and decode(data) -> list below, then leave
    # this line as the round trip the checker runs.
    return decode(encode(strs))


def encode(strs):
    # TODO: turn the list into one string
    pass


def decode(data):
    # TODO: rebuild the list from that string
    pass""",
        "jsBody": """  // Write encode(strs) and decode(data) below, then leave this line as the
  // round trip the checker runs.
  return decode(encode(strs));""",
        "description": """
Design an encoding that turns a list of strings into a single string, and a decoding that recovers the original list exactly. The strings may contain **any** characters, so no separator is safe on its own.

Write `encode(strs)` and `decode(data)`, and leave `codec(strs)` returning `decode(encode(strs))` — that round trip is what the checker calls.

**Constraints**

- `0 <= strs.length <= 200`
- `0 <= string length <= 200`
- Any ASCII characters, including separators and empty strings
""",
        "hints": [
            "Length-prefix each string, e.g. `4#word` — then the decoder never has to guess.",
            "Read the digits up to the delimiter, then take exactly that many characters.",
        ],
        "tests": [
            {"input": [["hello", "world"]], "output": ["hello", "world"], "sample": True},
            {"input": [[""]], "output": [""], "sample": True},
            {"input": [[]], "output": []},
            {"input": [["a#b", "3#x", ""]], "output": ["a#b", "3#x", ""]},
        ],
    },
]
