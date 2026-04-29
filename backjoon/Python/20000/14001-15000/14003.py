# https://www.acmicpc.net/problem/14003
# 2026-04-04
import sys
from bisect import bisect_left

def solution():
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int, input().split()))
    lis = []
    record = []

    for x in seq:
        if not lis or lis[-1] < x:
            lis.append(x)
            record.append((x, len(lis) - 1))
        else:
            idx = bisect_left(lis, x)
            lis[idx] = x
            record.append((x, idx))

    max_length = len(lis)
    print(max_length)

    ans = []
    target = max_length - 1

    for i in range(n - 1, -1, -1):
        if record[i][1] == target:
            ans.append(record[i][0])
            target -= 1

    print(*(ans[::-1]))

if __name__ == "__main__":
    solution()