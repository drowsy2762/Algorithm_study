# 2026-10-15
import math


def solution(n, k):
    numbers = list(range(1, n + 1))
    answer = []
    k -= 1

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        idx, k = divmod(k, fact)
        answer.append(numbers.pop(idx))

    return answer
