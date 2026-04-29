# https://www.acmicpc.net/problem/7576 : 토마토(python3)
from sys import stdin
from collections import deque

input = stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(q):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
tq = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tq.append((i, j))

bfs(tq)

if check():
    for i in range(n):
        for j in range(m):
            result = max(result, graph[i][j])
    print(result - 1)
else:
    print(-1)
