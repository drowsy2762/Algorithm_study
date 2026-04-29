# https://www.acmicpc.net/problem/21611
# 2026-02-22
import sys
input = sys.stdin.readline

dc, dr = [0, 0, -1, 1], [-1, 1, 0, 0]
dy, dx = [0, 1, 0, -1], [-1, 0, 1, 0]

n, m = map(int, input().split())
shark = n // 2
graph = [list(map(int, input().split())) for _ in range(n)]
graph[shark][shark] = -1
magics = []
ans = 0
for _ in range(m):
    magics.append(list(map(int, input().split())))

def get_1d_marbles():
    marbles = []
    y, x = shark, shark
    for length in range(1, n):
        for i in range(2):
            direction = (length % 2 == 0) * 2 + i 
            for _ in range(length):
                y += dy[direction]
                x += dx[direction]
                if graph[y][x] > 0:
                    marbles.append(graph[y][x])

    for i in range(n-1):
        y += dy[0]
        x += dx[0]
        if graph[y][x] > 0:
            marbles.append(graph[y][x])

    return marbles

def delete_marble(marble):
    if not marble: return [], False
    
    global ans
    boom = False  
    temp = [marble[0]]
    new_marble = []

    for i in range(1, len(marble)):
        if marble[i] == marble[i - 1]:
            temp.append(marble[i])
            
        else:
            if len(temp) > 3:
                ans += temp[0] * len(temp)
                boom = True
            else:
                new_marble.extend(temp) 
            temp = [marble[i]]

    if len(temp) > 3:
        ans += temp[0] * len(temp)
        boom = True
    else:
        new_marble.extend(temp)

    return new_marble, boom


def reposition_marble(marble):
    if not marble: return []
    new_marble = []
    temp = [marble[0]]
    
    for i in range(1, len(marble)):
        if marble[i] == marble[i - 1]:
            temp.append(marble[i])
            
        else:
            new_marble.append(len(temp))
            new_marble.append(temp[0])
            temp = [marble[i]]

    new_marble.append(len(temp))
    new_marble.append(temp[0])

    return new_marble

def fill_2d_marbles(marble):
    new_board = [[0] * n for _ in range(n)]
    y, x = shark, shark
    idx = 0
    for length in range(1, n):
        for i in range(2):
            direction = (length % 2 == 0) * 2 + i 
            for _ in range(length):
                y += dy[direction]
                x += dx[direction]
                
                if idx < len(marble):
                    new_board[y][x] = marble[idx]
                    idx += 1
                else:
                    return new_board
    for _ in range(n - 1):
        y += dy[0]
        x += dx[0]
        if idx < len(marble):
            new_board[y][x] = marble[idx]
            idx += 1
        else:
            return new_board
        
    return new_board

for i in range(m):
    direction, size = magics[i]
    for j in range(size):
        nr, nc = shark + dr[direction-1] * (j + 1), shark + dc[direction-1] * (j + 1)
        graph[nr][nc] = 0
    marble = get_1d_marbles()
    is_boom = True
    while is_boom:
        marble, is_boom = delete_marble(marble)
    marble = reposition_marble(marble)
    graph = fill_2d_marbles(marble)

print(ans)
