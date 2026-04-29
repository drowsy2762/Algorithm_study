# https://www.acmicpc.net/problem/11049
# 2026-03-10
import sys
input = sys.stdin.readline

n = int(input())
matrix = []
dp = [[0] * n for _ in range(n)]
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for length in range(n - 1):
    for i in range(n - length - 1):
        j = i + length + 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
print(dp[0][-1])
