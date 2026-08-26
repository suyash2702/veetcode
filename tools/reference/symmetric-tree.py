def isSymmetric(root):
    def mirror(a, b):
        if a is None or b is None:
            return a is None and b is None
        return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)

    return root is None or mirror(root.left, root.right)
