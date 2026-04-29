# https://www.acmicpc.net/problem/20125 : 쿠키의 신체 측정(python3)
# 2023-09-27
from sys import stdin

input = stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

cnt = 0
r_arm = 0
l_arm = 0
x_hurt = 0
y_hurt = 0
waist = 0
r_reg = 0
l_reg = 0
for i in range(n):
    rcnt = 0
    wcnt = 0
    for j in range(n):
        # 다리 길이 체크
        if graph[i][j] == "*" and cnt == 3 and rcnt == 0:
            for k in range(0, check_hurt - 1):
                if graph[i][k] == "*" and rcnt == 0:
                    l_reg += 1
            rcnt += 1
            for k in range(check_hurt, n):
                if graph[i][k] == "*" and rcnt == 1:
                    r_reg += 1
        # 허리 길이체크
        if graph[i][j] == "*" and cnt == 2 and wcnt == 0:
            wcnt += 1
            dist = 0
            for k in range(n):
                if graph[i][k] == "*":
                    dist += 1
            if dist == 2:
                cnt += 1
                continue
            else:
                waist += 1
        # 팔 길이 체크
        if graph[i][j] == "*" and cnt == 1:
            for k in range(0, check_hurt - 1):
                if graph[i][k] == "*":
                    l_arm += 1
            for k in range(check_hurt, n):
                if graph[i][k] == "*":
                    r_arm += 1
            cnt += 1
        # 심장 위치체크
        if graph[i][j] == "*" and cnt == 0:
            cnt += 1
            print(i + 2, j + 1)
            check_hurt = j + 1

print(l_arm, r_arm, waist - 1, l_reg, r_reg)
