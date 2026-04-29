# https://www.acmicpc.net/problem/13549 : 숨바꼭질 3 (python3)
# 2023-12-29
from collections import deque
from sys import stdin

input = stdin.readline


def bfs(n, m):
    queue = deque()
    queue.append(n)
    while queue:
        location = queue.popleft()
        if location == m:
            print(visited[location])
            break
        if 0 <= location * 2 < 100001 and visited[location * 2] == -1:
            visited[location * 2] = visited[location]
            queue.appendleft(location * 2)
        if 0 <= location - 1 < 100001 and visited[location - 1] == -1:
            visited[location - 1] = visited[location] + 1
            queue.append(location - 1)
        if 0 <= location + 1 < 100001 and visited[location + 1] == -1:
            visited[location + 1] = visited[location] + 1
            queue.append(location + 1)


n, m = map(int, input().split())
visited = [-1 for _ in range(100001)]
visited[n] = 0

bfs(n, m)
