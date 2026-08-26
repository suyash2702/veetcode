def flatten(root):
    node = root
    while node:
        if node.left:
            rightmost = node.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = node.right
            node.right = node.left
            node.left = None
        node = node.right
