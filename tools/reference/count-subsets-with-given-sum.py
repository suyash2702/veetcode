def countSubsets(nums, target):
    counts = [0] * (target + 1)
    counts[0] = 1
    for value in nums:
        if value == 0:
            for total in range(target + 1):
                counts[total] *= 2
            continue
        for total in range(target, value - 1, -1):
            counts[total] += counts[total - value]
    return counts[target]
