def flatten(head):
    def merge(a, b):
        dummy = ListNode(0)
        tail = dummy
        while a and b:
            if a.val <= b.val:
                tail.bottom, a = a, a.bottom
            else:
                tail.bottom, b = b, b.bottom
            tail = tail.bottom
        tail.bottom = a if a else b
        return dummy.bottom

    if head is None or head.next is None:
        return head
    rest = flatten(head.next)
    head.next = None
    return merge(head, rest)
