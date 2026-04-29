# https://www.acmicpc.net/problem/13458 : 시험 감독 (python3)
# 01-24-25
from sys import stdin

input = stdin.readline

n = int(input())
tester = list(map(int, input().split()))
b, c = map(int, input().split())
t = 0
for i in range(n):
    tester[i] -= b
    t += 1
    if tester[i] > 0:
        if tester[i] % c == 0:
            t += tester[i] // c
        else:
            t += tester[i] // c + 1

print(t)
