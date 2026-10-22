# 2026-10-22
def solution(n):
    target_ones = bin(n).count("1")
    next_num = n + 1
    while True:
        if bin(next_num).count("1") == target_ones:
            return next_num
        next_num += 1
