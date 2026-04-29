# https://www.acmicpc.net/problem/1800
# 2026-03-05
import sys
import heapq

input = sys.stdin.readline
N, P, K = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(P):
    u, v, p = map(int, input().split())
    adj[u].append((v, p))
    adj[v].append((u, p))

def check(limit):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        count, curr = heapq.heappop(pq)
        
        if dist[curr] < count:
            continue
            
        for nxt, p in adj[curr]:
            weight = 1 if p > limit else 0
            if dist[nxt] > count + weight:
                dist[nxt] = count + weight
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist[N] <= K

# 이분 탐색 시작
low, high = 0, 1000000
ans = -1

while low <= high:
    mid = (low + high) // 2
    if check(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)