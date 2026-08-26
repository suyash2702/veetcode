def findContentChildren(g, s):
    children = sorted(g)
    cookies = sorted(s)
    i = j = 0
    while i < len(children) and j < len(cookies):
        if cookies[j] >= children[i]:
            i += 1
        j += 1
    return i
