def nthRoot(n, m):
    def power(base):
        total = 1
        for _ in range(n):
            total *= base
            if total > m:
                return total
        return total

    lo, hi = 1, m
    while lo <= hi:
        mid = (lo + hi) // 2
        value = power(mid)
        if value == m:
            return mid
        if value < m:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
