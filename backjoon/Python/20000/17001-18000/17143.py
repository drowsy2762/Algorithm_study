# https://www.acmicpc.net/problem/17143
# 2026-01-24
from sys import stdin
from collections import deque
input = stdin.readline

dc, dr = [0, 0, 1, -1], [-1, 1, 0, 0]

R, C, M = map(int, input().split())
graph = [[None] * C for _ in range(R)]

ans = 0

# 상어끼리 위치가 겹치면 크기가 큰 상어가 잡아먹는다
for i in range(M):
    # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽 d-1로 변환해서 계산
    # s는 속력 (칸 / 초), z는 크기
    r, c, s, d, z = map(int, input().split())
    graph[r-1][c-1] = (s, d-1, z)

# 낚시왕 이동 후 낚시, 그 후 상어 이동
for c in range(C):
    # 상어 낚시
    for r in range(R):
        if graph[r][c] is not None:
            ans += graph[r][c][2]
            graph[r][c] = None 
            break 
    
    # 상어의 이동
    new_graph = [[None] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if graph[r][c] is not None:
                s, d, z = graph[r][c]
                nr, nc, nd = r, c, d
                if d <= 1: 
                    if R > 1:
                        dist = s % ((R - 1) * 2) 
                        for _ in range(dist):
                            if nr + dr[nd] < 0 or nr + dr[nd] >= R:
                                nd = 1 - nd 
                            nr += dr[nd]
                
                else: 
                    if C > 1:
                        dist = s % ((C - 1) * 2)
                        for _ in range(dist):
                            if nc + dc[nd] < 0 or nc + dc[nd] >= C:
                                nd = 5 - nd
                            nc += dc[nd]
                
                if new_graph[nr][nc]:
                    if z > new_graph[nr][nc][2]:
                        new_graph[nr][nc] = (s, nd, z)
                else:
                    new_graph[nr][nc] = (s, nd, z)
    
    # 모든 이동이 끝나면 그래프 갱신
    graph = new_graph

print(ans)