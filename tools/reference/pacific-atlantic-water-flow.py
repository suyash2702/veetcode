def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])

    def flood(starts):
        seen = set(starts)
        stack = list(starts)
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]):
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return seen

    pacific = flood([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
    atlantic = flood([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)])
    return [[r, c] for r, c in sorted(pacific & atlantic)]
