def combinationSum2(candidates, target):
    values = sorted(candidates)
    out = []
    current = []

    def walk(start, remaining):
        if remaining == 0:
            out.append(list(current))
            return
        for i in range(start, len(values)):
            if i > start and values[i] == values[i - 1]:
                continue
            if values[i] > remaining:
                break
            current.append(values[i])
            walk(i + 1, remaining - values[i])
            current.pop()

    walk(0, target)
    return out
