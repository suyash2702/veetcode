def lowestCommonAncestor(root, p, q):
    def walk(node):
        if node is None or node.val == p or node.val == q:
            return node
        left = walk(node.left)
        right = walk(node.right)
        if left and right:
            return node
        return left or right

    found = walk(root)
    return found.val if found else None
