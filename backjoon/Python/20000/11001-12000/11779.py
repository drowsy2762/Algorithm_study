# https://www.acmicpc.net/problem/11779 : 최소비용 구하기 2
# 2026-04-09
import sys
import heapq

def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    start, end = map(int, input().split())
    distances = [float('Inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]
    parent = [0] * (n + 1)

    while pq:
        dist, now = heapq.heappop(pq)
        if distances[now] < dist:
            continue
        for next_node, weight in graph[now]:
            new_dist = dist + weight
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                parent[next_node] = now
                heapq.heappush(pq, (new_dist, next_node))

    print(distances[end])

    path = []
    curr = end
    while curr != 0:
        path.append(curr)
        curr = parent[curr]
    
    print(len(path))
    print(*(path[::-1]))

if __name__ == "__main__":
    solution()