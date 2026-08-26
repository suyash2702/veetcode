def isSameTree(p, q):
    if p is None or q is None:
        return p is None and q is None
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
