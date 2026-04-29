# https://www.acmicpc.net/problem/5213
# 2026-04-03
import sys
from collections import deque
input = sys.stdin.readline

odd_dx = [-1, 1, 0, -1, 1, 0]
odd_dy = [0, 0, -1, 1, 1, 1]
even_dx = [-1, 1, 0, -1, 1, 0]
even_dy = [-1, -1, -1, 0, 0, 1]

def solution():
    n = int(input())

    if n == 1:
        print(1)
        print(1)
        return

    tile = [[None] * n for _ in range(n)]
    d = [[0] * n for _ in range(n)]
    move = [[None] * n for _ in range(n)]
    number = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                tile[i][j] = list(map(int, input().split()))
                number[i][j] = num
                num += 1
        else:
            for j in range(n - 1):
                tile[i][j] = list(map(int, input().split()))
                number[i][j] = num
                num += 1

    def bfs():
        q = deque([(0, 0)])
        d[0][0] = 1
        while q:
            x, y = q.popleft()
            dx, dy = (even_dx, even_dy) if x % 2 == 0 else (odd_dx, odd_dy)
            for i in range(6):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and tile[nx][ny] is not None:
                    if i <= 2:
                        if tile[x][y][0] == tile[nx][ny][1] and d[nx][ny] == 0:
                            d[nx][ny] = d[x][y] + 1
                            move[nx][ny] = (x, y)
                            q.append((nx, ny))
                    else:
                        if tile[x][y][1] == tile[nx][ny][0] and d[nx][ny] == 0:
                            d[nx][ny] = d[x][y] + 1
                            move[nx][ny] = (x, y)
                            q.append((nx, ny))

    bfs()

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if d[i][j] != 0:
                print(d[i][j])
                path = []
                curr_x, curr_y = i, j
                while True:
                    path.append(number[curr_x][curr_y])
                    if curr_x == 0 and curr_y == 0:
                        break 
                    curr_x, curr_y = move[curr_x][curr_y]
                
                path.reverse()
                print(" ".join(map(str, path)))
                return

if __name__ == "__main__":
    solution()