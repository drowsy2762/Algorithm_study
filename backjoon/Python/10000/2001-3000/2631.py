# https://www.acmicpc.net/problem/2631 : 줄세우기(python3)
from sys import stdin

input = stdin.readline


n = int(input())
line = []
for i in range(n):
    line.append(int(input()))

dp = [1] * (n + 1)

for i in range(n):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            print(dp)

print(n - max(dp))
