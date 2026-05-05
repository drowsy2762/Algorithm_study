# 2026-05-05


def solution(n):
    if n % 2 != 0:
        return 0

    MOD = 1000000007
    dp = [0] * (n + 1)

    dp[0] = 1
    if n >= 2:
        dp[2] = 3

    unique_sum = 0

    for i in range(4, n + 1, 2):
        unique_sum = (unique_sum + dp[i - 4]) % MOD
        dp[i] = (dp[i - 2] * 3 + unique_sum * 2) % MOD

    return dp[n]
