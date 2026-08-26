def subsetSum(nums, target):
    reachable = [False] * (target + 1)
    reachable[0] = True
    for value in nums:
        if value == 0:
            continue
        for total in range(target, value - 1, -1):
            if reachable[total - value]:
                reachable[total] = True
    return reachable[target]
