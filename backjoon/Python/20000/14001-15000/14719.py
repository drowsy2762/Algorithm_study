# https://www.acmicpc.net/problem/14719 : 빗물 (python3)
# 2024 - 01 - 11
from sys import stdin

input = stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
answer = 0
for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1 :])
    if blocks[i] < left and blocks[i] < right:
        answer += min(left, right) - blocks[i] 
print(answer)
