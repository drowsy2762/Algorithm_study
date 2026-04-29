# https://www.acmicpc.net/problem/14002
# 2026-04-02
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    seq = list(map(int, input().split()))
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    print(max_length)

    ans = []
    target = max_length

    for i in range(n - 1, -1, -1):
        if dp[i] == target:
            ans.append(seq[i])
            target -= 1

    print(*(ans[::-1]))

if __name__ == "__main__":
    solution()