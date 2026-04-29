# https://www.acmicpc.net/problem/21609
# 2026-02-20
from sys import stdin
from collections import deque
input = stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 종료조건 블록그룹이 모두 사라질 때 까지 

# 검은색블록을 제외한 나머지 그룹을 서치함
def find_block_group():
    # 그룹에 속해있는지 확인
    visited = [[False for _ in range(n)] for _ in range(n)]
    candidates = []
    for y in range(n):
        for x in range(n):
            # 이미 다른 그룹에 소속된 노드인지 확인
            if visited[y][x] == True or graph[y][x] <= 0:
                continue

            # bfs 과정
            q = deque()
            q.append((y, x))
            visited[y][x] = True
            cnt = 1

            color = graph[y][x]
            rainbow = []
            blocks = [(y, x)]
            while q:
                cy, cx = q.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < n and 0 <= nx < n:
                        if not visited[ny][nx]:
                            if graph[ny][nx] == color:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                                blocks.append((ny, nx))
                            elif graph[ny][nx] == 0:
                                visited[ny][nx] = True
                                cnt += 1
                                q.append((ny, nx))
                                rainbow.append((ny, nx))
                                blocks.append((ny, nx))

            if cnt >= 2:
                candidates.append([cnt, len(rainbow), y, x, blocks])

            for ry, rx in rainbow:
                visited[ry][rx] = False

    if not candidates:
        return []
    
    candidates.sort(reverse=True)
    return candidates[0][4]

def gravity():
    for x in range(n):
        for y in range(n - 2, -1, -1):
            if graph[y][x] >= 0: 
                ny = y
                while ny + 1 < n and graph[ny + 1][x] == -2:
                    graph[ny + 1][x] = graph[ny][x]
                    graph[ny][x] = -2
                    ny += 1

def solution():
    global graph
    score = 0
    while True:
        blocks = find_block_group()
        if not blocks:
            break
        score += len(blocks) ** 2
        for y, x in blocks:
            graph[y][x] = -2
        gravity()
        graph = list(map(list, zip(*graph)))[::-1]
        gravity()
        
    print(score)

solution()