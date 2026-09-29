# 2026-09-29
def solution(n, a, b):
    round_count = 0
    while a != b:
        round_count += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return round_count
