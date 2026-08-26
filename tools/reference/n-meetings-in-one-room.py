def maxMeetings(start, end):
    meetings = sorted(zip(end, start))
    count, last_end = 0, float("-inf")
    for finish, begin in meetings:
        if begin > last_end:
            count += 1
            last_end = finish
    return count
