def maxLen(nums):
    first_seen = {0: -1}
    total = 0
    best = 0
    for i, value in enumerate(nums):
        total += value
        if total in first_seen:
            best = max(best, i - first_seen[total])
        else:
            first_seen[total] = i
    return best
