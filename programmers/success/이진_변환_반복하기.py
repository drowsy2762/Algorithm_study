# 2026-08-11


def solution(s):
    transform_count = 0
    zero_count = 0
    while s != "1":
        num_zeros = s.count("0")
        zero_count += num_zeros
        c = len(s) - num_zeros
        s = bin(c)[2:]
        transform_count += 1

    return [transform_count, zero_count]
