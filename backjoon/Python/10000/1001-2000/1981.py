# http://acmicpc.net/problem/1981
# 2026-03-17
import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(min_val, max_val):
    if graph[0][0] < min_val or graph[0][0] > max_val:
        return False
    visited = [[False] * n for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        if y == n - 1 and x == n - 1:
            return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if min_val <= graph[ny][nx] <= max_val:
                    visited[ny][nx] = True
                    q.append((ny, nx))
    return False

left = 0 
right = 0 
min_diff = float('inf')

while left <= right and right <= 200: 
    if bfs(left, right):
        min_diff = min(min_diff, right - left)
        left += 1
    else:
        right += 1

print(min_diff)