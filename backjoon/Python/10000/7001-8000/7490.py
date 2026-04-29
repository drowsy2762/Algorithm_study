# https://www.acmicpc.net/problem/7490 : 0 만들기 (python3)
# 2024-02-08
from sys import stdin

input = stdin.readline

t = int(input())


def dfs(target, n, save):
    if target == n:
        if eval(save.replace(" ", "")) == 0:
            return print(save)
        return

    next = target + 1
    empty = save + " " + str(next)
    dfs(target + 1, n, empty)

    plus = save + "+" + str(next)
    dfs(target + 1, n, plus)

    minus = save + "-" + str(next)
    dfs(target + 1, n, minus)


for _ in range(t):
    n = int(input())
    dfs(1, n, "1")
    print()
