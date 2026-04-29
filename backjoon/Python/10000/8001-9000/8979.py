# https://www.acmicpc.net/problem/8979 : 올림픽 (python3)

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

rank = [i for i in range(1, n + 1)]

medal = []
for i in range(n):
    medal.append(list(map(int, input().split())))

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(n):
    if medal[i][0] == k:
        k = i
        break

for i in range(n):
    if medal[i][1:] == medal[k][1:]:
        print(rank[i])
        break
