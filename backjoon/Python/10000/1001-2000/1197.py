# https://www.acmicpc.net/problem/1197
# 2026-04-19
import sys
sys.setrecursionlimit(10**6)

def solution():
    input = sys.stdin.read().split()
    if not input: return
    
    v = int(input[0])
    e = int(input[1])
    
    parent = list(range(v + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(root_x, root_y):
        if root_x != root_y:
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
            return True
        return False

    edges = []
    curr = 2
    for _ in range(e):
        u = int(input[curr])
        v_node = int(input[curr+1])
        w = int(input[curr+2])
        edges.append((u, v_node, w))
        curr += 3
        
    edges.sort(key=lambda x: x[2])
    res = 0
    cnt = 0
    
    for u, v_node, w in edges:
        root_u = find(u)
        root_v = find(v_node)
        if union(root_u, root_v):
            res += w
            cnt += 1
            if cnt == v - 1:
                break
    print(res)

if __name__ == "__main__":
    solution()