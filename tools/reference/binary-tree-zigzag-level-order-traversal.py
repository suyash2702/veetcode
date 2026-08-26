def zigzagLevelOrder(root):
    if root is None:
        return []
    out, level, left_to_right = [], [root], True
    while level:
        values = [node.val for node in level]
        out.append(values if left_to_right else values[::-1])
        left_to_right = not left_to_right
        level = [child for node in level for child in (node.left, node.right) if child]
    return out
