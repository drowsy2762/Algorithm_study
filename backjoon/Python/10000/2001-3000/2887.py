# https://www.acmicpc.net/problem/2887
# 2026-04-23
import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    planets = []
    for i in range(n):
        x, y, z = map(int, input().split())
        planets.append((x, y, z, i))

    edges = []
    for i in range(3):
        planets.sort(key=lambda x:x[i])
        for j in range(n - 1):
            cost = abs(planets[j][i] - planets[j + 1][i])
            edges.append((cost, planets[j][3], planets[j + 1][3]))
        edges.sort()

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            if root_a < root_b:
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b
            return True
        return False

    total_cost = 0
    count = 0
    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            count += 1
            if count == n - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    solution()