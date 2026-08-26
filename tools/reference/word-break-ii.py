def wordBreak(s, wordDict):
    words = set(wordDict)
    memo = {}

    def build(start):
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]
        out = []
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece in words:
                for rest in build(end):
                    out.append(piece if not rest else piece + " " + rest)
        memo[start] = out
        return out

    return build(0)
