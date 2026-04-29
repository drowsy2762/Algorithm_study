# https://www.acmicpc.net/problem/2749 : 피본나치 수 3 (python3)
from sys import stdin

input = stdin.readline


def solution():
    mod = 1000000  # 10^6
    fibo = [0, 1]
    p = mod // 10 * 15  # 피사노 주기

    n = int(input())

    for i in range(2, p):
        fibo.append(fibo[i - 1] + fibo[i - 2])
        fibo[i] %= mod

    print(fibo[n % p])


solution()
