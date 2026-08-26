def rootToNodePath(root, target):
    path = []

    def walk(node):
        if node is None:
            return False
        path.append(node.val)
        if node.val == target or walk(node.left) or walk(node.right):
            return True
        path.pop()
        return False

    return path if walk(root) else []
