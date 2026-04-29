# https://www.acmicpc.net/problem/9177
# 2026-04-06
import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    
    for k in range(1, n + 1):
        a, b, c = input().split()
        len_a, len_b = len(a), len(b)
        dp = [[False] * (len_b + 1) for _ in range(len_a + 1)]
        dp[0][0] = True
        
        for i in range(1, len_a + 1):
            if dp[i - 1][0] and a[i - 1] == c[i - 1]:
                dp[i][0] = True
                
        for j in range(1, len_b + 1):
            if dp[0][j - 1] and b[j - 1] == c[j - 1]:
                dp[0][j] = True
                
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if dp[i - 1][j] and a[i - 1] == c[i + j - 1]:
                    dp[i][j] = True
                elif dp[i][j - 1] and b[j - 1] == c[i + j - 1]:
                    dp[i][j] = True
                    
        if dp[len_a][len_b]:
            print(f"Data set {k}: yes")
        else:
            print(f"Data set {k}: no")

if __name__ == "__main__":
    solution()