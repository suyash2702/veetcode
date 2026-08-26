from collections import deque


def bfsOfGraph(adj):
    seen = [False] * len(adj)
    seen[0] = True
    queue = deque([0])
    out = []
    while queue:
        node = queue.popleft()
        out.append(node)
        for neighbour in adj[node]:
            if not seen[neighbour]:
                seen[neighbour] = True
                queue.append(neighbour)
    return out
