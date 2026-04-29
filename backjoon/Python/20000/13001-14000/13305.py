# https://www.acmicpc.net/problem/13305 : 주유소(python3)
# 2023-10-05
from sys import stdin

n = int(input())
length = list(map(int, input().split()))
station = list(map(int, input().split()))

min_price = station[0]
total = 0
for i in range(n - 1):
    min_price = min(min_price, station[i])
    total += min_price * length[i]

print(total)
