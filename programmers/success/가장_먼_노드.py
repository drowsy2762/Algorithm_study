# 2026-05-15

from collections import deque


def solution(n, edge):
    node = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    for i, j in edge:
        node[i].append(j)
        node[j].append(i)

    def bfs(start):
        queue = deque([start])
        visited[start] = 0
        while queue:
            curr = queue.popleft()
            for next_node in node[curr]:
                if visited[next_node] == -1:
                    visited[next_node] = visited[curr] + 1
                    queue.append(next_node)

    bfs(1)

    return visited.count(max(visited))
