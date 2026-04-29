# https://www.acmicpc.net/problem/15683
# 2026-01-13
from sys import stdin
from collections import deque
from copy import deepcopy
input = stdin.readline
minimum = 1e9

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv_direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[1, 2, 3, 0]]
}

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append([graph[i][j], i, j])

def fill_blank(x, y, d, graph):
    nx, ny = x, y
    while True:
        nx += dx[d]
        ny += dy[d]
        if not (0 <= nx < n and 0 <= ny < m):
            break
        if graph[nx][ny] == 6:
            break
        if graph[nx][ny] == 0:
            graph[nx][ny] = 7


def dfs(graph, depth):
    if depth == len(cctv):
        global minimum
        cnt = 0
        for i in range(n):
            for j in range(m):
               if graph[i][j] == 0:
                    cnt += 1
        minimum = min(cnt, minimum)
        return
    cctv_kind, x, y = cctv[depth]
    for direction in cctv_direction[cctv_kind]:
        temp_graph = deepcopy(graph)
        for d in direction:
            fill_blank(x, y, d, temp_graph)
            
        dfs(temp_graph, depth + 1)


dfs(graph, 0)
print(minimum)