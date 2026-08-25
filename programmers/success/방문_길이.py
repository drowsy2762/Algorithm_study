# 2026-08-25


def solution(dirs):
    move = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    visited = set()
    x, y = 0, 0
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        if not (-6 < nx < 6 and -6 < ny < 6):
            continue
        visited.add(((x, y), (nx, ny)))
        visited.add(((nx, ny), (x, y)))
        x, y = nx, ny
    return len(visited) // 2
