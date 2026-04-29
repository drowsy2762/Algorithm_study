# https://www.acmicpc.net/problem/16954
# 2026-03-23
import sys
from collections import deque
input = sys.stdin.readline

dr, dc = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, 1, 1, 1, 0, -1, -1, -1]

def bfs():
    q = deque([(7, 0, 0)])
    while q:
        r, c, t = q.popleft()
        if t >= 8:
            return 1
        for i in range(9):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 8 and 0 <= nc < 8:
                if nr - t >= 0 and chess[nr - t][nc] == '#':
                    continue
                if nr - (t + 1) >= 0 and chess[nr - (t + 1)][nc] == '#':
                    continue
                if nr == 0 and nc == 7:
                    return 1
                q.append((nr, nc, t + 1))
    return 0

chess = [input().rstrip() for _ in range(8)]

print(bfs())