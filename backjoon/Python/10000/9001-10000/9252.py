# https://www.acmicpc.net/problem/9252
# 2026-04-05
import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

def solution():
    a = input().rstrip()
    b = input().rstrip()
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    max_length = dp[n][m]
    print(max_length)

    if max_length == 0:
        return
    
    ans = []
    i, j = n, m
    
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            ans.append(a[i - 1])
            i -= 1
            j -= 1
            
    print("".join(ans[::-1]))

if __name__ == "__main__":
    solution()