def floorCeil(root, key):
    floor_value = ceil_value = -1
    node = root
    while node:
        if node.val == key:
            return [key, key]
        if node.val < key:
            floor_value = node.val
            node = node.right
        else:
            ceil_value = node.val
            node = node.left
    return [floor_value, ceil_value]
