# https://www.acmicpc.net/problem/2751
# 2026-01-14
from sys import stdin
input = stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)