# 2026-05-28
def solution(target):
    sb_scores = set([50] + [i for i in range(1, 21)])
    dt_scores = (
        set([i * 2 for i in range(1, 21)] + [i * 3 for i in range(1, 21)]) - sb_scores
    )
    dp = [[float("inf"), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]

    for i in range(1, target + 1):
        for score in sb_scores:
            if i >= score:
                darts, sb = dp[i - score][0] + 1, dp[i - score][1] + 1
                if darts < dp[i][0] or (darts == dp[i][0] and sb > dp[i][1]):
                    dp[i] = [darts, sb]

        for score in dt_scores:
            if i >= score:
                darts, sb = dp[i - score][0] + 1, dp[i - score][1]
                if darts < dp[i][0] or (darts == dp[i][0] and sb > dp[i][1]):
                    dp[i] = [darts, sb]

    return dp[target]
