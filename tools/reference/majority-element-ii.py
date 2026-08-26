def majorityElement(nums):
    first = second = None
    count1 = count2 = 0
    for value in nums:
        if first is not None and value == first:
            count1 += 1
        elif second is not None and value == second:
            count2 += 1
        elif count1 == 0:
            first, count1 = value, 1
        elif count2 == 0:
            second, count2 = value, 1
        else:
            count1 -= 1
            count2 -= 1
    limit = len(nums) // 3
    return [v for v in (first, second) if v is not None and nums.count(v) > limit]
