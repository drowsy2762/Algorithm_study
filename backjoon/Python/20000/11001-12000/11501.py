# https://www.acmicpc.net/problem/11501 : 주식 (python3)
# 2023-11-08
from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    sequence = 0
    max, money = 0, 0

    for i in range(N - 1, -1, -1):
        if days[i] > max:
            max = days[i]
        else:
            money += max - days[i]
    print(money)
