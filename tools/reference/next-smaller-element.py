def nextSmallerElement(nums):
    out = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        if stack:
            out[i] = stack[-1]
        stack.append(nums[i])
    return out
