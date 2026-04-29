# https://www.acmicpc.net/problem/2583 : python3(영역 구하기)
from sys import stdin

input = stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    cnt = 1
    graph[x][y] = 1
    queue = [(x, y)]
    while queue:
        for i in range(4):
            nx = queue[0][0] + dx[i]
            ny = queue[0][1] + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                cnt += 1
        queue.pop(0)
    return cnt


for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    if lx > rx:
        rx, lx = lx, rx
    if ly > ry:
        ry, ly = ly, ry
    for j in range(lx, rx):
        for k in range(ly, ry):
            graph[j][k] = 1


count = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            count.append(bfs(i, j))

print(len(count))
count.sort()
print(*count)
