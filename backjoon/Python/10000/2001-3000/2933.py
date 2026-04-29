# https://www.acmicpc.net/problem/2933 : 미네랄 (python3)
from collections import deque
from sys import stdin

# 입력 최적화
input = stdin.readline

# 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
turn = True


def destroy(y):
    global turn, cave
    if turn == True:
        turn = False
        for i in range(c):
            if cave[r - y][i] == "x":
                cave[r - y][i] = "."
                break
    else:
        turn = True
        for i in range(c - 1, -1, -1):
            if cave[r - y][i] == "x":
                cave[r - y][i] = "."
                break


def find_cluster():
    visited = [[False] * c for _ in range(r)]
    q = deque()
    for i in range(c):
        if visited[r - 1][i] == False and cave[r - 1][i] == "x":
            visited[r - 1][i] = True
            q.append((r - 1, i))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < r
                and 0 <= ny < c
                and not visited[nx][ny]
                and cave[nx][ny] == "x"
            ):
                visited[nx][ny] = True
                q.append((nx, ny))
    cluster = []
    for i in range(r - 1, -1, -1):
        for j in range(c):
            if visited[i][j] == False and cave[i][j] == "x":
                cluster.append((i, j))
    if not cluster:
        return cluster, 1, visited
    else:
        return cluster, 0, visited


def drop_cluster(cluster, visited):
    down_min = 1e9
    for x, y in cluster:
        down = 0
        while x + down + 1 < r and visited[x + down + 1][y] == False:
            down += 1
        down_min = min(down_min, down)
    for x, y in cluster:
        cave[x][y] = "."
        cave[x + down_min][y] = "x"


# 메인 함수
def solution():
    global cave, r, c
    r, c = map(int, input().split())
    cave = [list(input().strip()) for _ in range(r)]
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(n):
        destroy(heights[i])
        cluster, flag, visited = find_cluster()
        if flag == 0:
            drop_cluster(cluster, visited)

    for i in range(r):
        print("".join(cave[i]))


solution()
