# https://www.acmicpc.net/problem/1138 : 한 줄로 서기 (python3)
# 2023-11-14
from sys import stdin

input = stdin.readline

n = int(input())

order = [0 for _ in range(n)]
arr = list(map(int, input().split()))

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and order[j] == 0:
            order[j] = i + 1
            break
        elif order[j] == 0:
            cnt += 1
print(" ".join(map(str, order)))
