def longestWordWithAllPrefixes(words):
    root = {}
    for word in words:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    best = [""]

    def walk(node, prefix):
        if len(prefix) > len(best[0]) or (len(prefix) == len(best[0]) and prefix < best[0]):
            best[0] = prefix
        for ch in sorted(k for k in node if k != "$"):
            child = node[ch]
            if child.get("$"):
                walk(child, prefix + ch)

    walk(root, "")
    return best[0]
