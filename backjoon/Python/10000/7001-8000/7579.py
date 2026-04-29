# https://www.acmicpc.net/problem/7579
# 2026-03-12
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memoryList = list(map(int, input().split()))
costList = list(map(int, input().split()))
max_cost = sum(costList)
dp = [0] * (max_cost + 1)

for i in range(n):
    mem = memoryList[i]
    cost = costList[i]
    for j in range(max_cost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + mem)

for i in range(max_cost + 1):
    if dp[i] >= m:
        print(i)
        break