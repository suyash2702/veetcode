def aggressiveCows(stalls, cows):
    positions = sorted(stalls)

    def fits(distance):
        placed, last = 1, positions[0]
        for position in positions[1:]:
            if position - last >= distance:
                placed += 1
                last = position
                if placed >= cows:
                    return True
        return placed >= cows

    lo, hi = 0, positions[-1] - positions[0]
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if fits(mid):
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best
