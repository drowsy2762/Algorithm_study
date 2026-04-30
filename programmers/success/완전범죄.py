# 2026-04-30
from typing import List


def solution(info: List[List[int]], n: int, m: int) -> int:
    INF = float("inf")
    dp = [INF] * m
    dp[0] = 0

    for traceA, traceB in info:
        next_dp = [INF] * m
        for b in range(m):
            if dp[b] == INF:
                continue
            if dp[b] + traceA < n:
                next_dp[b] = min(next_dp[b], dp[b] + traceA)
            if b + traceB < m:
                next_dp[b + traceB] = min(next_dp[b + traceB], dp[b])

        dp = next_dp

    answer = min(dp)

    return answer if answer < n else -1
