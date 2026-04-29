# https://www.acmicpc.net/problem/17144
# 2026-01-23
from sys import stdin
input = stdin.readline

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

air_cleaner = []
for i in range(r):
    if graph[i][0] == -1:
        air_cleaner.append(i)

up = air_cleaner[0]
down = air_cleaner[1]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for _ in range(t):
    # 미세먼지 퍼짐
    temp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                spread = graph[x][y] // 5
                if spread == 0: continue
                
                count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        temp[nx][ny] += spread
                        count += 1
                
                graph[x][y] -= spread * count # 남은 양 갱신

    # 공기청정기 작동
    for x in range(r):
        for y in range(c):
            graph[x][y] += temp[x][y]

    # 위쪽 공기청정기
    for i in range(up - 1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(c - 1):
        graph[0][i] = graph[0][i+1]
    for i in range(up):
        graph[i][c-1] = graph[i+1][c-1]
    for i in range(c - 1, 1, -1):
        graph[up][i] = graph[up][i-1]
    graph[up][1] = 0 

    # 아랫쪽 공기청정기
    for i in range(down + 1, r - 1):
        graph[i][0] = graph[i+1][0]
    for i in range(c - 1):
        graph[r-1][i] = graph[r-1][i+1] 
    for i in range(r - 1, down, -1):
        graph[i][c-1] = graph[i-1][c-1]
    for i in range(c - 1, 1, -1):
        graph[down][i] = graph[down][i-1]
    graph[down][1] = 0 # 정화된 공기

ans = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            ans += graph[i][j]

print(ans)