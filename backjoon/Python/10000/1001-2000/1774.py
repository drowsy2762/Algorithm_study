# https://www.acmicpc.net/problem/1774
# 2026-04-22
import sys
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    coords = []
    for _ in range(n):
        coords.append(list(map(int, input().split())))
    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if root_u < root_v:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
            return True
        return False

    for _ in range(m):
        u, v = map(int, input().split())
        union(u, v)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = coords[i][0] - coords[j][0]
            dy = coords[i][1] - coords[j][1]
            dist = math.sqrt(dx**2 + dy**2)
            edges.append((dist, i + 1, j + 1))

    edges.sort()

    res = 0
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            res += dist
    
    print(f"{res:.2f}")

if __name__ == "__main__":
    solution()