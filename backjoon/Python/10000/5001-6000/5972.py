# https://www.acmicpc.net/problem/5972 : 택배 배송 (python3)
# 2024 - 01 - 12
from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def bfs(q):
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, [cost, i[0]])


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

INF = int(1e9)
distance = [INF] * (n + 1)
distance[1] = 0
q = []
heappush(q, [0, 1])
bfs(q)
print(distance[n])
