# https://www.acmicpc.net/problem/9370
# 2026-03-15
import sys
import heapq
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, d = map(int, input().split())
            weight = d * 2
            if (a == g and b == h) or (a == h and b == g):
                weight -= 1
            graph[a].append((b, weight))
            graph[b].append((a, weight))
            
        candidates = []
        for _ in range(t):
            candidates.append(int(input()))

        dist = [float('inf')] * (n + 1)
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if dist[curr_node] < curr_dist:
                continue
            for next_node, next_weight in graph[curr_node]:
                cost = curr_dist + next_weight
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(pq, (cost, next_node))
        
        ans = []
        for candi in candidates:
            if dist[candi] != float('inf') and dist[candi] % 2 == 1:
                ans.append(candi)
            
        ans.sort()
        print(*ans)

if __name__ == '__main__':
    solve()