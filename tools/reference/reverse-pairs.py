def reversePairs(nums):
    def sort_count(values):
        if len(values) < 2:
            return values, 0
        mid = len(values) // 2
        left, a = sort_count(values[:mid])
        right, b = sort_count(values[mid:])
        count = a + b
        j = 0
        for value in left:
            while j < len(right) and value > 2 * right[j]:
                j += 1
            count += j
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    return sort_count(list(nums))[1]
