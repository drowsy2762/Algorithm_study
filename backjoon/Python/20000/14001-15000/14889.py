# https://www.acmicpc.net/problem/14889
# 2026-01-10
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

res = sys.maxsize


def dfs(l, idx):
    global res

    if l == n//2:
        start = 0
        link = 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]

        res = min(res, abs(start-link))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(l+1, i+1)
            visited[i] = False

dfs(0, 0)
print(res)