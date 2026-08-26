def longestCommonSubsequence(text1, text2):
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    previous = [0] * (len(text2) + 1)
    for a in text1:
        current = [0] * (len(text2) + 1)
        for j, b in enumerate(text2, 1):
            current[j] = previous[j - 1] + 1 if a == b else max(previous[j], current[j - 1])
        previous = current
    return previous[-1]
