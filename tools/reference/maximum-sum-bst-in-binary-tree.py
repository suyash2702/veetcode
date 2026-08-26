def maxSumBST(root):
    best = [0]

    def walk(node):
        """(sum, min, max, is_bst) for this subtree."""
        if node is None:
            return 0, float("inf"), float("-inf"), True
        left_sum, left_min, left_max, left_bst = walk(node.left)
        right_sum, right_min, right_max, right_bst = walk(node.right)
        if left_bst and right_bst and left_max < node.val < right_min:
            total = left_sum + right_sum + node.val
            best[0] = max(best[0], total)
            return total, min(left_min, node.val), max(right_max, node.val), True
        return 0, float("-inf"), float("inf"), False

    walk(root)
    return best[0]
