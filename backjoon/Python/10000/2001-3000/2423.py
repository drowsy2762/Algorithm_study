# https://www.acmicpc.net/problem/2423 : 전구를 켜라 (python3)
from sys import stdin

input = stdin.read

grid = []
n, m = map(int, input().split())

for i in range(n):
    temp = input().strip()
    grid.append(temp)

print(grid)
