# https://www.acmicpc.net/problem/1931
# 2026-02-03
from sys import stdin
input = stdin.readline

n = int(input())
meeting_room = []
for _ in range(n):
    meeting_room.append(list(map(int, input().split())))

meeting_room.sort(key=lambda x: (x[1], x[0]))
end = 0
start = 0
cnt = 0

for meeting in meeting_room:
    if meeting[1] >= end and meeting[0] >= end:
        end = meeting[1]
        cnt += 1
print(cnt)