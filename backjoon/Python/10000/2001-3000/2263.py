# https://www.acmicpc.net/problem/2263
# 2026-04-12
import sys
sys.setrecursionlimit(10**6)

def solution():
    input = sys.stdin.readline

    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[inorder[i]] = i
        
    def get_preorder(in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return
        
        root = postorder[post_end]
        print(root, end=' ')
        
        root_idx = pos[root]
        left_size = root_idx - in_start
        get_preorder(in_start, root_idx - 1, post_start, post_start + left_size - 1)
        get_preorder(root_idx + 1, in_end, post_start + left_size, post_end - 1)

    get_preorder(0, n-1, 0, n-1)

if __name__ == "__main__":
    solution()