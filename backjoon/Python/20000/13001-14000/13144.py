# https://www.acmicpc.net/problem/13144 : List of Unique Numbers (python3)
# 2024-02-16
from sys import stdin
from collections import defaultdict

input = stdin.readline
num_dict = defaultdict(list)

n = int(input().rstrip())
num_list = list(map(int, input().split()))

result = 0
start, end = 0, 0
seq = [False for _ in range(1000001)]
while start < n and end < n:
    if not seq[num_list[end]]:
        seq[num_list[end]] = True
        end += 1
        result += end - start
    else:
        seq[num_list[start]] = False
        start += 1

print(result)
