# 2026-10-20


def solution(n):
    MOD = 1234567
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, (a + b) % MOD

    return a
