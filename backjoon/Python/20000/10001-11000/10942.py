# https://www.acmicpc.net/problem/10942
# 2026-03-13
import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

# 길이 1짜리 펠린드롬
for i in range(n):
    dp[i][i] = 1

# 길이 2짜리 펠린드롬
for i in range(n - 1):
    if board[i] == board[i + 1]:
        dp[i][i + 1] = 1

# 길이 3이상 펠린드롬
for length in range(3, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1
        if board[start] == board[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1

# 출력문
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])