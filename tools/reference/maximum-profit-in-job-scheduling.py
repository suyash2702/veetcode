import bisect


def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    ends = [0]
    best = [0]
    for end, start, value in jobs:
        index = bisect.bisect_right(ends, start) - 1
        candidate = best[index] + value
        if candidate > best[-1]:
            ends.append(end)
            best.append(candidate)
    return best[-1]
