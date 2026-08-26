def findMaxConsecutiveOnes(nums):
    best = run = 0
    for value in nums:
        run = run + 1 if value == 1 else 0
        best = max(best, run)
    return best
