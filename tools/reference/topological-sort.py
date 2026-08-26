import heapq


def topologicalSort(n, edges):
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        adj[a].append(b)
        indegree[b] += 1
    ready = [i for i in range(n) if indegree[i] == 0]
    heapq.heapify(ready)
    out = []
    while ready:
        node = heapq.heappop(ready)
        out.append(node)
        for neighbour in adj[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                heapq.heappush(ready, neighbour)
    return out if len(out) == n else []
