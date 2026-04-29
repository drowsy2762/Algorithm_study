# https://www.acmicpc.net/problem/2493 : 탑 (python3)
# 2024-01-08
from sys import stdin

input = stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, towers[i]])

print(" ".join(map(str, answer)))
