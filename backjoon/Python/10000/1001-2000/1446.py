# https://www.acmicpc.net/problem/1446 : 지름길 (python3)
# 2023-11-21
import sys

input = sys.stdin.readline

n, d = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
graph = [i for i in range(d + 1)]

for i in range(d + 1):
    # print(graph[i], graph[i - 1] + 1)
    graph[i] = min(graph[i], graph[i - 1] + 1)
    for start, end, le in n_list:
        if i == start and end <= d:
            graph[end] = min(graph[end], graph[i] + le)
print(graph)
print(graph[-1])
