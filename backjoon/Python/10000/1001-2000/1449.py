# https://www.acmicpc.net/problem/1449
# 2026-02-05
from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
water_leak = list(map(int, input().split()))
water_leak.sort()
ans = 0
tape_end = 0

for location in water_leak:
    if location <= tape_end:
        continue
    else:
        ans += 1
        tape_end = location + l - 1

print(ans)