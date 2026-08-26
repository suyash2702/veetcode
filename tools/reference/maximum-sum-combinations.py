import heapq


def maxCombinations(a, b, k):
    first = sorted(a, reverse=True)
    second = sorted(b, reverse=True)
    heap = [(-(first[0] + second[0]), 0, 0)]
    seen = {(0, 0)}
    out = []
    while heap and len(out) < k:
        total, i, j = heapq.heappop(heap)
        out.append(-total)
        for ni, nj in ((i + 1, j), (i, j + 1)):
            if ni < len(first) and nj < len(second) and (ni, nj) not in seen:
                seen.add((ni, nj))
                heapq.heappush(heap, (-(first[ni] + second[nj]), ni, nj))
    return out
