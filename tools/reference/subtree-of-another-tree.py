def isSubtree(root, subRoot):
    def same(a, b):
        if a is None or b is None:
            return a is None and b is None
        return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

    if root is None:
        return subRoot is None
    if same(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
