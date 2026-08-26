def connect(root):
    level = root
    while level:
        node = level
        nxt = None
        tail = None
        while node:
            for child in (node.left, node.right):
                if child is None:
                    continue
                if nxt is None:
                    nxt = child
                if tail is not None:
                    tail.next = child
                tail = child
            node = getattr(node, "next", None)
        if tail is not None:
            tail.next = None
        level = nxt
    return root
