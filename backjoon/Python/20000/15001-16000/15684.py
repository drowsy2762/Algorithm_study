# https://www.acmicpc.net/problem/15684
# 2026-01-17
from sys import stdin
from copy import deepcopy
input = stdin.readline

flag = False
ans = -1
n, m, h = map(int,input().split())
graph = [[0] *(n+1) for _ in range(h+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1

def check():
    for start in range(1, n + 1):
        k = start
        for i in range(1, h + 1):
            if graph[i][k] == 1:
                k += 1
            elif graph[i][k - 1] == 1:
                k -= 1
        if k != start:
            return False
    return True

def dfs(cnt, x, y, target):
    global flag
    if flag == True:
        return
    
    if cnt == target:
        if check() == True:
            flag = True
        return
    
    for i in range(x, h+1):
        k = y if i == x else 1
        for j in range(k, n):
            if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i][j+1] == 0:
                graph[i][j] = 1
                dfs(cnt + 1, i, j+2, target)
                graph[i][j] = 0 

for i in range(4):
    dfs(0, 1, 1, i)
    if flag == True:
        ans = i
        break
print(ans)