def longestPalindrome(s):
    best = ''
    for center in range(len(s)):
        for lo, hi in ((center, center), (center, center + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            candidate = s[lo + 1:hi]
            if len(candidate) > len(best):
                best = candidate
    return best
