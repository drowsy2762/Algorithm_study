# https://www.acmicpc.net/problem/14499
# 2025-10-10
from sys import stdin

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(dice, direction):
    top, bottom, east, west, south, north = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1: # 동
        dice[0], dice[2], dice[1], dice[3] = west, top, east, bottom
    elif direction == 2: # 서
        dice[0], dice[3], dice[1], dice[2] = east, top, west, bottom
    elif direction == 3: # 북
        dice[0], dice[5], dice[1], dice[4] = south, top, north, bottom
    else: # 남
        dice[0], dice[4], dice[1], dice[5] = north, top, south, bottom
    
    return dice

def solution():
    n, m, x, y, k = map(int,input().split())
    dice = [0, 0, 0, 0, 0, 0]
    graphs = [list(map(int, input().rstrip().split())) for _ in range(n)]
    directions = list(map(int, input().rstrip().split()))

    for i in range(k):
        order = directions[i]
        nx = x + dx[order - 1]
        ny = y + dy[order - 1]

        if not (0 <= nx < n and 0 <= ny < m):
            continue
            
        dice = move(dice, order)

        if graphs[nx][ny] == 0:
            graphs[nx][ny] = dice[1]
        else:
            dice[1] = graphs[nx][ny] 
            graphs[nx][ny] = 0
            
        x, y = nx, ny
        print(dice[0])

solution()