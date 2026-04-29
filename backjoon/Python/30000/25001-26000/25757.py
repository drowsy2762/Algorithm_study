# https://www.acmicpc.net/problem/25757 : 임스와 함께하는 미니게임 (python3)
# 2023-09-26

from sys import stdin

input = stdin.readline

n, s = list(input().split())
n = int(n)

player = [input() for _ in range(n)]
player = list(set(player))

if s == "Y":
    print(len(player))
elif s == "F":
    print(len(player) // 2)
elif s == "O":
    print(len(player) // 3)
