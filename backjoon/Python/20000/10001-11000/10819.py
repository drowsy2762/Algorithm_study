# https://www.acmicpc.net/problem/10819
# 2026-01-27
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0

for p in permutations(a):
    total = 0
    for i in range(n - 1):
        total += abs(p[i] - p[i+1])
    ans = max(ans, total)

print(ans)