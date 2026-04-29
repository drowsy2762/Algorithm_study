# https://www.acmicpc.net/problem/1522 : 문자열 교환 (python3)
# 2023-11-24
from sys import stdin
from collections import deque

input = stdin.readline

s = input().rstrip()
a = s.count("a")

s += s
min_v = float("inf")
for i in range(len(s) - (a - 1)):
    min_v = min(min_v, s[i : i + a].count("b"))
print(min_v)
