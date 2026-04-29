# https://www.acmicpc.net/problem/16235
# 2026-01-21
from sys import stdin
from collections import deque

input = stdin.readline
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
land = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for i in range(n):
    for j in range(n):
        if trees[i][j]:
            trees[i][j] = deque(sorted(trees[i][j]))

for _ in range(k):
    for r in range(n):
        for c in range(n):
            if trees[r][c]: # 나무가 존재시
                len_t = len(trees[r][c])
                new_trees = deque()
                dead_nutrient = 0                 
                for _ in range(len_t):
                    age = trees[r][c].popleft()
                    if land[r][c] >= age: # 양분 먹기 
                        land[r][c] -= age
                        new_trees.append(age + 1)
                    else: 
                        dead_nutrient += age // 2
                        while trees[r][c]:
                             dead_nutrient += trees[r][c].popleft() // 2
                        break # 이 칸의 모든 나무 처리 끝
                trees[r][c] = new_trees
                # 여름
                land[r][c] += dead_nutrient


    # 가을
    for r in range(n):
        for c in range(n):
            for age in trees[r][c]:
                if age % 5 == 0:
                    for i in range(8):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n and 0 <= nc < n:
                            trees[nr][nc].appendleft(1)
    
    # 겨울
    for r in range(n):
        for c in range(n):
            land[r][c] += A[r][c]

ans = 0
for r in range(n):
    for c in range(n):
        ans += len(trees[r][c])

print(ans)