from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = {}
        self.counts = {}
        self.buckets = defaultdict(OrderedDict)
        self.smallest = 0

    def _touch(self, key):
        count = self.counts[key]
        del self.buckets[count][key]
        if not self.buckets[count]:
            del self.buckets[count]
            if self.smallest == count:
                self.smallest += 1
        self.counts[key] = count + 1
        self.buckets[count + 1][key] = None

    def get(self, key):
        if key not in self.values:
            return -1
        self._touch(key)
        return self.values[key]

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.values:
            self.values[key] = value
            self._touch(key)
            return
        if len(self.values) >= self.capacity:
            evicted, _ = self.buckets[self.smallest].popitem(last=False)
            if not self.buckets[self.smallest]:
                del self.buckets[self.smallest]
            del self.values[evicted]
            del self.counts[evicted]
        self.values[key] = value
        self.counts[key] = 1
        self.buckets[1][key] = None
        self.smallest = 1
