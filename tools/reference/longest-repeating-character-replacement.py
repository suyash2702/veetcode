def characterReplacement(s, k):
    counts = {}
    best = most_common = left = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        most_common = max(most_common, counts[ch])
        while right - left + 1 - most_common > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
