# https://www.acmicpc.net/problem/1949
# 2026-04-28
import sys

def solution():
    input_data = iter(sys.stdin.read().split())
    try:
        n = int(next(input_data))
    except StopIteration:
        return
    
    pops = [0] + [int(next(input_data)) for _ in range(n)]
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = int(next(input_data)), int(next(input_data))
        adj[u].append(v)
        adj[v].append(u)

    order = []
    stack = [1]
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    visited[1] = True
    
    while stack:
        curr = stack.pop()
        order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                stack.append(neighbor)

    dp = [[0, 0] for _ in range(n + 1)]
    
    for curr in reversed(order):
        dp[curr][1] = pops[curr] 
        dp[curr][0] = 0 
        
        for neighbor in adj[curr]:
            if neighbor != parent[curr]:
                dp[curr][0] += max(dp[neighbor][0], dp[neighbor][1])
                dp[curr][1] += dp[neighbor][0]

    sys.stdout.write(str(max(dp[1])) + '\n')

if __name__ == "__main__":
    solution()