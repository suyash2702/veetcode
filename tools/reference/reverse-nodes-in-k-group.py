def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        node = group_prev
        for _ in range(k):
            node = node.next
            if node is None:
                return dummy.next
        group_next = node.next

        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            cur.next, prev, cur = prev, cur, cur.next
        tail = group_prev.next
        group_prev.next = prev
        group_prev = tail
