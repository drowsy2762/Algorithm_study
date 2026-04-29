# https://www.acmicpc.net/problem/17780
# 2026-03-02
import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
rev_dir = [0, 2, 1, 4, 3]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
horses = []

for i in range(k):
    x, y, d = map(int, input().split())
    horses.append([x-1, y-1, d])
    chess_map[x-1][y-1].append(i) 

def solution():
    turn = 0
    while turn < 1000:
        turn += 1
        for i in range(k):
            x, y, d = horses[i]
            if chess_map[x][y][0] != i:
                continue 
                
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                d = rev_dir[d]
                horses[i][2] = d 
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                    continue
            
            stack = chess_map[x][y]
            moving_stack = stack[:] 
            chess_map[x][y] = []  
            
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