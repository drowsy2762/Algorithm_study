# https://www.acmicpc.net/problem/2668 : 숫자고르기 (python3)
# 2024-01-17
from sys import stdin

input = stdin.readline


def dfs(n):
    if visited[n] == False:
        visited[n] = True
        for i in graphs[n]:
            tmp_up.add(n)
            tmp_bottom.add(i)

            if tmp_bottom == tmp_up:
                ans.extend(list(tmp_bottom))
                return
            dfs(i)
    visited[n] = False


n = int(input())
graphs = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    graphs[i].append(int(input()))

ans = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    tmp_up = set()
    tmp_bottom = set()
    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for i in ans:
    print(i)
