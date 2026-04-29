# https://www.acmicpc.net/problem/1027 : 고층 건물 (python3)
# 2024-02-21
# 2025-09-30 (retry)
import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = [0] * n
    for i in range(n - 1):
        temp = -sys.maxsize
        for j in range(i + 1, n):
            if temp < (buildings[j] - buildings[i]) / (j - i):
                answer[i] += 1
                answer[j] += 1
                temp = (buildings[j] - buildings[i]) / (j - i)
    print(max(answer))

solution()
