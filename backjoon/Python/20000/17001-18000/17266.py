# https://www.acmicpc.net/problem/17266 : 어두운 굴다리(python3)
# 2023-10-03
from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

max_size = 0
for i in range(1, m):
    max_size = max(max_size, arr[i] - arr[i - 1])

print(max((max_size + 1) // 2, arr[0] - 0, n - arr[-1]))
