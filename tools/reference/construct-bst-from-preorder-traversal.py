def bstFromPreorder(preorder):
    index = [0]

    def build(bound):
        if index[0] == len(preorder) or preorder[index[0]] > bound:
            return None
        node = TreeNode(preorder[index[0]])
        index[0] += 1
        node.left = build(node.val)
        node.right = build(bound)
        return node

    return build(float("inf"))
