def findPreSuc(root, key):
    predecessor = successor = -1
    node = root
    while node:
        if node.val < key:
            predecessor = node.val
            node = node.right
        else:
            node = node.left
    node = root
    while node:
        if node.val > key:
            successor = node.val
            node = node.left
        else:
            node = node.right
    return [predecessor, successor]
