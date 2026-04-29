# https://www.acmicpc.net/problem/4179 : 불! (python3)
# 2024-02-15
from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())
graph = []

pos_j = []
pos_f = []
for i in range(R):
    tmp = list(input())
    for j in range(C):
        if tmp[j] == "J":
            pos_j.append((i, j))
        elif tmp[j] == "F":
            pos_f.append((i, j))
    graph.append(tmp)


q = deque()
q.append((pos_j[0][0], pos_j[0][1], "J"))
graph[pos_j[0][0]][pos_j[0][1]] = 0

if len(pos_f) != 0:
    for r, c in pos_f:
        q.append((r, c, "F"))
        graph[r][c] = "#"


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, case = q.popleft()
        if case == "J" and (x == 0 or y == 0 or x == R - 1 or y == C - 1):
            if graph[x][y] == "#":
                continue
            return graph[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] != "#" and case == "F":
                    graph[nx][ny] = "#"
                    q.append((nx, ny, "F"))
                elif graph[nx][ny] == "." and case == "J" and graph[x][y] != "#":
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny, "J"))
    return "IMPOSSIBLE"


print(bfs())
