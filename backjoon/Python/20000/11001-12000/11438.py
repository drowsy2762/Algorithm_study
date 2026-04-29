# https://www.acmicpc.net/problem/11438 : LCA 2 (python3)
# 2026-04-14
import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    log = 18 
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    parent = [[0] * log for _ in range(n + 1)]

    def bfs(root):
        q = deque([root])
        visited[root] = True
        depth[root] = 0
        while q:
            curr = q.popleft()
            for next_node in graph[curr]:
                if not visited[next_node]:
                    visited[next_node] = True
                    depth[next_node] = depth[curr] + 1
                    parent[next_node][0] = curr
                    q.append(next_node)
    
    def set_parent():
        for k in range(1, log):
            for i in range(1, n + 1):
                parent[i][k] = parent[parent[i][k - 1]][k - 1]

    bfs(1)
    set_parent()

    def lca(a, b):
        if depth[a] > depth[b]:
            a, b = b, a

        for i in range(log - 1, -1, -1):
            if depth[b] - depth[a] >= (1 << i):
                b = parent[b][i]

        if a == b:
            return a
        
        for i in range(log - 1, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]

        return parent[a][0]
    
    m = int(input())
    results = []
    for _ in range(m):
        u, v = map(int, input().split())
        results.append(str(lca(u, v)))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solution()