def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        if any(word[i] != ch for word in strs):
            return shortest[:i]
    return shortest
