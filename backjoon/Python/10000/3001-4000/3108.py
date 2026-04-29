# https://www.acmicpc.net/problem/3108
# 2026-03-30
import sys
input = sys.stdin.readline

def solution():
    def find(n):
        temp = n
        while n != group[n]:
            n = group[n]
        group[temp] = n
        return n

    def union(n1, n2):
        n1 = find(n1)
        n2 = find(n2)
        if n1 > n2:
            n1, n2 = n2, n1
        group[n2] = n1

    n = int(input())
    group = [i for i in range(n + 1)]
    rect = [(0, 0, 0, 0)]
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rect.append((x1, y1, x2, y2))
    for i in range(n):
        x1, y1, x2, y2 = rect[i]
        for j in range(i + 1, n + 1):
            x3, y3, x4, y4 = rect[j]
            if x3 > x1 and x2 > x4 and y3 > y1 and y2 > y4:
                continue
            if x1 > x3 and x4 > x2 and y1 > y3 and y4 > y2:
                continue
            if x3 > x2 or x1 > x4 or y3 > y2 or y1 > y4:
                continue
            union(i, j)
    for i in range(n + 1):
        find(i)
    print(len(set(group)) - 1)

if __name__ == "__main__":
    solution()