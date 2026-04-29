# https://www.acmicpc.net/problem/18500
# 2026-03-03
import sys
from collections import deque
input = sys.stdin.readline

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
int(input())
sticks = list(map(int, input().split()))

def destroy(r_idx, c_idx, turn):
    # turn True: 왼쪽 -> 오른쪽 / False: 오른쪽 -> 왼쪽
    rng = range(c_idx) if turn else range(c_idx - 1, -1, -1)
    for j in rng:
        if graph[r_idx][j] == 'x':
            graph[r_idx][j] = '.'
            return r_idx, j
    return None

def floating_cluster(start_r, start_c):
    if graph[start_r][start_c] == '.': return None
    visited = {(start_r, start_c)}
    q = deque([(start_r, start_c)])
    floating = True
    cluster = [(start_r, start_c)]

    while q:
        cur_r, cur_c = q.popleft()
        if cur_r == R - 1:
            return None

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]
            if (0 <= nr < R and 0 <= nc < C) and graph[nr][nc] == 'x' and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))
                cluster.append((nr, nc))
    return cluster

def gravity_cluster(cluster, r, c):
    for r_idx, c_idx in cluster:
        graph[r_idx][c_idx] = '.'
    fall_dist = R
    for r_idx, c_idx in cluster:
        d = 0
        for k in range(r_idx + 1, R):
            if graph[k][c_idx] == 'x':
                break
            d += 1
        else: 
            pass
        fall_dist = min(fall_dist, d)
    
    for r_idx, c_idx in cluster:
        graph[r_idx + fall_dist][c_idx] = 'x'

turn = True

for h in sticks:
    target_r = R - h
    destroyed_pos = destroy(target_r, C, turn)
    turn = not turn # 방향 전환
    
    if destroyed_pos:
        r_pos, c_pos = destroyed_pos
        for i in range(4):
            nr, nc = r_pos + dr[i], c_pos + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                cluster = floating_cluster(nr, nc)
                if cluster:
                    gravity_cluster(cluster, R, C)
                    break 

for row in graph:
    print("".join(row))