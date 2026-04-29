# https://www.acmicpc.net/problem/10810 : 공 넣기(python3)
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

basket = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i, j + 1):
        basket[a - 1] = k

for i in range(n):
    print(basket[i], end=" ")
