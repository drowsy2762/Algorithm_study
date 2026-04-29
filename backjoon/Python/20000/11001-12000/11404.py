# https://www.acmicpc.net/problem/11404
# 2026-03-20
import sys
input = sys.stdin.readline

INF = 10**9 

def solve():
    N = int(input())
    M = int(input())

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        graph[i][i] = 0
        
    for _ in range(M):
        a, b, c = map(int, input().split())
        if c < graph[a][b]:
            graph[a][b] = c

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            if graph[a][k] != INF:
                for b in range(1, N + 1):
                    cost = graph[a][k] + graph[k][b]
                    if cost < graph[a][b]:
                        graph[a][b] = cost
                    
    for i in range(1, N + 1):
        print(*(0 if graph[i][j] == INF else graph[i][j] for j in range(1, N + 1)))

if __name__ == '__main__':
    solve()