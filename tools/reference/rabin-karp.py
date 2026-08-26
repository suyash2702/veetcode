BASE = 256
MOD = 1000000007


def searchPattern(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    high = pow(BASE, m - 1, MOD)
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * BASE + ord(pattern[i])) % MOD
        window_hash = (window_hash * BASE + ord(text[i])) % MOD

    out = []
    for start in range(n - m + 1):
        if window_hash == pattern_hash and text[start:start + m] == pattern:
            out.append(start)
        if start + m < n:
            window_hash = ((window_hash - ord(text[start]) * high) * BASE + ord(text[start + m])) % MOD
    return out
