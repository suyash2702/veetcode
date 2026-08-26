def cloneGraph(node):
    if node is None:
        return None
    copies = {node: Node(node.val)}
    stack = [node]
    while stack:
        current = stack.pop()
        for neighbour in current.neighbors:
            if neighbour not in copies:
                copies[neighbour] = Node(neighbour.val)
                stack.append(neighbour)
            copies[current].neighbors.append(copies[neighbour])
    return copies[node]
