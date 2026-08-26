def maxSumIS(nums):
    best = list(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                best[i] = max(best[i], best[j] + nums[i])
    return max(best)
