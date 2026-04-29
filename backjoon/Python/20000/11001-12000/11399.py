# https://www.acmicpc.net/problem/11399
# 2026-02-04
from sys import stdin
input = stdin.readline

n = int(input())
bank = list(map(int, input().split()))
bank.sort()
ans = 0
cnt = 0
for time in bank:
    cnt += time
    ans += cnt
    
print(ans)