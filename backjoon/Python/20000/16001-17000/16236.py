# https://www.acmicpc.net/problem/16236
# 2026-01-22
from sys import stdin
from collections import deque
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

input = stdin.readline

n = int(input())
ocean = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            shark_x, shark_y = i, j
            ocean[i][j] = 0

def bfs(x, y, size):
    visited = [[-1] * n for _ in range(n)] 
    visited[x][y] = 0
    search_q = deque()
    search_q.append([x, y])
    can_eat = []
    while search_q:
        r, c = search_q.popleft()
        for idx in range(4):
            nx, ny = r + dx[idx], c + dy[idx]
            if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == -1:
                if ocean[nx][ny] <= size:
                    visited[nx][ny] = visited[r][c] + 1
                    search_q.append([nx, ny])
                    
                    if 0 < ocean[nx][ny] < size:
                        can_eat.append([visited[nx][ny], nx, ny])
    return sorted(can_eat)

shark_size = 2
eat_feed = 0
while True:
    can_eat = deque(bfs(shark_x, shark_y, shark_size))
    
    if not can_eat:
        break

    distance, x, y = can_eat.popleft()
    ans += distance
    shark_x, shark_y = x, y
    eat_feed += 1
    ocean[x][y] = 0

    if shark_size == eat_feed:
        shark_size += 1
        eat_feed = 0
print(ans)