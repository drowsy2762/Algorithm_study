# 2026-10-26
def solution(n):
    MOD = 1000000007
    a, b = 1, 2
    if n <= 2:
        return n
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD
    return b
