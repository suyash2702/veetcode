def buildTree(inorder, postorder):
    position = {value: i for i, value in enumerate(inorder)}
    index = [len(postorder) - 1]

    def build(lo, hi):
        if lo > hi:
            return None
        value = postorder[index[0]]
        index[0] -= 1
        node = TreeNode(value)
        mid = position[value]
        node.right = build(mid + 1, hi)
        node.left = build(lo, mid - 1)
        return node

    return build(0, len(inorder) - 1)
