def moveZeroes(nums):
    w = 0
    for i, x in enumerate(nums):
        if x != 0:
            nums[w], nums[i] = nums[i], nums[w]
            w += 1
