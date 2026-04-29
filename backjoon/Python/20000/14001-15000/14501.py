# https://www.acmicpc.net/problem/14501 : 퇴사(python3)
# 2025-02-26
# retry 2026-01-06
from sys import stdin

input = stdin.readline

n = int(input())
schedule = []
for i in range(n):
    j, k = map(int,input().rstrip().split())
    schedule.append([j, k])
    
dp = [0 for _ in range(n + 1)]

for i in range(n-1 , -1, -1):
    if i + schedule[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])
    
print(dp[0])