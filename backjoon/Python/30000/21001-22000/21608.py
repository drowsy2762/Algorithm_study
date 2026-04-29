# https://www.acmicpc.net/problem/21608
# 2026-02-19 
from sys import stdin
input = stdin.readline

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
total_students = n ** 2 
students = [list(map(int, input().split())) for _ in range(total_students)]
students_dict = {}
result = 0

for line in students:
    student_num = line[0]
    friends = line[1:]
    students_dict[student_num] = friends
    candidates = []
    for r in range(n):
        for c in range(n):
            if graph[r][c] != 0: 
                continue 
            
            like_cnt = 0
            empty_cnt = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if graph[nr][nc] in friends:
                        like_cnt += 1
                    elif graph[nr][nc] == 0:
                        empty_cnt += 1
            candidates.append((-like_cnt, -empty_cnt, r, c))
    candidates.sort()
    
    best_seat = candidates[0]
    best_r, best_c = best_seat[2], best_seat[3]
    graph[best_r][best_c] = student_num

for r in range(n):
    for c in range(n):
        student = graph[r][c]
        friends = students_dict[student]
        
        cnt = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if graph[nr][nc] in friends:
                    cnt += 1
        if cnt > 0:
            result += 10 ** (cnt - 1)

print(result)