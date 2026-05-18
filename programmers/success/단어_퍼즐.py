# 2026-05-18


def solution(strs, t):
    n = len(t)
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    word_set = set(strs)

    for i in range(1, n + 1):
        for length in range(1, min(i, 5) + 1):
            if dp[i - length] != float("inf"):
                if t[i - length : i] in word_set:
                    if dp[i - length] + 1 < dp[i]:
                        dp[i] = dp[i - length] + 1

    return dp[n] if dp[n] != float("inf") else -1
