# https://www.acmicpc.net/problem/11657
# 2026-03-18
import sys
input = sys.stdin.readline

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        updated = False
        for now, nxt, cost in edges:
            if dist[now] != float('inf') and dist[nxt] > dist[now] + cost:
                dist[nxt] = dist[now] + cost
                updated = True
                if i == n - 1:
                    return True
        if not updated:
            break

    return False

n, m = map(int, input().split())
edges = []
dist = [float('inf')] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    ans = [-1 if d == float('inf') else d for d in dist[2:]]
    print(*ans, sep='\n')