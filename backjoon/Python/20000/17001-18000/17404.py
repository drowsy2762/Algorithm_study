# https://www.acmicpc.net/problem/17404
# 2026-03-29
import sys
input = sys.stdin.readline
INF = 10**9 

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

ans = INF

for i in range(3):
    dp = [INF, INF, INF]
    dp[i] = rgb[0][i]
    
    for j in range(1, n):
        next_dp = [
            min(dp[1], dp[2]) + rgb[j][0],
            min(dp[0], dp[2]) + rgb[j][1],
            min(dp[0], dp[1]) + rgb[j][2]
        ]
        dp = next_dp 
        
    for c in range(3):
        if i != c:
            ans = min(ans, dp[c])

print(ans)