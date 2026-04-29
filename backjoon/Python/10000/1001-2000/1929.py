# https://www.acmicpc.net/problem/1929 : 소수 구하기 (python3)
# 입력시간 최적화
from sys import stdin

input = stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


m, n = map(int, input().split())
for i in range(m, n + 1):
    if is_prime(i):
        print(i)
