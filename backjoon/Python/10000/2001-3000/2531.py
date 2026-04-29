# https://www.acmicpc.net/problem/2531 : 회전 초밥 (python3)
# 2023-11-23
from sys import stdin

input = stdin.readline

N, d, k, c = map(int, input().rstrip().split())
belts = [int(input()) for _ in range(N)]
max = 0
for i in range(N):
    if i + k > N:
        num = len(set(belts[i:N] + belts[: (i + k) % N] + [c]))
    else:
        num = len(set(belts[i : i + k] + [c]))
    if max < num:
        max = num
print(max)
