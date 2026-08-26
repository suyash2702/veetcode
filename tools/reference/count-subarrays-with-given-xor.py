def countSubarrays(nums, k):
    seen = {0: 1}
    prefix = 0
    count = 0
    for value in nums:
        prefix ^= value
        count += seen.get(prefix ^ k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
