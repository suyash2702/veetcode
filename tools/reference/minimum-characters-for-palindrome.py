def minCharsForPalindrome(s):
    combined = s + "#" + s[::-1]
    failure = [0] * len(combined)
    for i in range(1, len(combined)):
        length = failure[i - 1]
        while length and combined[i] != combined[length]:
            length = failure[length - 1]
        if combined[i] == combined[length]:
            length += 1
        failure[i] = length
    return len(s) - failure[-1]
