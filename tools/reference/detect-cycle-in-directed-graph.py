def hasCycle(n, edges):
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        adj[a].append(b)
        indegree[b] += 1
    queue = [i for i in range(n) if indegree[i] == 0]
    seen = 0
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        seen += 1
        for neighbour in adj[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return seen != n
