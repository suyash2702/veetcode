def countAndSay(n):
    term = "1"
    for _ in range(n - 1):
        out = []
        i = 0
        while i < len(term):
            j = i
            while j < len(term) and term[j] == term[i]:
                j += 1
            out.append(str(j - i))
            out.append(term[i])
            i = j
        term = "".join(out)
    return term
