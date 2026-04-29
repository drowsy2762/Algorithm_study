# https://www.acmicpc.net/problem/20055 : 컨베이어 벨트 위의 로봇 (python3)
# 2024-01-05
from sys import stdin
from collections import deque

input = stdin.readline


n, k = map(int, input().split())
A = deque(list(map(int, input().split())))
robots = deque([0] * n)
step = 0

while True:
    step += 1
    A.rotate(1)
    robots[-1] = 0
    robots.rotate(1)
    robots[-1] = 0
    for i in range(n - 2, -1, -1):
        if A[i + 1] >= 1 and robots[i + 1] == 0 and robots[i] == 1:
            robots[i + 1] = 1
            robots[i] = 0
            A[i + 1] -= 1
    robots[-1] = 0
    if A[0] != 0 and robots[0] != 1:
        robots[0] = 1
        A[0] -= 1
    if A.count(0) >= k:
        break

print(step)
