def kthElement(a, b, k):
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    lo = max(0, k - m)
    hi = min(k, n)
    while lo <= hi:
        cut_a = (lo + hi) // 2
        cut_b = k - cut_a
        left_a = a[cut_a - 1] if cut_a > 0 else float("-inf")
        left_b = b[cut_b - 1] if cut_b > 0 else float("-inf")
        right_a = a[cut_a] if cut_a < n else float("inf")
        right_b = b[cut_b] if cut_b < m else float("inf")
        if left_a <= right_b and left_b <= right_a:
            return max(left_a, left_b)
        if left_a > right_b:
            hi = cut_a - 1
        else:
            lo = cut_a + 1
    return -1
