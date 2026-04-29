# https://www.acmicpc.net/problem/11066
# 2026-03-09
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    chapter = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + chapter[i]
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1): 
            j = i + length - 1 
            dp[i][j] = float('inf')
            sub_sum = prefix_sum[j+1] - prefix_sum[i]
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sub_sum)

    print(dp[0][n-1])

t = int(input())
for _ in range(t):
    solve()