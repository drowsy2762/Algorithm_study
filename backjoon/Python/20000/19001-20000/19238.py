# https://www.acmicpc.net/problem/19238
# 2026-02-15
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, fuel = map(int, input().split())
# 0: 빈칸, 1: 벽
board = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1

passengers = {}
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    passengers[(r1-1, c1-1)] = (r2-1, c2-1)

def bfs_find_passenger(start_x, start_y):
    if (start_x, start_y) in passengers:
        return 0, start_x, start_y

    q = deque([(start_x, start_y)])
    visited = [[-1] * n for _ in range(n)]
    visited[start_x][start_y] = 0
    
    candidates = []
    min_dist = float('inf')

    while q:
        x, y = q.popleft()

        if visited[x][y] >= min_dist:
            break 

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and board[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    
                    if (nx, ny) in passengers:
                        min_dist = visited[nx][ny] 
                        candidates.append((visited[nx][ny], nx, ny))
                    
                    q.append((nx, ny))

    if not candidates:
        return -1, -1, -1

    candidates.sort()
    return candidates[0]

def bfs_move_to_dest(start_x, start_y, dest_x, dest_y):
    q = deque([(start_x, start_y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[start_x][start_y] = True

    while q:
        x, y, dist = q.popleft()

        if x == dest_x and y == dest_y:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    
    return -1

success_count = 0
while success_count < m:
    dist, p_x, p_y = bfs_find_passenger(taxi_x, taxi_y)
    
    if dist == -1 or fuel < dist:
        print(-1)
        break
    
    fuel -= dist 
    
    dest_x, dest_y = passengers[(p_x, p_y)]
    del passengers[(p_x, p_y)]
    
    dist_to_dest = bfs_move_to_dest(p_x, p_y, dest_x, dest_y)
    
    if dist_to_dest == -1 or fuel < dist_to_dest:
        print(-1)
        break
        
    fuel += dist_to_dest 
    success_count += 1
    taxi_x, taxi_y = dest_x, dest_y

else:
    print(fuel)