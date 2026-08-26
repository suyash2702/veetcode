def searchBST(root, val):
    node = root
    while node and node.val != val:
        node = node.left if val < node.val else node.right
    return node
