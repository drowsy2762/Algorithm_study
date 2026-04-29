# https://www.acmicpc.net/problem/11401 : 이항 계수 3 (python3)

from sys import stdin

input = stdin.readline
MOD = 1000000007
cashes = []


def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % MOD
    return n


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % MOD
    else:
        return tmp * tmp % MOD


def solution():
    n, k = map(int, input().split())
    top = factorial(n)
    bot = factorial(n - k) * factorial(k) % MOD

    print(top * square(bot, MOD - 2) % MOD)


solution()
