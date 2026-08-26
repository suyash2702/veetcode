from collections import defaultdict


def groupAnagrams(strs):
    buckets = defaultdict(list)
    for word in strs:
        buckets[tuple(sorted(word))].append(word)
    return list(buckets.values())
