def dfsOfGraph(adj):
    seen = [False] * len(adj)
    out = []
    stack = [0]
    while stack:
        node = stack.pop()
        if seen[node]:
            continue
        seen[node] = True
        out.append(node)
        for neighbour in reversed(adj[node]):
            if not seen[neighbour]:
                stack.append(neighbour)
    return out
