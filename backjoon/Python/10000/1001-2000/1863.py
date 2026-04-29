# https://www.acmicpc.net/problem/1863 : 스카이라인 쉬운거 (python3)
# 2024-01-18
from sys import stdin

input = stdin.readline

n = int(input())
answer = 0
stack = []
for _ in range(n):
    x, y = map(int, input().split())
    while len(stack) > 0 and stack[-1] > y:
        answer += 1
        stack.pop()
    if len(stack) > 0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack) > 0:
    if stack[-1] > 0:
        answer += 1
    stack.pop()

print(answer)
