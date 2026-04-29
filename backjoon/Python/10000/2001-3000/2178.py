# https://www.acmicpc.net/problem/2178 : 미로 탐색(python3)
from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx >= n or nx < 0) or (ny >= m or ny < 0):
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))


bfs()
print(maze[n - 1][m - 1])
