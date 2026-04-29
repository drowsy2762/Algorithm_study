# https://www.acmicpc.net/problem/1086
# 2026-03-28
import sys
import math
input = sys.stdin.readline

def solve():
    N = int(input())
    S_str = [input().rstrip() for _ in range(N)]
    K = int(input())
    S_mod = [int(s) % K for s in S_str]
    power = [pow(10, len(s), K) for s in S_str]
    remain = [[(j * power[i] + S_mod[i]) % K for j in range(K)] for i in range(N)]
    dp = [[0] * K for _ in range(1 << N)]
    dp[0][0] = 1
    
    for mask in range(1 << N):
        for j in range(K):
            if dp[mask][j] == 0:
                continue
            
            for i in range(N):
                if mask & (1 << i):
                    continue
                dp[mask | (1 << i)][remain[i][j]] += dp[mask][j]

    correct = dp[(1 << N) - 1][0]
    total = math.factorial(N) 
    
    if correct == 0:
        print("0/1")
    else:
        m = math.gcd(correct, total)
        print(f"{correct // m}/{total // m}")

if __name__ == "__main__":
    solve()