# https://www.acmicpc.net/problem/2098
# 2026-03-26
import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
DP = [[-1] * N for _ in range(1 << N)]
INF = 10**9

def tsp(visited, curr):
    if visited == (1 << N) - 1:
        return W[curr][0] if W[curr][0] != 0 else INF
    if DP[visited][curr] != -1:
        return DP[visited][curr]
    
    min_cost = INF
    for nxt in range(N):
        if not (visited & (1 << nxt)) and W[curr][nxt] != 0:
            cost = tsp(visited | (1 << nxt), nxt) + W[curr][nxt]
            min_cost = min(min_cost, cost)
    
    DP[visited][curr] = min_cost
    return min_cost

print(tsp(1 << 0, 0))