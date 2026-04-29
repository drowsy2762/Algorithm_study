# https://www.acmicpc.net/problem/17142
# 2026-02-07
from sys import stdin
from itertools import combinations
from collections import deque
input = stdin.readline

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
virus = []
M = 1e9
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i, j])

q = deque()

def bfs(virus_list, visited):
    q = deque()
    for x, y in virus_list:
        q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny]) 
    local_max = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and visited[i][j] == -1:
                return 1e9
            
            if graph[i][j] == 0:
                local_max = max(local_max, visited[i][j])
                
    return local_max

for v in combinations(virus, m):
    visited = [[-1] * n for _ in range(n)]
    for x, y in v:
        visited[x][y] = 0
        visited[x][y] = 0
    M = min(M, bfs(v, visited))
    
if M == 1e9:
    print(-1)
else:
    print(M)