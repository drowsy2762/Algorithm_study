# https://www.acmicpc.net/problem/19941 : 햄버거 분배 (python3)
# 2023-10-12
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n):
    if s[i] == "P":
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if s[j] == "H":
                s[j] = 0
                cnt += 1
                break

print(cnt)
