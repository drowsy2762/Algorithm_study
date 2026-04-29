# https://www.acmicpc.net/problem/2512 : 예산 (python3)
# 2023-10-09

from sys import stdin

input = stdin.readline


n = int(input())
request = list(map(int, input().split()))
budget = int(input())
average = int(budget / n)

start, end = 0, max(request)
result = 0

while start <= end:
    mid = int((start + end) / 2)
    total = 0

    for i in request:
        if i > mid:
            total += mid
        else:
            total += i

    if total > budget:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
