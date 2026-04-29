# https://www.acmicpc.net/problem/15685
# 2026-01-18
from sys import stdin
input = stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    curve = [d]
    # g세대 만큼 반복하며 방향 리스트 불리기
    # 규칙: 현재 리스트를 역순으로 돌면서 (방향 + 1) % 4 한 것을 뒤에 붙임
    for _ in range(g):
        temp = []
        for i in range(len(curve) - 1, -1, -1):
            temp.append((curve[i] + 1) % 4)
        curve.extend(temp) # 리스트 합치기
        
    graph[y][x] = 1 # 시작점 체크
    nx, ny = x, y
    for direction in curve:
        nx += dx[direction]
        ny += dy[direction]
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            graph[ny][nx] = 1

# 정사각형 개수 세기
ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            ans += 1

print(ans)