# https://www.acmicpc.net/problem/20006 : 랭킹전 대기열 (python3)
# 2023-11-07
from sys import stdin

input = stdin.readline

p, m = map(int, input().split())
rooms = []

for p in range(p):
    l, n = input().split()
    if not rooms:
        rooms.append([[int(l), n]])
        continue

    enter = False
    for room in rooms:
        if len(room) < m and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l), n])
            enter = True
            break
    if not enter:
        rooms.append([[int(l), n]])

for room in rooms:
    room.sort(key=lambda x: x[1])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for lv, name in room:
        print(lv, name)
