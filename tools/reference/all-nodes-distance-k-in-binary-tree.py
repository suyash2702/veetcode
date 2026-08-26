from collections import deque


def distanceK(root, target, k):
    parents = {}
    start = [None]

    def walk(node, parent):
        if node is None:
            return
        parents[node] = parent
        if node.val == target:
            start[0] = node
        walk(node.left, node)
        walk(node.right, node)

    walk(root, None)
    if start[0] is None:
        return []

    seen = {start[0]}
    queue = deque([start[0]])
    distance = 0
    while queue:
        if distance == k:
            return [node.val for node in queue]
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in (node.left, node.right, parents[node]):
                if neighbour and neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)
        distance += 1
    return []
