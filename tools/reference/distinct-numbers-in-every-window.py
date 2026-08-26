def countDistinct(nums, k):
    counts = {}
    out = []
    for i, value in enumerate(nums):
        counts[value] = counts.get(value, 0) + 1
        if i >= k:
            leaving = nums[i - k]
            counts[leaving] -= 1
            if counts[leaving] == 0:
                del counts[leaving]
        if i >= k - 1:
            out.append(len(counts))
    return out
