def topView(root):
    if root is None:
        return []
    seen = {}
    queue = [(root, 0)]
    head = 0
    while head < len(queue):
        node, column = queue[head]
        head += 1
        if column not in seen:
            seen[column] = node.val
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))
    return [seen[c] for c in sorted(seen)]
