# https://www.acmicpc.net/problem/10026 : 적록색약(python3)
from sys import stdin
from copy import deepcopy

input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())

graph1 = [list(input().rstrip()) for _ in range(n)]
graph2 = deepcopy(graph1)
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
cnt1 = 0
cnt2 = 0

# 색약용 탐색 그래프 생성
for i in range(n):
    for j in range(n):
        if graph2[i][j] == "G":
            graph2[i][j] = "R"


# 범위 우선탐색
def dfs(x, y, graph, visited):
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        x = queue[0][0]
        y = queue[0][1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
        queue.pop(0)
    return 1


for i in range(n):
    for j in range(n):
        if visited1[i][j] == False:
            cnt1 += dfs(i, j, graph1, visited1)
        if visited2[i][j] == False:
            cnt2 += dfs(i, j, graph2, visited2)

print(cnt1, cnt2)
