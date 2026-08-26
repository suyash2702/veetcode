def bToDLL(root):
    head = [None]
    prev = [None]

    def walk(node):
        if node is None:
            return
        walk(node.left)
        if prev[0] is None:
            head[0] = node
        else:
            prev[0].right = node
            node.left = prev[0]
        prev[0] = node
        walk(node.right)

    walk(root)
    if prev[0] is not None:
        prev[0].right = None
    if head[0] is not None:
        head[0].left = None
    return head[0]
