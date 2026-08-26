def subsetsWithDup(nums):
    values = sorted(nums)
    out = []
    current = []

    def walk(start):
        out.append(list(current))
        for i in range(start, len(values)):
            if i > start and values[i] == values[i - 1]:
                continue
            current.append(values[i])
            walk(i + 1)
            current.pop()

    walk(0)
    return out
