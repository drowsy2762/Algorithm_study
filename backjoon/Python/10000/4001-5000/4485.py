# https://www.acmicpc.net/problem/4485 : 녹색 옷 입은 애가 젤다지? (python3)
# 2024-02-09
from sys import stdin
import heapq

input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f"Problem {count}: {distance[x][y]}")
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if distance[nx][ny] > cost + graph[nx][ny]:
                distance[nx][ny] = cost + graph[nx][ny]
                heapq.heappush(q, (distance[nx][ny], nx, ny))


count = 1

while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[float("inf")] * n for _ in range(n)]

    dijkstra()
    count += 1
