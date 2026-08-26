class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word):
        node = self
        for ch in word:
            node = node.children.setdefault(ch, WordDictionary())
        node.is_word = True

    def search(self, word):
        def walk(node, index):
            if index == len(word):
                return node.is_word
            ch = word[index]
            if ch == ".":
                return any(walk(child, index + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and walk(child, index + 1)

        return walk(self, 0)
