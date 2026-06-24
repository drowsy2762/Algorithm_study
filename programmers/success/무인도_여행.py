# 2026-06-24

from collections import deque


def solution(maps):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                island_food = int(maps[i][j])
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and maps[nx][ny] != "X":
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                island_food += int(maps[nx][ny])

                answer.append(island_food)

    if not answer:
        return [-1]

    answer.sort()
    return answer
