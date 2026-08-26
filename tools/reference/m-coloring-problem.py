def graphColoring(n, edges, m):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    colour = [0] * n

    def walk(node):
        if node == n:
            return True
        for c in range(1, m + 1):
            if all(colour[neighbour] != c for neighbour in adj[node]):
                colour[node] = c
                if walk(node + 1):
                    return True
                colour[node] = 0
        return False

    return walk(0)
