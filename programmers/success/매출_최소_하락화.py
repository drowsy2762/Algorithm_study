# 2026-05-14


def solution(sales, links):
    n = len(sales)
    tree = [[] for _ in range(n + 1)]
    dp = [[0, 0] for _ in range(n + 1)]
    for i, j in links:
        tree[i].append(j)

    def dfs(curr):
        dp[curr][1] = sales[curr - 1]
        dp[curr][0] = 0
        if not tree[curr]:
            return
        flag = False
        min_diff = float("inf")

        for member in tree[curr]:
            dfs(member)
            dp[curr][1] += min(dp[member][0], dp[member][1])
            dp[curr][0] += min(dp[member][0], dp[member][1])
            if dp[member][1] <= dp[member][0]:
                flag = True
            else:
                min_diff = min(min_diff, dp[member][1] - dp[member][0])
        if not flag:
            dp[curr][0] += min_diff

    dfs(1)

    return min(dp[1][0], dp[1][1])
