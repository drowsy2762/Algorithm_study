# https://www.acmicpc.net/problem/19236
# 2026-02-13
from sys import stdin
from copy import deepcopy
input = stdin.readline

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]

max_score = 0
n = [list(map(int, input().split())) for _ in range(4)]
fishs = [[0] * 4 for _ in range(4)]
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ / 1부터
directions = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        fishs[i][j] = n[i][j * 2]
        directions[i][j] = n[i][(j * 2) + 1] - 1

# 상어는 -1
# 종료조건은 상어가 더 이상 움직이지 못할때

def fish_move(shark_x, shark_y, fish, Dir):
    for cnt in range(1, 17):
        x, y = -1, -1
        for i in range(4):
            for j in range(4):
                if fish[i][j] == cnt:
                    x, y = i, j
                    break
            if x != -1: break
        if x == -1:
            continue
        current_dir = Dir[x][y]
        
        for k in range(8):
            nd = (current_dir + k) % 8
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == shark_x and ny == shark_y):
                    Dir[x][y] = nd
                    fish[x][y], fish[nx][ny] = fish[nx][ny], fish[x][y]
                    Dir[x][y], Dir[nx][ny] = Dir[nx][ny], Dir[x][y]
                    break
                    
    return fish, Dir

def shark_moves(shark_x, shark_y, fish, Dir):
    moves = []
    d = Dir[shark_x][shark_y]
    for step in range(1, 4):
        nx = shark_x + dx[d] * step
        ny = shark_y + dy[d] * step
        if 0 <= nx < 4 and 0 <= ny < 4:
            if fish[nx][ny] > 0:
                moves.append([nx, ny])
        else:
            break
            
    return moves

def dfs(shark_x, shark_y, fish, Dir, score):
    global max_score
    score += fish[shark_x][shark_y]
    max_score = max(score, max_score)
    fish[shark_x][shark_y] = -1

    fish, Dir = fish_move(shark_x, shark_y, fish, Dir)
    moves = shark_moves(shark_x, shark_y, fish, Dir)

    for nx, ny in moves:
        if fish[nx][ny] > 0:
            c_fish = deepcopy(fish)
            c_dir = deepcopy(Dir)
            c_fish[shark_x][shark_y] = 0
            dfs(nx, ny, c_fish, c_dir, score)
    
dfs(0, 0, fishs, directions, 0)
print(max_score)