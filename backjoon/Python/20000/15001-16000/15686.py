# https://www.acmicpc.net/problem/15686
# 2026-01-19
from sys import stdin
import itertools
input = stdin.readline
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
 
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
min_city_chicken_dist = 1e9
chicken, house = [], [] #치킨집
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i, j])
        elif graph[i][j] == 1:
            house.append([i, j])

for candidates in itertools.combinations(chicken, m):
    city_dist = 0

    for hr, hc in house:
        dist = 1e9
        for cr, cc in candidates:
            dist = min(dist, abs(hr-cr) + abs(hc-cc))
        city_dist += dist

        if city_dist >= min_city_chicken_dist:
            break

    min_city_chicken_dist = min(min_city_chicken_dist, city_dist)

print(min_city_chicken_dist)