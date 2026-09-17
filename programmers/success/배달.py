# 2026-09-17

import heapq


def solution(N, road, K):
    ans = 0
    graph = [[] for _ in range(N + 1)]
    for s, e, t in road:
        graph[s].append((e, t))
        graph[e].append((s, t))
    INF = float("inf")
    distances = [INF] * (N + 1)
    distances[1] = 0
    pq = [(0, 1)]
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_dist > distances[cur_node]:
            continue
        for next_node, time in graph[cur_node]:
            cost = cur_dist + time
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return sum(1 for dist in distances[1:] if dist <= K)
