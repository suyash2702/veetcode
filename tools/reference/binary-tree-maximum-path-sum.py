def maxPathSum(root):
    best = [float("-inf")]

    def down(node):
        if node is None:
            return 0
        left = max(down(node.left), 0)
        right = max(down(node.right), 0)
        best[0] = max(best[0], node.val + left + right)
        return node.val + max(left, right)

    down(root)
    return best[0]
