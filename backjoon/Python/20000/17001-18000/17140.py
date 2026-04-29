# http://acmicpc.net/problem/17140
# 2026-01-25
from sys import stdin
input = stdin.readline

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
graph = [list(map(int, input().split())) for _ in range(3)]

# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행, 행의 개수 ≥ 열의 개수인 경우에 적용
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행, 행의 개수 < 열의 개수인 경우에 적용

def sort(matrix):
    sorted_matrix = []
    max_len = 0
    for i in range(len(matrix)):
        dic = {}
        for num in matrix[i]:
            if num == 0:
                continue

            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        sorted_pairs = sorted(dic.items(), key=lambda x: (x[1], x[0]))

        new_row = []
        for num, count in sorted_pairs:
            new_row.append(num)
            new_row.append(count)
        new_row = new_row[:100]
        sorted_matrix.append(new_row)
    for row in sorted_matrix:
        if len(row) > max_len:
            max_len = len(row)
            
    if max_len > 100:
        max_len = 100

    for row in sorted_matrix:
        if len(row) < max_len:
            row.extend([0] * (max_len - len(row)))
    
    return sorted_matrix


time = 0
while True:
    if time > 100:
        print(-1)
        break

    if r < len(graph) and c < len(graph[0]):
        if graph[r][c] == k:
            print(time)
            break
    time += 1
    
    if len(graph) >= len(graph[0]):
        # R연산
        graph = sort(graph)
    else:
        # C 연산
        graph = list(map(list, zip(*graph)))
        graph = sort(graph)
        graph = list(map(list, zip(*graph)))