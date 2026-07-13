# 2026-07-13


def solution(elements):
    unique_sums = set()
    n = len(elements)
    extended = elements * 2

    for i in range(n):
        current_sum = 0
        for length in range(n):
            current_sum += extended[i + length]
            unique_sums.add(current_sum)

    return len(unique_sums)
