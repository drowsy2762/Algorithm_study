# https://www.acmicpc.net/problem/15591
# 2026-02-28
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA != rootB:
        parent[rootB] = rootA          
        size[rootA] += size[rootB]     

N, Q = map(int, input().split())

edges = []
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    edges.append((r, p, q)) 

queries = []
for i in range(Q):
    k, v = map(int, input().split())
    queries.append((k, v, i))

edges.sort(reverse=True)
queries.sort(reverse=True)

parent = [i for i in range(N + 1)]
size = [1] * (N + 1)
ans = [0] * Q  

edge_idx = 0

for k, v, original_idx in queries:
    while edge_idx < N - 1 and edges[edge_idx][0] >= k:
        weight, p, q = edges[edge_idx]
        union(p, q)
        edge_idx += 1
        
    root_v = find(v)
    ans[original_idx] = size[root_v] - 1

for a in ans:
    print(a)