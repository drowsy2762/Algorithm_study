# https://www.acmicpc.net/problem/23290
# 2026-02-26
import sys
from collections import deque
input = sys.stdin.readline

dr, dc = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
sr, sc = [-1, 0, 1, 0], [0, -1, 0, 1]

graph = [[deque() for _ in range(4)] for _ in range(4)]
smells = [[0] * 4 for _ in range(4)]

M, S = map(int, input().split())
for _ in range(M):
    fish_x, fish_y, d = map(int, input().split())
    graph[fish_x-1][fish_y-1].append(d-1)
shark_r, shark_c = map(int, input().split())
shark_r -= 1
shark_c -= 1

def copy_magic_and_move_fish():
    new_graph = [[deque() for _ in range(4)] for _ in range(4)]
    moved_graph = [[deque() for _ in range(4)] for _ in range(4)]
    
    for r in range(4):
        for c in range(4):
            while graph[r][c]:
                d = graph[r][c].popleft()
                new_graph[r][c].append(d) 
                
                can_move = False
                for i in range(8):
                    td = (d - i) % 8
                    nr, nc = r + dr[td], c + dc[td]
                    if 0 <= nr < 4 and 0 <= nc < 4 and smells[nr][nc] == 0 and (nr != shark_r or nc != shark_c):
                        moved_graph[nr][nc].append(td)
                        can_move = True
                        break 
                
                if not can_move:
                    moved_graph[r][c].append(d)

    for r in range(4):
        for c in range(4):
            graph[r][c] = moved_graph[r][c]

    return new_graph

def shark_move():
    global shark_r, shark_c
    max_fish = -1 
    best_path = []
    
    for fd in range(4):
        for sd in range(4):
            for td in range(4):
                r1, c1 = shark_r + sr[fd], shark_c + sc[fd]
                r2, c2 = r1 + sr[sd], c1 + sc[sd]
                r3, c3 = r2 + sr[td], c2 + sc[td]
                
                if (0 <= r1 < 4 and 0 <= c1 < 4) and (0 <= r2 < 4 and 0 <= c2 < 4) and (0 <= r3 < 4 and 0 <= c3 < 4):
                    visited_cells = set([(r1, c1), (r2, c2), (r3, c3)])
                    current_fish = 0
                    for r, c in visited_cells:
                        current_fish += len(graph[r][c])
                    if current_fish > max_fish:
                        max_fish = current_fish
                        best_path = [(r1, c1), (r2, c2), (r3, c3)]
                        
    for r, c in best_path:
        if len(graph[r][c]) > 0:      
            graph[r][c] = deque()
            smells[r][c] = 3           
            
    shark_r, shark_c = best_path[-1][0], best_path[-1][1]

def smell_delete():
    for r in range(4):
        for c in range(4):
            if smells[r][c] > 0:
                smells[r][c] -= 1

for _ in range(S):
    new_graph = copy_magic_and_move_fish()
    shark_move()
    smell_delete()
    for r in range(4):
        for c in range(4):
            while new_graph[r][c]:
                tempd = new_graph[r][c].popleft()
                graph[r][c].append(tempd)

ans = 0

for r in range(4):
    for c in range(4):
        while graph[r][c]:
            graph[r][c].pop()
            ans += 1

print(ans)
# 물고기는 중복 가능
# 물고기 냄새는 격자에서 제외되는 물고기가 남김

