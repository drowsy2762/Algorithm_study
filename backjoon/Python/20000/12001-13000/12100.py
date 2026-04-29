# https://www.acmicpc.net/problem/12100
# 2025-10-04
from sys import stdin
import copy
input = stdin.readline

n = int(input())
initial_map = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def move(board, direction):
    if direction == 0: # 상
        for j in range(n):
            cursor = 0
            for i in range(1, n):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[cursor][j] == 0:
                        board[cursor][j] = tmp
                    elif board[cursor][j] == tmp:
                        board[cursor][j] *= 2
                        cursor += 1
                    else:
                        cursor += 1
                        board[cursor][j] = tmp

    elif direction == 1: # 하
        for j in range(n):
            cursor = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[cursor][j] == 0:
                        board[cursor][j] = tmp
                    elif board[cursor][j] == tmp:
                        board[cursor][j] *= 2
                        cursor -= 1
                    else:
                        cursor -= 1
                        board[cursor][j] = tmp

    elif direction == 2: # 좌
        for i in range(n):
            cursor = 0
            for j in range(1, n):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][cursor] == 0:
                        board[i][cursor] = tmp
                    elif board[i][cursor] == tmp:
                        board[i][cursor] *= 2
                        cursor += 1
                    else:
                        cursor += 1
                        board[i][cursor] = tmp
                        
    else: # 우
        for i in range(n):
            cursor = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j] != 0:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][cursor] == 0:
                        board[i][cursor] = tmp
                    elif board[i][cursor] == tmp:
                        board[i][cursor] *= 2
                        cursor -= 1
                    else:
                        cursor -= 1
                        board[i][cursor] = tmp
    return board

def dfs(N, arr):
    global ans
    if N == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, arr[i][j])
        return
    
    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        moved_arr = move(copy_arr, i)
        dfs(N + 1, moved_arr)

for r in range(n):
    for c in range(n):
        ans = max(ans, initial_map[r][c])

dfs(0, initial_map)
print(ans)