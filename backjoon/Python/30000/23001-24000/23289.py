# https://www.acmicpc.net/problem/23289
# 2026-02-25
import sys
from collections import deque
input = sys.stdin.readline

# 0:우, 1:좌, 2:상, 3:하
dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]

R, C, K = map(int, input().split())
grid = [[0] * C for _ in range(R)]
room_info = [list(map(int, input().split())) for _ in range(R)]

heaters = []
targets = []

for r in range(R):
    for c in range(C):
        if 1 <= room_info[r][c] <= 4:
            heaters.append((r, c, room_info[r][c]))
        elif room_info[r][c] == 5:
            targets.append((r, c))

w = int(input())
walls = set()
for _ in range(w):
    r, c, t = map(int, input().split())
    r -= 1
    c -= 1
    if t == 0:
        walls.add(((r, c), (r-1, c)))
        walls.add(((r-1, c), (r, c)))
    else:
        walls.add(((r, c), (r, c+1)))
        walls.add(((r, c+1), (r, c)))

def blow_wind(sr, sc, d):
    nr, nc = sr + dr[d], sc + dc[d]
    if not (0 <= nr < R and 0 <= nc < C): return
    if ((sr, sc), (nr, nc)) in walls: return

    visited = [[False] * C for _ in range(R)]
    q = deque([(nr, nc, 5)])
    visited[nr][nc] = True
    grid[nr][nc] += 5 

    while q:
        r, c, power = q.popleft()
        if power == 1: continue 
        
        if d == 0: 
            nr, nc = r - 1, c + 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r-1,c)) not in walls and ((r-1,c), (r-1,c+1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))
            nr, nc = r, c + 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r,c+1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))
            nr, nc = r + 1, c + 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r+1,c)) not in walls and ((r+1,c), (r+1,c+1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

        elif d == 1: 
            nr, nc = r - 1, c - 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r-1,c)) not in walls and ((r-1,c), (r-1,c-1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

            nr, nc = r, c - 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r,c-1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

            nr, nc = r + 1, c - 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r+1,c)) not in walls and ((r+1,c), (r+1,c-1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

        elif d == 2: 
            nr, nc = r - 1, c - 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r,c-1)) not in walls and ((r,c-1), (r-1,c-1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))
            
            nr, nc = r - 1, c
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r-1,c)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

            nr, nc = r - 1, c + 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r,c+1)) not in walls and ((r,c+1), (r-1,c+1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

        elif d == 3: 
            nr, nc = r + 1, c - 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r,c-1)) not in walls and ((r,c-1), (r+1,c-1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

            nr, nc = r + 1, c
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r+1,c)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

            nr, nc = r + 1, c + 1
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if ((r,c), (r,c+1)) not in walls and ((r,c+1), (r+1,c+1)) not in walls:
                    visited[nr][nc] = True
                    grid[nr][nc] += (power - 1)
                    q.append((nr, nc, power - 1))

def adjust_temp():
    temp_grid = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0: continue
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if ((r, c), (nr, nc)) in walls: continue
                    
                    if grid[r][c] > grid[nr][nc]:
                        diff = (grid[r][c] - grid[nr][nc]) // 4
                        if diff > 0:
                            temp_grid[r][c] -= diff
                            temp_grid[nr][nc] += diff

    for r in range(R):
        for c in range(C):
            grid[r][c] += temp_grid[r][c]

def decrease_border():
    for c in range(C):
        if grid[0][c] > 0: grid[0][c] -= 1
        if grid[R-1][c] > 0: grid[R-1][c] -= 1
    for r in range(1, R-1):
        if grid[r][0] > 0: grid[r][0] -= 1
        if grid[r][C-1] > 0: grid[r][C-1] -= 1

chocolate = 0
while chocolate <= 100:
    for r, c, d in heaters:
        blow_wind(r, c, d-1)
    adjust_temp()
    decrease_border()
    chocolate += 1
    
    check = True
    for r, c in targets:
        if grid[r][c] < K:
            check = False
            break
    if check:
        print(chocolate)
        break
else:
    print(101)