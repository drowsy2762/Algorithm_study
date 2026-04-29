# https://www.acmicpc.net/problem/13460 
# 2025-09-28

from collections import deque
from sys import stdin
input = stdin.readline

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
for i in range(n):  # n, m 순서에 맞게 수정
    for j in range(m):
        if graph[i][j] == "R":
            rx, ry = i, j
        elif graph[i][j] == "B":
            bx, by = i, j

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 0))  # 튜플로 묶어서 전달, 카운트도 추가
    visited = set()
    visited.add((rx, ry, bx, by))
    
    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        
        if cnt >= 10:
            print(-1)
            return
            
        for i in range(4):
            rnx, rny = rx, ry  # 올바른 변수 할당
            # 빨간 구슬 이동
            while True:
                rnx += dx[i]
                rny += dy[i]
                if graph[rnx][rny] == '#':  # 벽에 닿았을 때
                    rnx -= dx[i]
                    rny -= dy[i]
                    break
                if graph[rnx][rny] == 'O':  # 구멍에 빠졌을 때
                    break
            
            bnx, bny = bx, by  # 올바른 변수 할당
            # 파란 구슬 이동
            while True:
                bnx += dx[i]
                bny += dy[i]
                if graph[bnx][bny] == '#':  # 벽에 닿았을 때
                    bnx -= dx[i]
                    bny -= dy[i]
                    break
                if graph[bnx][bny] == 'O':  # 구멍에 빠졌을 때
                    break
            
            # 파란 구슬이 구멍에 빠지면 실패
            if graph[bnx][bny] == 'O':
                continue
                
            # 빨간 구슬이 구멍에 빠지면 성공
            if graph[rnx][rny] == 'O':
                print(cnt + 1)
                return
            
            # 두 구슬이 같은 위치에 있으면 조정
            if rnx == bnx and rny == bny:
                if abs(rnx-rx) + abs(rny-ry) > abs(bnx-bx) + abs(bny-by):
                    rnx -= dx[i]
                    rny -= dy[i]
                else:
                    bnx -= dx[i]
                    bny -= dy[i]
            
            # 방문하지 않은 상태라면 큐에 추가
            if (rnx, rny, bnx, bny) not in visited:
                visited.add((rnx, rny, bnx, bny))
                queue.append((rnx, rny, bnx, bny, cnt + 1))
    
    print(-1)

bfs(rx, ry, bx, by)