# https://www.acmicpc.net/problem/22233 : 가희와 키워드 (python3)
# 2023-11-03
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
memo = dict()
for _ in range(N):
    memo[input().rstrip()] = 1

result = N
for i in range(M):
    tmp = list(input().rstrip().split(","))
    for j in tmp:
        if j in memo.keys():
            if memo[j] == 1:
                memo[j] -= 1
                result -= 1
    print(result)
