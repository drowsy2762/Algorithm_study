# https://www.acmicpc.net/problem/2533
# 2026-04-27
import sys

def solve():
    input_data = iter(sys.stdin.read().split())
    
    try:
        n = int(next(input_data))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(input_data))
        v = int(next(input_data))
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0, 1] for _ in range(n + 1)]
    
    order = []
    stack = [1]
    parents = [0] * (n + 1)
    visited = [False] * (n + 1)
    visited[1] = True
    
    visited_order = []
    stack = [1]
    while stack:
        curr = stack.pop()
        visited_order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = curr
                stack.append(neighbor)

    for curr in reversed(visited_order):
        for neighbor in adj[curr]:
            if neighbor != parents[curr]:
                dp[curr][0] += dp[neighbor][1]
                dp[curr][1] += min(dp[neighbor][0], dp[neighbor][1])

    sys.stdout.write(str(min(dp[1][0], dp[1][1])) + '\n')

if __name__ == "__main__":
    solve()