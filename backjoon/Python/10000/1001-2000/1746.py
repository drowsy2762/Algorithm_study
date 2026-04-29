# https://www.acmicpc.net/problem/1764
# 2026-02-02
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = set()
b = set()
for i in range(n):
    a.add(input().rstrip())
for i in range(m):
    b.add(input().rstrip())

results = sorted(list(a & b))
print(len(results))
for result in results:
    print(result)