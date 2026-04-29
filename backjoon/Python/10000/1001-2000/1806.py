# https://www.acmicpc.net/problem/1806 : 부분합 (python3)
# 2024-02-10
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
lists = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = sys.maxsize

while True:
    if sum >= s:
        min_length = min(min_length, right - left)
        sum -= lists[left]
        left += 1
    elif right == n:
        break
    else:
        sum += lists[right]
        right += 1


if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
