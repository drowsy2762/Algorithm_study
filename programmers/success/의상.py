# 2026-09-16

from collections import Counter
import math


def solution(clothes):
    counts = Counter(category for _, category in clothes).values()
    return math.prod(c + 1 for c in counts) - 1
