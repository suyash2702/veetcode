def findMaximumXOR(nums):
    best = 0
    mask = 0
    for bit in range(31, -1, -1):
        mask |= 1 << bit
        prefixes = {value & mask for value in nums}
        candidate = best | (1 << bit)
        if any(prefix ^ candidate in prefixes for prefix in prefixes):
            best = candidate
    return best
