def numDecodings(s):
    if not s or s[0] == "0":
        return 0
    previous, current = 1, 1
    for i in range(1, len(s)):
        total = 0
        if s[i] != "0":
            total += current
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            total += previous
        previous, current = current, total
        if current == 0:
            return 0
    return current
