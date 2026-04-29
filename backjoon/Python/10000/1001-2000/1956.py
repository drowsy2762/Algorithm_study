# https://www.acmicpc.net/problem/1956
# 2026-03-24
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        if graph[i][k] == INF:
            continue
        ik_dist = graph[i][k]
        for j in range(1, v + 1):
            new_dist = ik_dist + graph[k][j]
            if new_dist < graph[i][j]:
                graph[i][j] = new_dist

answer = INF
for i in range(1, v + 1):
    if graph[i][i] < answer:
        answer = graph[i][i]

print(answer if answer != INF else -1)