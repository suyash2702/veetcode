def findPlatform(arrival, departure):
    arrivals = sorted(arrival)
    departures = sorted(departure)
    platforms = best = 0
    i = j = 0
    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            platforms += 1
            best = max(best, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    return best
