# https://www.acmicpc.net/problem/4386
# 2026-04-20
import sys
import math

def solution():
    input = sys.stdin.readline

    n = int(input())
    stars = [list(map(float, input().split())) for _ in range(n)]
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(u, v):
        if u != v:
            if u < v:
                parent[v] = u
            else:
                parent[u] = v
            return True
        return False

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
                dist = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
                edges.append((dist, i, j))
    edges.sort()
    cnt = 0
    res = 0

    for dist, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        if union(root_u, root_v):
            res += dist
            cnt += 1
            if cnt == n - 1:
                break
    
    print(f"{res:.2f}")
    
if __name__ == "__main__":
    solution()