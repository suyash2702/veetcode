def findMissingRepeating(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    square = n * (n + 1) * (2 * n + 1) // 6
    diff = sum(nums) - total                 # repeating - missing
    square_diff = sum(v * v for v in nums) - square
    total_sum = square_diff // diff          # repeating + missing
    repeating = (diff + total_sum) // 2
    return [repeating, repeating - diff]
