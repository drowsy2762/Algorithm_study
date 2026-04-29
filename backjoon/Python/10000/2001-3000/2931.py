# https://www.acmicpc.net/problem/2931
# 2026-03-19
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

pipe_dir = {
    '|': {0: 0, 2: 2},
    '-': {1: 1, 3: 3},
    '+': {0: 0, 1: 1, 2: 2, 3: 3},
    '1': {2: 1, 3: 0},
    '2': {0: 1, 3: 2},
    '3': {0: 3, 1: 2},
    '4': {2: 3, 1: 0}
}

pipe_map = {
    (True, True, True, True): '+',
    (True, True, False, False): '|',
    (False, False, True, True): '-',
    (False, True, False, True): '1',
    (True, False, False, True): '2',
    (True, False, True, False): '3',
    (False, True, True, False): '4'
}

mr, mc = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'M':
            mr, mc = i, j
curr_r, curr_c, curr_dir = -1, -1, -1
for i in range(4):
    nr, nc = mr + dr[i], mc + dc[i]
    if 0 <= nr < r and 0 <= nc < c:
        pipe = graph[nr][nc]
        if i == 0 and pipe in '|+23':
            curr_r, curr_c, curr_dir = nr, nc, 0
            break
        elif i == 1 and pipe in '-+34':
            curr_r, curr_c, curr_dir = nr, nc, 1
            break
        elif i == 2 and pipe in '|+14':
            curr_r, curr_c, curr_dir = nr, nc, 2
            break
        elif i == 3 and pipe in '-+12':
            curr_r, curr_c, curr_dir = nr, nc, 3
            break
er, ec = -1, -1

while True:
    pipe = graph[curr_r][curr_c]
    
    if pipe == '.':
        er, ec = curr_r, curr_c
        break 
    curr_dir = pipe_dir[pipe][curr_dir]
    curr_r += dr[curr_dir]
    curr_c += dc[curr_dir]

up = er > 0 and graph[er - 1][ec] in '|+14'
down = er + 1 < r and graph[er + 1][ec] in '|+23'
left = ec > 0 and graph[er][ec - 1] in '-+12'
right = ec + 1 < c and graph[er][ec + 1] in '-+34'

ans_pipe = pipe_map[(up, down, left, right)]

print(f"{er + 1} {ec + 1} {ans_pipe}")