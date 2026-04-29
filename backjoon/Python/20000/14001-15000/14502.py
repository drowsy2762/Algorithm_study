# https://www.acmicpc.net/problem/14502
# 2026-01-07
from sys import stdin
from collections import deque
from copy import deepcopy
import itertools
input = stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = 0

n, m = map(int,input().rstrip().split())

graph = [list(map(int, input().split())) for _ in range(n)]
blank = []
virus = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])
        elif graph[i][j] == 2:
            virus.append([i, j])

def bfs(c_graph):
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    q = deque()
    for x, y in virus:
        q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            # 빈 칸(0)만 감염 확산
            if c_graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                c_graph[nx][ny] = 2
                q.append((nx, ny))  # 좌표를 하나의 튜플로 추가
    for i in range(n):
        for j in range(m):
            if c_graph[i][j] == 0:
                cnt += 1
    return cnt

for (i1, i2), (j1, j2), (k1, k2) in itertools.combinations(blank, 3):
    c_graph = deepcopy(graph)
    c_graph[i1][i2] = 1
    c_graph[j1][j2] = 1
    c_graph[k1][k2] = 1
    ans = max(bfs(c_graph), ans)
print(ans)