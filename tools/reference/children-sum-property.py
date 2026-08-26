def changeTree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    children = (root.left.val if root.left else 0) + (root.right.val if root.right else 0)
    if children >= root.val:
        root.val = children
    else:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val

    changeTree(root.left)
    changeTree(root.right)

    total = (root.left.val if root.left else 0) + (root.right.val if root.right else 0)
    if root.left or root.right:
        root.val = total
    return root
