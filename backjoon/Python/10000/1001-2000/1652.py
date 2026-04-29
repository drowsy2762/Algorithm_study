# https://www.acmicpc.net/problem/1652 : 누울 자리를 찾아라 (python3)
# cleartime : 20/06/23 12:15
# inputtime 최적화
from sys import stdin


# 열 확인
def checkRow():
    layDown = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if room[i][j] == ".":
                cnt += 1
            else:
                if cnt > 1:
                    layDown += 1
                cnt = 0
        if cnt > 1:
            layDown += 1
    return layDown


# 행 확인
def checkCol():
    layDown = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if room[j][i] == ".":
                cnt += 1
            else:
                if cnt > 1:
                    layDown += 1
                cnt = 0
        if cnt > 1:
            layDown += 1
    return layDown


input = stdin.readline
# 방의 크기를 입력받음
n = int(input())
room = [input().rstrip() for _ in range(n)]
print(checkRow(), checkCol())
