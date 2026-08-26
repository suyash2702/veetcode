def getPermutation(n, k):
    digits = [str(d) for d in range(1, n + 1)]
    factorial = 1
    for d in range(1, n):
        factorial *= d
    k -= 1
    out = []
    for remaining in range(n - 1, -1, -1):
        index, k = divmod(k, factorial)
        out.append(digits.pop(index))
        if remaining:
            factorial //= remaining
    return "".join(out)
