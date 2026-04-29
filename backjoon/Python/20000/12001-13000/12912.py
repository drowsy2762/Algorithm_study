# https://www.acmicpc.net/problem/12919 : A와 B 2 (python3)
# 2023-01-04

from sys import stdin

input = stdin.readline


def dfs(s):
    global result

    if len(s) == len(S):
        if s == S:
            result = 1
            return
        return

    if s[-1] == "A":
        s.pop()
        dfs(s)
        s.append("A")

    if s[0] == "B":
        s.reverse()
        s.pop()
        dfs(s)
        s.append("B")
        s.reverse()


S = list(input().rstrip())
T = list(input().strip())
result = 0
dfs(T)
print(result)
