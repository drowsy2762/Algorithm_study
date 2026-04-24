# https://www.acmicpc.net/problem/15681
# 2026-04-24
import sys
sys.setrecursionlimit(200000)

def solution():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    ptr = 0
    N = int(input_data[ptr]); ptr += 1
    R = int(input_data[ptr]); ptr += 1
    Q = int(input_data[ptr]); ptr += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(input_data[ptr]); ptr += 1
        v = int(input_data[ptr]); ptr += 1
        adj[u].append(v)
        adj[v].append(u)
        
    subtree_size = [0] * (N + 1)
    visited = [False] * (N + 1)

    def count_subtree(node):
        visited[node] = True
        subtree_size[node] = 1
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                subtree_size[node] += count_subtree(neighbor)
        
        return subtree_size[node]

    count_subtree(R)

    results = []
    for _ in range(Q):
        u = int(input_data[ptr]); ptr += 1
        results.append(str(subtree_size[u]))
        
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solution()    