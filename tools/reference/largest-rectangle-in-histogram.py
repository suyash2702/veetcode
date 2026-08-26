def largestRectangleArea(heights):
    stack = []
    best = 0
    for i, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= height:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            best = max(best, heights[top] * width)
        stack.append(i)
    return best
