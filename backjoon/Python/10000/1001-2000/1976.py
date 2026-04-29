# https://www.acmicpc.net/problem/1976 : 여행 가자 (Python3)
# 2024-02-20
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
m = int(input())

city = []

for i in range(n):
    city.append(list(map(int, input().split())))
plan = list(map(int, input().split()))


def bfs(s, e):
    q = deque()
    q.append(s)
    visited = [False] * n
    visited[s] = True

    while q:
        here = q.popleft()

        if here == e:
            return True

        for i in range(n):
            if city[here][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)

    return False


answer = True
for i in range(m - 1):
    if plan[i] != plan[i + 1]:
        if not bfs(plan[i] - 1, plan[i + 1] - 1):
            answer = False
            break

if answer:
    print("YES")
else:
    print("NO")
