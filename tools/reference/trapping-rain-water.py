def trap(height):
    lo, hi = 0, len(height) - 1
    left_max = right_max = total = 0
    while lo < hi:
        if height[lo] <= height[hi]:
            left_max = max(left_max, height[lo])
            total += left_max - height[lo]
            lo += 1
        else:
            right_max = max(right_max, height[hi])
            total += right_max - height[hi]
            hi -= 1
    return total
