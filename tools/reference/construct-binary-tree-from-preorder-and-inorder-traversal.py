def buildTree(preorder, inorder):
    position = {value: i for i, value in enumerate(inorder)}
    index = [0]

    def build(lo, hi):
        if lo > hi:
            return None
        value = preorder[index[0]]
        index[0] += 1
        node = TreeNode(value)
        mid = position[value]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder) - 1)
