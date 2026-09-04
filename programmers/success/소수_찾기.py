# 2026-09-04

import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def solution(numbers):
    n = len(numbers)
    visited = [False] * n
    candidate_numbers = set()

    def dfs(current_str):
        if current_str:
            candidate_numbers.add(int(current_str))
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(current_str + numbers[i])
                visited[i] = False

    dfs("")

    prime_count = 0
    for num in candidate_numbers:
        if is_prime(num):
            prime_count += 1

    return prime_count
