def longestConsecutive(nums):
    pool = set(nums)
    best = 0
    for x in pool:
        if x - 1 in pool:
            continue
        length = 1
        while x + length in pool:
            length += 1
        best = max(best, length)
    return best
