# https://www.acmicpc.net/problem/10775 : 공항(python3)
# 2026-04-18
import sys

def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    g_count = int(input_data[0])
    p_count = int(input_data[1])
    
    parent = list(range(g_count + 1))

    def find_parent(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        
        while parent[x] != root:
            next_node = parent[x]
            parent[x] = root
            x = next_node
            
        return root

    cnt = 0
    for i in range(2, p_count + 2):
        gi = int(input_data[i])
        root = find_parent(gi)

        if root == 0:
            break
        
        parent[root] = find_parent(root - 1)
        cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    solution()