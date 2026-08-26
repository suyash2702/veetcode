def permute(nums):
    out = []

    def walk(start):
        if start == len(nums):
            out.append(list(nums))
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            walk(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    walk(0)
    return out
