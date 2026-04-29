# https://www.acmicpc.net/problem/1019
# 2026-04-07
import sys

def solution():
    input = sys.stdin.readline

    n = int(input())
    cnt = [0] * 10
    A = 1
    B = n
    point = 1
    
    def count(num, point):
        while num > 0:
            cnt[num % 10] += point
            num //= 10

    while A <= B:
        while A % 10 != 0 and A <= B:
            count(A, point)
            A += 1

        if A > B:
            break
        
        while B % 10 != 9 and A <= B:
            count(B, point)
            B -= 1

        blocks = (B // 10 - A // 10 + 1)

        for i in range(10):
            cnt[i] += blocks * point

        A //= 10
        B //= 10
        point *= 10

    print(*(cnt))

if __name__ == "__main__":
    solution()