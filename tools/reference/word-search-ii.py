def findWords(board, words):
    trie = {}
    for word in words:
        node = trie
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = word

    rows, cols = len(board), len(board[0])
    found = []

    def walk(r, c, node):
        ch = board[r][c]
        nxt = node.get(ch)
        if nxt is None:
            return
        word = nxt.pop("$", None)
        if word is not None:
            found.append(word)
        board[r][c] = "#"
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                walk(nr, nc, nxt)
        board[r][c] = ch
        if not nxt:
            node.pop(ch, None)

    for r in range(rows):
        for c in range(cols):
            walk(r, c, trie)
    return found
