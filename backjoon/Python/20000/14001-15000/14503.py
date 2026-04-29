# https://www.acmicpc.net/problem/14503
# 2026-01-08
from sys import stdin
input = stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_range(x, y):
    return 0 <= x < n and 0 <= y < m

def cleaner(r, c, d):
    cnt = 0
    x, y = r, c
    while True:
        for i in range(4):
            if graph[x][y] == 0:
                graph[x][y] = -1
                cnt += 1
            
            for _ in range(4):
                d = (d - 1) % 4
                nx, ny = x + dx[d], y + dy[d]
                if check_range(nx, ny) and graph[nx][ny] == 0:
                    x, y = nx, ny
                    break
            
            else:
                x, y = x + dx[d] *(-1), y + dy[d] * (-1)
                if check_range(x, y) and graph[x][y] == 1 or not check_range(x, y):
                    print(cnt)
                    return

cleaner(r, c, direction)
