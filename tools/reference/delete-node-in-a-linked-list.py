def deleteNode(head, position):
    node = head
    for _ in range(position):
        node = node.next
    node.val = node.next.val
    node.next = node.next.next
    return head
