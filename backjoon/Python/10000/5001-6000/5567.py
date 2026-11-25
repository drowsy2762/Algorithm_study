# 2026-11-25
from collections import deque
import sys

input = sys.stdin.readline


def solve():
    n = int(input().strip())
    m = int(input().strip())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])

    while queue:
        cur = queue.popleft()
        if dist[cur] == 2:
            continue

        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

    invite_count = sum(1 for d in dist[2:] if 1 <= d <= 2)
    print(invite_count)


if __name__ == "__main__":
    solve()
