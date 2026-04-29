# https://www.acmicpc.net/problem/1697 : 숨바꼭질 (python3)
from sys import stdin
from collections import deque

input = stdin.readline


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i <= max and not dist[i]:
                dist[i] = dist[x] + 1
                queue.append(i)


n, k = map(int, input().split())
max = 10**5
dist = [0] * (max + 1) # 가중치

bfs()
