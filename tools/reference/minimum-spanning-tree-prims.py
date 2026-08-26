import heapq


def spanningTree(n, edges):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((w, b))
        adj[b].append((w, a))

    seen = [False] * n
    heap = [(0, 0)]
    total = 0
    taken = 0
    while heap and taken < n:
        weight, node = heapq.heappop(heap)
        if seen[node]:
            continue
        seen[node] = True
        total += weight
        taken += 1
        for edge_weight, neighbour in adj[node]:
            if not seen[neighbour]:
                heapq.heappush(heap, (edge_weight, neighbour))
    return total
