def countSCC(n, edges):
    adj = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        reverse[b].append(a)

    seen = [False] * n
    order = []
    for start in range(n):
        if seen[start]:
            continue
        stack = [(start, 0)]
        seen[start] = True
        while stack:
            node, index = stack.pop()
            if index < len(adj[node]):
                stack.append((node, index + 1))
                nxt = adj[node][index]
                if not seen[nxt]:
                    seen[nxt] = True
                    stack.append((nxt, 0))
            else:
                order.append(node)

    seen = [False] * n
    components = 0
    for node in reversed(order):
        if seen[node]:
            continue
        components += 1
        stack = [node]
        seen[node] = True
        while stack:
            current = stack.pop()
            for previous in reverse[current]:
                if not seen[previous]:
                    seen[previous] = True
                    stack.append(previous)
    return components
