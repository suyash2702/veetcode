def rob(nums):
    def line(values):
        take = skip = 0
        for value in values:
            take, skip = skip + value, max(skip, take)
        return max(take, skip)

    if len(nums) == 1:
        return nums[0]
    return max(line(nums[1:]), line(nums[:-1]))
