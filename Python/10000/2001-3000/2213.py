# https://www.acmicpc.net/problem/2213
# 2026-04-26
import sys

sys.setrecursionlimit(20000)

def solution():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    ptr = 0
    n = int(input_data[ptr]); ptr += 1
    
    weights = [0] + [int(x) for x in input_data[ptr:ptr+n]]
    ptr += n
    
    adj = [[] for _ in range(n + 1)]
    while ptr < len(input_data):
        u = int(input_data[ptr]); ptr += 1
        v = int(input_data[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    tree = [[] for _ in range(n + 1)]

    def dfs(curr):
        visited[curr] = True
        dp[curr][0] = 0
        dp[curr][1] = weights[curr]
        
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                tree[curr].append(neighbor)
                dfs(neighbor)
                dp[curr][0] += max(dp[neighbor][0], dp[neighbor][1])
                dp[curr][1] += dp[neighbor][0]

    dfs(1)

    res_nodes = []
    def backtrack(curr, include):
        if include:
            res_nodes.append(curr)
            for child in tree[curr]:
                backtrack(child, False)
        else:
            for child in tree[curr]:
                if dp[child][1] > dp[child][0]:
                    backtrack(child, True)
                else:
                    backtrack(child, False)

    if dp[1][1] > dp[1][0]:
        backtrack(1, True)
    else:
        backtrack(1, False)

    print(max(dp[1][0], dp[1][1]))
    res_nodes.sort()
    print(*(res_nodes))

if __name__ == "__main__":
    solution()