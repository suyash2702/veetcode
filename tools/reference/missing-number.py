def missingNumber(nums):
    out = len(nums)
    for i, value in enumerate(nums):
        out ^= i ^ value
    return out
