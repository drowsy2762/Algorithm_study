# https://www.acmicpc.net/problem/2186
# 2026-03-27
import sys
# sys.setrecursionlimit(10**6) 메모리 오류를 발생시킴
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, idx):
    if idx == target_len:
        return 1
    
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    count = 0
    target_char = target[idx] 
    
    for i in range(4):
        nx, ny = x, y
        for _ in range(k):
            nx += dx[i]
            ny += dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == target_char:
                    count += dfs(nx, ny, idx + 1)
            else:
                break 
    dp[x][y][idx] = count
    return count

n, m, k = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)]
target = input().rstrip()
target_len = len(target)
dp = [[[-1] * target_len for _ in range(m)] for _ in range(n)]
res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == target[0]:
            res += dfs(i, j, 1)

print(res)