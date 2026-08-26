def findCelebrity(knows):
    n = len(knows)
    candidate = 0
    for other in range(1, n):
        if knows[candidate][other]:
            candidate = other
    for other in range(n):
        if other == candidate:
            continue
        if knows[candidate][other] or not knows[other][candidate]:
            return -1
    return candidate
