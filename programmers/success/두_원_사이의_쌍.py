# 2026-06-13

import math


def solution(r1, r2):
    total_points = 0

    for x in range(1, r2 + 1):
        v2 = r2**2 - x**2
        max_y = math.isqrt(v2)

        if x < r1:
            v1 = r1**2 - x**2
            root = math.isqrt(v1)
            if root * root == v1:
                min_y = root
            else:
                min_y = root + 1
        else:
            min_y = 0
        total_points += max_y - min_y + 1

    return total_points * 4
