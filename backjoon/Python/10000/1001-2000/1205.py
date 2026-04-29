# https://www.acmicpc.net/problem/1205 : 등수 구하기 (python3)
# 2023-09-28

from sys import stdin

input = stdin.readline

n, new, p = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))
    if n == p and score[-1] >= new:
        print(-1)
    else:
        res = n + 1
        for i in range(n):
            if score[i] <= new:
                res = i + 1
                break
        print(res)
