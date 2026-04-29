# https://www.acmicpc.net/problem/19637 : IF문 좀 대신 써줘
# 2023-11-02
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def binarySearch(end):
    start = 0
    while start <= end:
        mid = (start + end) // 2
        if mid > n:
            mid = n
        if title[mid - 1][1] < cp <= title[mid][1]:
            return mid
        elif title[mid][1] < cp:
            start = mid
        else:
            end = mid


title = [[0, -1]]
n, m = map(int, input().split())
for i in range(n):
    title.append(input().split())
    title[i + 1][1] = int(title[i + 1][1])
for _ in range(m):
    cp = int(input())
    tmp = binarySearch(n + 1)
    print(title[tmp][0])
