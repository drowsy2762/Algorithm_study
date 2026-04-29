# https://www.acmicpc.net/problem/9017 : 크로스 컨트리 (python3)
# 2023-10-02
from sys import stdin
from collections import deque

input = stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    team = list(map(int, input().strip().split()))

    manage = {}
    for j in range(n):
        if team[j] not in manage:
            manage[team[j]] = [1, [], 0]
        else:
            manage[team[j]][0] += 1

    contain = set(k for k, v in manage.items() if v[0] < 6)

    grade = 1
    for j in range(n):
        if team[j] not in contain:
            manage[team[j]][1].append(grade)
            if len(manage[team[j]][1]) <= 4:
                manage[team[j]][2] += grade
            grade += 1

    answer = []
    for k, v in manage.items():
        if len(v[1]) != 0 and v[2] != 0:
            answer.append([k, v[1][4], v[2]])

    a = sorted(answer, key=lambda x: (x[2], x[1]))
    print(a[0][0])
