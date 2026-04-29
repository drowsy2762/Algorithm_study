# https://www.acmicpc.net/problem/2606 : 바이러스 (python3)
from sys import stdin

input = stdin.readline

# n = int(input())
# t = int(input())
# cnt = 0

# graph = [[] for _ in range(n + 1)]
# visited = [False for _ in range(n + 1)]


# def dfs(node):
#     if visited[node] == False:
#         visited[node] = True
#         global cnt
#         cnt += 1
#         for i in graph[node]:
#             if visited[i] == False:
#                 dfs(i)


# for _ in range(t):
#     i, j = map(int, input().split())
#     graph[i].append(j)
#     graph[j].append(i)


# dfs(1)
# print(cnt - 1)

from collections import deque

n = int(input())
line = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(line):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)


def bfs(start_node, grahp):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        curr_node = queue.popleft()

        for next_node in grahp[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

    return len(visited) - 1


print(bfs(1, graph))
