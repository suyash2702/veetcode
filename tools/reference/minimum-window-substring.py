from collections import Counter


def minWindow(s, t):
    need = Counter(t)
    missing = len(t)
    best = (float('inf'), 0, 0)
    left = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return '' if best[0] == float('inf') else s[best[1]:best[2]]
