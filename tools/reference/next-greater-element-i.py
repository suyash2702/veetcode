def nextGreaterElement(nums1, nums2):
    greater = {}
    stack = []
    for value in nums2:
        while stack and stack[-1] < value:
            greater[stack.pop()] = value
        stack.append(value)
    return [greater.get(value, -1) for value in nums1]
