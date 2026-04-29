# https://www.acmicpc.net/problem/6087 : 레이저 통신 (python3)
# 2025-10-23(can't solve) / 2026-03-08(solve)
from sys import stdin
from collections import deque

input = stdin.readline

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

w, h = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(h)]
dist = [[float('inf')] * w for _ in range(h)]

c_pos = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == "C":
            c_pos.append((i, j))
(sr, sc), (er, ec) = c_pos[0], c_pos[1]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = -1
    while q:
        r, c = q.popleft()
        if r == er and c == ec:
            return dist[er][ec]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            while 0 <= nr < h and 0 <= nc < w and graph[nr][nc] != "*":
                if dist[nr][nc] >= dist[r][c] + 1:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
                    nr += dr[i]
                    nc += dc[i]
                elif dist[nr][nc] < dist[r][c] + 1:
                    break 



print(bfs(sr, sc))