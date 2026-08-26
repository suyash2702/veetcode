def myAtoi(s):
    i, n = 0, len(s)
    while i < n and s[i] == " ":
        i += 1
    sign = 1
    if i < n and s[i] in "+-":
        sign = -1 if s[i] == "-" else 1
        i += 1
    value = 0
    while i < n and s[i].isdigit():
        value = value * 10 + int(s[i])
        i += 1
        if sign * value <= -2 ** 31:
            return -2 ** 31
        if sign * value >= 2 ** 31 - 1:
            return 2 ** 31 - 1
    return sign * value
