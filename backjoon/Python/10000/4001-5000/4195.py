# https://www.acmicpc.net/problem/4195
# 2026-04-17
import sys

def solution():
    input = sys.stdin.readline

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a
            number[a] += number[b]
        print(number[a])

    for _ in range(int(input())):
        num = int(input())
        parent, number = {}, {}
        for i in range(num):
            a, b = input().split()
            if a not in parent:
                parent[a] = a
                number[a] = 1
            if b not in parent:
                parent[b] =b
                number[b] = 1
            union(a, b)

if __name__ == "__main__":
    solution()