def kmpSearch(text, pattern):
    m = len(pattern)
    failure = [0] * m
    length = 0
    for i in range(1, m):
        while length and pattern[i] != pattern[length]:
            length = failure[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
        failure[i] = length

    out = []
    length = 0
    for i, ch in enumerate(text):
        while length and ch != pattern[length]:
            length = failure[length - 1]
        if ch == pattern[length]:
            length += 1
        if length == m:
            out.append(i - m + 1)
            length = failure[length - 1]
    return out
