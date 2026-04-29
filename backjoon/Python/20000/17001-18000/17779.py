# https://www.acmicpc.net/problem/17779
# 2026-02-08
import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
total_people = sum(map(sum, grid))

ans = 1e9

def solve(x, y, d1, d2):
    temp = [[0] * N for _ in range(N)]
    people = [0] * 5

    for i in range(d1 + 1):
        temp[x + i][y - i] = 5
        temp[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        temp[x + i][y + i] = 5
        temp[x + d1 + i][y - d1 + i] = 5

    for r in range(x + 1, x + d1 + d2):
        start_c = -1
        end_c = -1
        for c in range(N):
            if temp[r][c] == 5:
                start_c = c
                break
        for c in range(N - 1, -1, -1):
            if temp[r][c] == 5:
                end_c = c
                break
        if start_c != -1 and end_c != -1:
            for c in range(start_c + 1, end_c):
                temp[r][c] = 5
    # 1번 선거구
    for r in range(x + d1):
        for c in range(y + 1):
            if temp[r][c] == 5:
                break 
            people[0] += grid[r][c]
            
    # 2번 선거구 
    for r in range(x + d2 + 1):
        for c in range(N - 1, y, -1):
            if temp[r][c] == 5:
                break
            people[1] += grid[r][c]
            
    # 3번 선거구 
    for r in range(x + d1, N):
        for c in range(y - d1 + d2):
            if temp[r][c] == 5:
                break
            people[2] += grid[r][c]
            
    # 4번 선거구 
    for r in range(x + d2 + 1, N):
        for c in range(N - 1, y - d1 + d2 - 1, -1):
            if temp[r][c] == 5:
                break
            people[3] += grid[r][c]
    
    # 5번 선거구 
    people[4] = total_people - sum(people)
    
    return max(people) - min(people)

for x in range(N - 2):
    for y in range(1, N - 1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 < N and 0 <= y - d1 and y + d2 < N:
                    ans = min(ans, solve(x, y, d1, d2))

print(ans)