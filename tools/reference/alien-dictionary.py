import heapq


def alienOrder(words):
    letters = {ch for word in words for ch in word}
    adj = {ch: set() for ch in letters}
    indegree = {ch: 0 for ch in letters}

    for first, second in zip(words, words[1:]):
        for a, b in zip(first, second):
            if a != b:
                if b not in adj[a]:
                    adj[a].add(b)
                    indegree[b] += 1
                break
        else:
            if len(first) > len(second):
                return ""

    ready = [ch for ch in letters if indegree[ch] == 0]
    heapq.heapify(ready)
    out = []
    while ready:
        ch = heapq.heappop(ready)
        out.append(ch)
        for nxt in sorted(adj[ch]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, nxt)
    return "".join(out) if len(out) == len(letters) else ""
