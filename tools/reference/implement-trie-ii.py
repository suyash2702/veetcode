class Trie:
    def __init__(self):
        self.children = {}
        self.ends = 0
        self.passing = 0

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())
            node.passing += 1
        node.ends += 1

    def _walk(self, prefix):
        node = self
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def countWordsEqualTo(self, word):
        node = self._walk(word)
        return node.ends if node else 0

    def countWordsStartingWith(self, prefix):
        node = self._walk(prefix)
        return node.passing if node else 0

    def erase(self, word):
        node = self
        for ch in word:
            child = node.children.get(ch)
            if child is None:
                return
            child.passing -= 1
            node = child
        node.ends -= 1
