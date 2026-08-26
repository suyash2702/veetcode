class _Trie:
    __slots__ = ("children",)

    def __init__(self):
        self.children = [None, None]


def maximizeXor(nums, queries):
    values = sorted(nums)
    order = sorted(range(len(queries)), key=lambda i: queries[i][1])
    root = _Trie()
    added = 0
    out = [-1] * len(queries)

    def insert(value):
        node = root
        for bit in range(29, -1, -1):
            index = (value >> bit) & 1
            if node.children[index] is None:
                node.children[index] = _Trie()
            node = node.children[index]

    def best_xor(value):
        node = root
        total = 0
        for bit in range(29, -1, -1):
            index = (value >> bit) & 1
            preferred = node.children[1 - index]
            if preferred is not None:
                total |= 1 << bit
                node = preferred
            else:
                node = node.children[index]
        return total

    for i in order:
        x, limit = queries[i]
        while added < len(values) and values[added] <= limit:
            insert(values[added])
            added += 1
        out[i] = best_xor(x) if added else -1
    return out
