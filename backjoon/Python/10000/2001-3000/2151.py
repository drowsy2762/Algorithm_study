# https://www.acmicpc.net/problem/2151
# 2026-03-22
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def solve():
    N = int(input())
    room = [list(input().rstrip()) for _ in range(N)]
    points = []
    for i in range(N):
        for j in range(N):
            if room[i][j] == '#':
                points.append((i, j))
    
    (sx, sy), (ex, ey) = points[0], points[1]
    v = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    q = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for d in range(4):
        nx, ny = sx + dx[d], sy + dy[d]
        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] != '*':
            v[nx][ny][d] = 0
            heapq.heappush(q, (0, nx, ny, d))
    while q:
        mirror, x, y, d = heapq.heappop(q)
        if mirror > v[x][y][d]:
            continue
        if x == ex and y == ey:
            print(mirror)
            return
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] != '*':
            if v[nx][ny][d] > mirror:
                v[nx][ny][d] = mirror
                heapq.heappush(q, (mirror, nx, ny, d))
        if room[x][y] == '!':
            for nd in [(d - 1) % 4, (d + 1) % 4]:
                nx, ny = x + dx[nd], y + dy[nd]
                if 0 <= nx < N and 0 <= ny < N and room[nx][ny] != '*':
                    if v[nx][ny][nd] > mirror + 1:
                        v[nx][ny][nd] = mirror + 1
                        heapq.heappush(q, (mirror + 1, nx, ny, nd))

solve()