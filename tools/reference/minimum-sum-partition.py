def minDifference(nums):
    total = sum(nums)
    half = total // 2
    reachable = [False] * (half + 1)
    reachable[0] = True
    for value in nums:
        if value == 0 or value > half:
            continue
        for amount in range(half, value - 1, -1):
            if reachable[amount - value]:
                reachable[amount] = True
    for amount in range(half, -1, -1):
        if reachable[amount]:
            return total - 2 * amount
    return total
