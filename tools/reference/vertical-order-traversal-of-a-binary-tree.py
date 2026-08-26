def verticalTraversal(root):
    triples = []

    def walk(node, row, column):
        if node is None:
            return
        triples.append((column, row, node.val))
        walk(node.left, row + 1, column - 1)
        walk(node.right, row + 1, column + 1)

    walk(root, 0, 0)
    triples.sort()
    out = []
    last_column = None
    for column, _, value in triples:
        if column != last_column:
            out.append([])
            last_column = column
        out[-1].append(value)
    return out
