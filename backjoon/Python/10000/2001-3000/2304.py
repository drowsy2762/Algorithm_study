# https://www.acmicpc.net/problem/2304 : 창고 다각형(python3)
# 2023-11-10
from sys import stdin

input = stdin.readline

n = int(input())

storage = list()
area = 0
for _ in range(n):
    l, m = map(int, input().split())
    storage.append((l, m))
storage.sort()
x, ymax = storage[0][0], storage[0][1]
for i, k in storage:
    area += (i - x) * ymax
    if ymax < k:
        ymax = k
    x = i
area += ymax
storage.reverse()
smax = storage[0][1]
t = storage[0][1]
for i, k in storage:
    # print(area, smax, ymax, k)
    if smax == ymax:
        break
    area -= (x - i) * (ymax - smax)
    if k > smax:
        t = smax
        smax = k
    x = i
    # print(k, smax)

print(area)
