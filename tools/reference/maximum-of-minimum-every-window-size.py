def maxOfMin(nums):
    n = len(nums)
    left = [-1] * n
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    best = [None] * (n + 1)
    for i in range(n):
        width = right[i] - left[i] - 1
        if best[width] is None or nums[i] > best[width]:
            best[width] = nums[i]
    for width in range(n - 1, 0, -1):
        if best[width] is None or (best[width + 1] is not None and best[width + 1] > best[width]):
            best[width] = best[width + 1]
    return best[1:]
