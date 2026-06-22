# 2026-06-22

from collections import deque


def solution(maps):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    start_x, start_y, end_x, end_y, lever_x, lever_y = 0, 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start_x, start_y = i, j
            elif maps[i][j] == "L":
                lever_x, lever_y = i, j
            elif maps[i][j] == "E":
                end_x, end_y = i, j

    def bfs(from_x, from_y, to_x, to_y):
        visited = [[False] * m for _ in range(n)]
        visited[from_x][from_y] = True
        q = deque([(from_x, from_y, 0)])
        while q:
            x, y, dist = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and visited[nx][ny] == False
                    and maps[nx][ny] != "X"
                ):
                    if nx == to_x and ny == to_y:
                        return dist + 1
                    q.append([nx, ny, dist + 1])
                    visited[nx][ny] = True
        return -1

    to_lever = bfs(start_x, start_y, lever_x, lever_y)
    to_end = bfs(lever_x, lever_y, end_x, end_y)

    if to_lever == -1 or to_end == -1:
        return -1
    return to_lever + to_end
