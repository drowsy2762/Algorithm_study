# https://www.acmicpc.net/problem/1987 : 알파벳 (python3)
# 2024-02-13
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


r, c = map(int, input().split())

maps = []
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    maps.append(input().strip())

spells = set(maps[0][0])


def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in spells:
            spells.add(maps[nx][ny])
            dfs(nx, ny, count + 1)
            spells.remove(maps[nx][ny])


dfs(0, 0, 1)
print(answer)
