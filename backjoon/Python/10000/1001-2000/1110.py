# https://www.acmicpc.net/problem/1110 : 더하기 사이클 (python3)
# 입력시간 최적화
from sys import stdin

input = stdin.readline


def generate(n):
    a, b = n // 10, n % 10
    return b * 10 + (a + b) % 10


n = int(input())
constant = n
cnt = 1
while True:
    n = generate(n)
    if n == constant:
        break
    cnt += 1

print(cnt)
