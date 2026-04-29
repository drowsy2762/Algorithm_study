# https://www.acmicpc.net/problem/20058
# 2026-02-18
from sys import stdin
from collections import deque
input = stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, q = map(int, input().split())
N = 2 ** n 
graph = [list(map(int, input().split())) for _ in range(N)]
line = list(map(int, input().split()))

def rotate(l):
    sub_size = 2 ** l
    for r in range(0, N, sub_size):
        for c in range(0, N, sub_size):
            sub_grid = [row[c : c + sub_size] for row in graph[r : r + sub_size]]
            rotated = list(zip(*sub_grid[::-1]))
            for i in range(sub_size):
                for j in range(sub_size):
                    graph[r + i][c + j] = rotated[i][j]

def melt():
    melting_list = []

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 0: continue

            cnt = 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:
                    if graph[nr][nc] > 0:
                        cnt += 1
            if cnt < 3:
                melting_list.append((r, c))

    for r, c in melting_list:
        if graph[r][c] > 0:
            graph[r][c] -= 1

def get_total_ice():
    return sum(sum(row) for row in graph)

def bfs(start_r, start_c, visited):
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    cnt = 1
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and graph[nr][nc] > 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cnt += 1
    return cnt

def get_max_mass():
    visited = [[False] * N for _ in range(N)]
    max_count = 0
    
    for r in range(N):
        for c in range(N):
            if graph[r][c] > 0 and not visited[r][c]:
                max_count = max(max_count, bfs(r, c, visited))
                
    return max_count

for l in line:
    rotate(l)
    melt()

print(get_total_ice())
print(get_max_mass())