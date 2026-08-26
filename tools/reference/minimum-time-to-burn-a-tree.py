from collections import deque


def timeToBurnTree(root, start):
    parents = {}
    source = [None]

    def walk(node, parent):
        if node is None:
            return
        parents[node] = parent
        if node.val == start:
            source[0] = node
        walk(node.left, node)
        walk(node.right, node)

    walk(root, None)
    if source[0] is None:
        return 0

    seen = {source[0]}
    queue = deque([source[0]])
    seconds = -1
    while queue:
        seconds += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in (node.left, node.right, parents[node]):
                if neighbour and neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)
    return seconds
