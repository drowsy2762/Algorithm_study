# https://www.acmicpc.net/problem/3190
# 2025-10-02
from sys import stdin
from collections import deque
input = stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def solution():
    n = int(input())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    
    k = int(input())
    for _ in range(k):
        r, c = map(int, input().split())
        board[r][c] = 2  

    l = int(input())
    turns = {}
    for _ in range(l):
        sec, d = input().split()
        turns[int(sec)] = d

    time = 0
    y, x = 1, 1
    direction = 0  
    
    snake_body = deque([(y, x)])
    snake_set = {(y, x)}

    while True:
        time += 1
        ny, nx = y + dy[direction], x + dx[direction]

        if not (1 <= ny <= n and 1 <= nx <= n) or (ny, nx) in snake_set:
            break

        snake_body.append((ny, nx))
        snake_set.add((ny, nx))
        
        if board[ny][nx] != 2:  
            tail_y, tail_x = snake_body.popleft()
            snake_set.remove((tail_y, tail_x))
        else:  
            board[ny][nx] = 0 

        y, x = ny, nx

        if time in turns:
            if turns[time] == 'D': 
                direction = (direction + 1) % 4
            else: 
                direction = (direction - 1 + 4) % 4
                
    print(time)

solution()