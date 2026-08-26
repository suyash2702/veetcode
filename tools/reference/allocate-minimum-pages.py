def findPages(books, students):
    if students > len(books):
        return -1

    def readers_needed(limit):
        count, total = 1, 0
        for pages in books:
            if total + pages > limit:
                count += 1
                total = pages
            else:
                total += pages
        return count

    lo, hi = max(books), sum(books)
    while lo < hi:
        mid = (lo + hi) // 2
        if readers_needed(mid) <= students:
            hi = mid
        else:
            lo = mid + 1
    return lo
