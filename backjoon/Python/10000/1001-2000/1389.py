# 2026-11-27
from collections import deque
import sys

input = sys.stdin.readline


def bfs(start: int, n: int, graph: list[list[int]]) -> int:
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

    return sum(d for d in dist[1:] if d > 0)


def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    min_bacon = float("inf")
    answer = 1

    for person in range(1, n + 1):
        bacon = bfs(person, n, graph)
        if bacon < min_bacon:
            min_bacon = bacon
            answer = person

    print(answer)


if __name__ == "__main__":
    solve()
