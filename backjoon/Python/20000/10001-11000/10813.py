# https://www.acmicpc.net/problem/10813 : 공 바꾸기 (python3)
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]

for i in basket:
    print(i, end=" ")
