def largestBst(root):
    best = [0]

    def walk(node):
        """(size, min, max, is_bst) for this subtree."""
        if node is None:
            return 0, float("inf"), float("-inf"), True
        left_size, left_min, left_max, left_bst = walk(node.left)
        right_size, right_min, right_max, right_bst = walk(node.right)
        if left_bst and right_bst and left_max < node.val < right_min:
            size = left_size + right_size + 1
            best[0] = max(best[0], size)
            return size, min(left_min, node.val), max(right_max, node.val), True
        return 0, float("-inf"), float("inf"), False

    walk(root)
    return best[0]
