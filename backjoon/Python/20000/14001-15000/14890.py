# https://www.acmicpc.net/problem/14890
# 2026-01-11
from sys import stdin
input = stdin.readline

n, l = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

def chekc_line(line):
    visited = [False] * n
    
    for i in range(n - 1):
        diff = line[i] - line[i + 1]

        if diff == 0:
            continue

        if abs(diff) > 1:
            return False
        
        if diff == -1:
            if i - l + 1 < 0:
                return False
            
            for j in range(i, i - l, -1):
                if line[j] != line[i] or visited[j]:
                    return False
            
            for i in range(i, i - l, -1):
                visited[i] = True

        elif diff == 1:
            if i + l + 1 > n :
                return False
            
            for j in range(i + 1, i + 1 + l):
                if line[j] != line[i + 1] or visited[j]: 
                    return False

            for i in range(i + 1, i + l + 1):
                visited[i] = True
        
    return True
   
for i in range(n):
    if chekc_line(graph[i]):
        cnt += 1

for i in range(n):
    col = []
    for j in range(n):
        col.append(graph[j][i])

    if chekc_line(col):
        cnt += 1

print(cnt)
    