# https://www.acmicpc.net/problem/21610
# 2026-02-21
import sys
input = sys.stdin.readline

dr, dc = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
visited = [[-1] * N for _ in range(N)] 

for m in range(M):
    d, s = map(int, input().split())
    
    moved_clouds = []
    for r, c in clouds:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        arr[nr][nc] += 1
        visited[nr][nc] = m  
        moved_clouds.append((nr, nc))
        
    for r, c in moved_clouds:
        water_cnt = 0
        for i in (2, 4, 6, 8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > 0:
                water_cnt += 1
        arr[r][c] += water_cnt
        
    clouds = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and visited[i][j] != m:
                arr[i][j] -= 2
                clouds.append((i, j))

print(sum(sum(row) for row in arr))