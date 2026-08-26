def subsetSums(nums):
    sums = [0]
    for value in nums:
        sums += [total + value for total in sums]
    return sums
