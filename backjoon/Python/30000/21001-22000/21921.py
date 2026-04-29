# https://www.acmicpc.net/problem/21921 : 블로그 (python3)
# 2023-10-10

from sys import stdin

input = stdin.readline


def slideWindow():
    start = 0
    end = x
    tmax = 0
    for i in range(end):
        tmax += visiters[i]
    max, cnt = tmax, 1
    while end < n:
        tmax += visiters[end]
        tmax -= visiters[start]
        if tmax > max:
            max = tmax
            cnt = 1
        elif tmax == max:
            cnt += 1
        end += 1
        start += 1
    if max == 0:
        print("SAD")
    else:
        print(max)
        print(cnt)


n, x = map(int, input().split())
visiters = list(map(int, input().split()))

slideWindow()
