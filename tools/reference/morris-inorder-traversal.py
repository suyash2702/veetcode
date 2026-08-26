def morrisInorder(root):
    out = []
    node = root
    while node:
        if node.left is None:
            out.append(node.val)
            node = node.right
            continue
        predecessor = node.left
        while predecessor.right and predecessor.right is not node:
            predecessor = predecessor.right
        if predecessor.right is None:
            predecessor.right = node
            node = node.left
        else:
            predecessor.right = None
            out.append(node.val)
            node = node.right
    return out
