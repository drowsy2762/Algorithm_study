# https://www.acmicpc.net/problem/13913
# 2026-04-08
import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    
    dist = [-1] * 100001
    parent = [-1] * 10000

    def bfs():
        q = deque([n]) 
        dist[n] = 0
        while q:
            x = q.popleft()
            if x == k:
                break
            for nx in (x + 1, x - 1, x * 2):
                if 0 <= nx <= 100000 and dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    parent[nx] = x
                    q.append(nx)
    bfs() 

    path = []
    curr = k
    
    while curr != n:
        path.append(curr)
        curr = parent[curr]
        
    path.append(n)
    path.reverse() 

    print(dist[k])
    print(*(path))

if __name__ == "__main__":
    solution()