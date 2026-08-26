def widthOfBinaryTree(root):
    if root is None:
        return 0
    best = 0
    level = [(root, 0)]
    while level:
        first = level[0][1]
        best = max(best, level[-1][1] - first + 1)
        nxt = []
        for node, index in level:
            offset = index - first
            if node.left:
                nxt.append((node.left, 2 * offset))
            if node.right:
                nxt.append((node.right, 2 * offset + 1))
        level = nxt
    return best
