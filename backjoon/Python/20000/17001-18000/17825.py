# https://www.acmicpc.net/problem/17825
# 2026-02-11
from sys import stdin
input = stdin.readline

graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 
         40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

move_table = [[0] * 6 for _ in range(33)]
for i in range(32):
    for d in range(1, 6):
        curr = graph[i][1] if len(graph[i]) == 2 else graph[i][0]
        for _ in range(d - 1):
            curr = graph[curr][0]
        move_table[i][d] = curr
move_table[32] = [32] * 6 

dice = list(map(int, input().split()))
ans = 0
horses = [0, 0, 0, 0]
occupied = [False] * 33

def backtracking(depth, total):
    global ans
    if depth == 10:
        ans = max(ans, total)
        return

    moved_start_horse = False
    
    for i in range(4):
        curr_pos = horses[i]

        if curr_pos == 32:
            continue
            
        if curr_pos == 0:
            if moved_start_horse: continue
            moved_start_horse = True
            
        next_pos = move_table[curr_pos][dice[depth]]
        
        if next_pos != 32 and occupied[next_pos]:
            continue
            
        occupied[curr_pos] = False
        occupied[next_pos] = True
        horses[i] = next_pos
        
        backtracking(depth + 1, total + score[next_pos])
        
        horses[i] = curr_pos
        occupied[next_pos] = False
        occupied[curr_pos] = True if curr_pos != 0 else False

backtracking(0, 0)
print(ans)