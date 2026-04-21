# https://www.acmicpc.net/problem/10282
# 2026-04-21
import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def solution():
    n, d, c = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s)) 
        
    dist = [INF] * (n + 1)
    dist[c] = 0 
    pq = []
    heapq.heappush(pq, (0, c))
    
    while pq:
        current_time, current_node = heapq.heappop(pq)
        if dist[current_node] < current_time:
            continue
            
        for next_node, weight in adj[current_node]:
            next_time = current_time + weight
            if next_time < dist[next_node]:
                dist[next_node] = next_time
                heapq.heappush(pq, (next_time, next_node))
                
    infected_count = 0
    max_time = 0
    
    for i in range(1, n + 1):
        if dist[i] != INF:
            infected_count += 1
            max_time = max(max_time, dist[i])
            
    print(infected_count, max_time)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        solution()