# 2026-10-28
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0, 1)])
    maps[0][0] = 0
    while queue:
        x, y, dist = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny, dist + 1))

    return -1
