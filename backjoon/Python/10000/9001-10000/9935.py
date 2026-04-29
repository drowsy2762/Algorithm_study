# https://www.acmicpc.net/problem/9935 : 문자열 폭발(python3)
# 2024-02-16
from sys import stdin

input = stdin.readline

s = list(input().rstrip())
bomb = list(input().rstrip())
m = len(bomb)
stack = []
for i in s:
    stack.append(i)
    if stack[len(stack) - m : len(stack)] == bomb:
        for _ in range(m):
            stack.pop()

if stack:
    print(*stack, sep="")
else:
    print("FRULA")
