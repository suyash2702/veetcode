def combinationSum(candidates, target):
    out = []
    current = []

    def walk(start, remaining):
        if remaining == 0:
            out.append(list(current))
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                walk(i, remaining - candidates[i])
                current.pop()

    walk(0, target)
    return out
