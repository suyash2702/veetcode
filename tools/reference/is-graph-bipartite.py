from collections import deque


def isBipartite(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    colour = [0] * n
    for start in range(n):
        if colour[start]:
            continue
        colour[start] = 1
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbour in adj[node]:
                if colour[neighbour] == colour[node]:
                    return False
                if not colour[neighbour]:
                    colour[neighbour] = -colour[node]
                    queue.append(neighbour)
    return True
