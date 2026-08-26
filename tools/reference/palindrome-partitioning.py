def partition(s):
    out = []
    current = []

    def walk(start):
        if start == len(s):
            out.append(list(current))
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                current.append(piece)
                walk(end)
                current.pop()

    walk(0)
    return out
