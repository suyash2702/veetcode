from collections import Counter


def topKFrequent(nums, k):
    return [value for value, _ in Counter(nums).most_common(k)]
