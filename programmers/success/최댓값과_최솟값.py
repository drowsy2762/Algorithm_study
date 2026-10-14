# 2026-10-14


def solution(s):
    numbers = list(map(int, s.split()))
    min_val = min(numbers)
    max_val = max(numbers)
    return f"{min_val} {max_val}"
