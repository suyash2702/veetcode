def countNodes(root):
    def depth(node, go_left):
        count = 0
        while node:
            count += 1
            node = node.left if go_left else node.right
        return count

    if root is None:
        return 0
    left = depth(root, True)
    right = depth(root, False)
    if left == right:
        return (1 << left) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)
