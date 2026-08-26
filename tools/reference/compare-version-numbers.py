def compareVersion(version1, version2):
    first = version1.split(".")
    second = version2.split(".")
    for i in range(max(len(first), len(second))):
        a = int(first[i]) if i < len(first) else 0
        b = int(second[i]) if i < len(second) else 0
        if a != b:
            return 1 if a > b else -1
    return 0
