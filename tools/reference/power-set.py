def powerSet(s):
    out = []
    for mask in range(1, 1 << len(s)):
        out.append("".join(s[i] for i in range(len(s)) if mask & (1 << i)))
    return out
