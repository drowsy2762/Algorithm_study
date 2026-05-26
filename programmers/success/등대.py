# 2026-05-26


import sys

sys.setrecursionlimit(200000)


def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for u, v in lighthouse:
        graph[u].append(v)
        graph[v].append(u)

    dp = [[0, 1] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child][0], dp[child][1])

    dfs(1)

    return min(dp[1][0], dp[1][1])
