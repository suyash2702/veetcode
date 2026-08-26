import heapq


def dijkstra(n, edges, source):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((b, w))
        adj[b].append((a, w))

    best = [float("inf")] * n
    best[source] = 0
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > best[node]:
            continue
        for neighbour, weight in adj[node]:
            candidate = distance + weight
            if candidate < best[neighbour]:
                best[neighbour] = candidate
                heapq.heappush(heap, (candidate, neighbour))
    return [-1 if d == float("inf") else d for d in best]
