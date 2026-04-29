# https://www.acmicpc.net/problem/16234 : 인구 이동 (python3)
# 2024-01-05
from sys import stdin
from collections import deque

input = stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0 for _ in range(n)] for _ in range(n)]


def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))

    return union


day = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    flag = 1
                    people = sum(graph[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        graph[x][y] = people

    if flag == 0:
        print(day)
        break
    day += 1
