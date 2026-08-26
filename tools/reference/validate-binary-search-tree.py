def isValidBST(root):
    def walk(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return walk(node.left, low, node.val) and walk(node.right, node.val, high)

    return walk(root, float('-inf'), float('inf'))
