def boundaryTraversal(root):
    if root is None:
        return []

    def is_leaf(node):
        return node.left is None and node.right is None

    out = [root.val] if not is_leaf(root) else []

    node = root.left
    while node:
        if not is_leaf(node):
            out.append(node.val)
        node = node.left or node.right

    def leaves(node):
        if node is None:
            return
        if is_leaf(node):
            out.append(node.val)
            return
        leaves(node.left)
        leaves(node.right)

    leaves(root)

    right_side = []
    node = root.right
    while node:
        if not is_leaf(node):
            right_side.append(node.val)
        node = node.right or node.left
    out.extend(reversed(right_side))
    return out
