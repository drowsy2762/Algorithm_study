# https://www.acmicpc.net/problem/10217
# 2026-03-21
import sys
from collections import deque
input = sys.stdin.readline

import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra():
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))
    for i in range(1, N + 1):
        graph[i].sort(key=lambda x: x[2])
    dist_cost = [[INF] * (M + 1) for _ in range(N + 1)]
    dist_cost[1][0] = 0
    pq = [(0, 1, 0)]
    
    while pq:
        d, curr, c = heapq.heappop(pq)
        if dist_cost[curr][c] < d:
            continue
        for nxt, ncost, ndist in graph[curr]:
            total_cost = c + ncost
            total_dist = d + ndist
            if total_cost <= M and dist_cost[nxt][total_cost] > total_dist:
                for j in range(total_cost, M + 1):
                    if dist_cost[nxt][j] > total_dist:
                        dist_cost[nxt][j] = total_dist
                    else:
                        break
                heapq.heappush(pq, (total_dist, nxt, total_cost))

    result = dist_cost[N][M]
    print(result if result != INF else "Poor KCM")

T = int(input())
for _ in range(T):
    dijkstra()