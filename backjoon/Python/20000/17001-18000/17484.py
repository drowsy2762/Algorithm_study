# https://www.acmicpc.net/problem/17484 : 진우의 달 여행 (small) (python3)
# 2023-10-13
import sys

n, m = map(int, sys.stdin.readline().split(" "))
matrix = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)]

direction = [-1, 0, 1]


def dfs(col, row, d, low, answer):
    if col == n - 1:
        return min(low, answer)
    for i in direction:
        if i != d:
            if 0 <= col < n and 0 <= row + i < m:
                low = dfs(col + 1, row + i, i, low, answer + matrix[col + 1][row + i])
    return low


low = int(sys.maxsize)
for i in range(m):
    low = min(dfs(0, i, 2, low, matrix[0][i]), low)

print(low)
