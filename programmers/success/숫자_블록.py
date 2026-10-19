# 2026-10-19
import math


def get_block_number(position, max_block_limit=10_000_000):
    if position == 1:
        return 0

    max_valid_divisor = 1
    sqrt_pos = int(math.isqrt(position))
    for i in range(2, sqrt_pos + 1):
        if position % i == 0:
            paired_divisor = position // i
            if paired_divisor <= max_block_limit:
                return paired_divisor
            max_valid_divisor = i

    return max_valid_divisor


def solution(begin, end):
    return [get_block_number(pos) for pos in range(begin, end + 1)]
