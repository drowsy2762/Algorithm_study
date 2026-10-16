# 2026-10-16
def solution(n):
    return sum(1 for divisor in range(1, n + 1, 2) if n % divisor == 0)
