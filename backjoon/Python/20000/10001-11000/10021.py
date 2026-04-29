# https://www.acmicpc.net/problem/10021
# 2026-03-01
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
fields = [tuple(map(int, input().split())) for _ in range(n)]

dist = [float('inf')] * n
visited = [False] * n  
dist[0] = 0
answer = 0
connected_count = 0

for _ in range(n):
    min_cost = float('inf')
    min_idx = -1
    for i in range(n):
        if not visited[i] and dist[i] < min_cost:
            min_cost = dist[i]
            min_idx = i

    if min_cost == float('inf'):
        break

    visited[min_idx] = True
    answer += min_cost
    connected_count += 1
    
    x1, y1 = fields[min_idx]
    for i in range(n):
        if not visited[i]:
            x2, y2 = fields[i]
            cost = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if cost >= c and cost < dist[i]:
                dist[i] = cost

if connected_count == n:
    print(answer)
else:
    print(-1)