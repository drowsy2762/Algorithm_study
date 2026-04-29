# https://www.acmicpc.net/problem/17837
# 2026-02-09
import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, k = map(int, input().split())
# 0: 흰색, 1: 빨강, 2: 파랑
board = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
print(chess_map)
horses = []

for i in range(k):
    x, y, d = map(int, input().split())
    horses.append([x-1, y-1, d])
    chess_map[x-1][y-1].append(i) 

def get_reverse_dir(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3

def solution():
    turn = 0
    while turn < 1000:
        turn += 1
        for i in range(k):
            x, y, d = horses[i]
            nx = x + dx[d]
            ny = y + dy[d]

            # 파란색 or 벽
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                d = get_reverse_dir(d)
                horses[i][2] = d 
                nx = x + dx[d]
                ny = y + dy[d]
                
                # 또 벽이거나 파란색
                if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                    continue
            
            # 흰색 or 빨강
            stack = chess_map[x][y]
            idx = stack.index(i)
            
            moving_stack = stack[idx:] 
            chess_map[x][y] = stack[:idx] 
            
            if board[nx][ny] == 1: 
                moving_stack.reverse() 

            chess_map[nx][ny].extend(moving_stack)
            
            for horse_idx in moving_stack:
                horses[horse_idx][0] = nx
                horses[horse_idx][1] = ny

            if len(chess_map[nx][ny]) >= 4:
                return turn
                
    return -1

print(solution())