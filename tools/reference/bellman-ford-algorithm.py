def bellmanFord(n, edges, source):
    INF = float("inf")
    best = [INF] * n
    best[source] = 0
    for _ in range(n - 1):
        changed = False
        for a, b, w in edges:
            if best[a] != INF and best[a] + w < best[b]:
                best[b] = best[a] + w
                changed = True
        if not changed:
            break
    for a, b, w in edges:
        if best[a] != INF and best[a] + w < best[b]:
            return [-1]
    return [-1 if d == INF else d for d in best]
