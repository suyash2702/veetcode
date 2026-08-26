def copyRandomList(head):
    if head is None:
        return None

    node = head
    while node:
        copy = ListNode(node.val)
        copy.next = node.next
        node.next = copy
        node = copy.next

    node = head
    while node:
        node.next.random = node.random.next if node.random else None
        node = node.next.next

    node = head
    new_head = head.next
    while node:
        copy = node.next
        node.next = copy.next
        copy.next = copy.next.next if copy.next else None
        node = node.next
    return new_head
