# 2026-07-29

from itertools import combinations


def solution(line):
    points = set()

    for (a1, b1, c1), (a2, b2, c2) in combinations(line, 2):
        denom = a1 * b2 - b1 * a2
        if denom == 0:
            continue
        num_x = b1 * c2 - c1 * b2
        num_y = c1 * a2 - a1 * c2

        if num_x % denom == 0 and num_y % denom == 0:
            x = num_x // denom
            y = num_y // denom
            points.add((x, y))

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [["."] * width for _ in range(height)]

    for x, y in points:
        r = max_y - y
        c = x - min_x
        grid[r][c] = "*"

    return ["".join(row) for row in grid]
