# https://www.acmicpc.net/problem/2467 : 용액 (python3)
# 2024-01-12
from sys import stdin

input = stdin.readline

n = int(input())

liquids = list(map(int, input().split()))
liquids.sort()

left = 0
right = n - 1
answer = [liquids[left], liquids[right]]
min_value = abs(liquids[left] + liquids[right])
while left < right:
    value = liquids[left] + liquids[right]
    if abs(value) < min_value:
        min_value = abs(value)
        answer = [liquids[left], liquids[right]]
    if value > 0:
        right -= 1
    elif value < 0:
        left += 1
    else:
        break
print(*answer)
