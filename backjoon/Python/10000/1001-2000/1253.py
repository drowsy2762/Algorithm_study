# https://www.acmicpc.net/problem/1253 : 좋다 (python3)
# 2024-02-09
from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(n):
    left = 0
    right = n - 1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        if arr[left] + arr[right] == arr[i]:
            cnt += 1
            break
        if arr[left] + arr[right] < arr[i]:
            left += 1
        else:
            right -= 1
print(cnt)
