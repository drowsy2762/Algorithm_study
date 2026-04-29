# https://www.acmicpc.net/problem/14469
# 2026-03-06
import sys
input = sys.stdin.readline

n = int(input())
cows = [list(map(int, input().split())) for _ in range(n)]
cows.sort()

time = 0
for k, t in cows:
    time = max(time, k) + t
print(time)