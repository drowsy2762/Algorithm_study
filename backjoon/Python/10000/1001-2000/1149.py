# https://www.acmicpc.net/problem/1149 : RGB거리 (python3)
# 2024-04-08

from sys import stdin

input = stdin.readline


def solution():
    n = int(input())
    house = []
    for _ in range(n):
        red, blue, green = map(int, input().split())
        house.append([red, blue, green])
    for i in range(1, n):
        house[i][0] = min(house[i - 1][1], house[i - 1][2]) + house[i][0]
        house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
        house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]
    print(min(house[n - 1]))
    print(house)


solution()
