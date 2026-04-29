# https://www.acmicpc.net/problem/20056
# 2026-02-16
from sys import stdin
input = stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

n, M, k = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

for _ in range(k):
    grid = {}
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % n
        nc = (c + dc[d] * s) % n
        if (nr, nc) not in grid:
            grid[(nr, nc)] = []
        grid[(nr, nc)].append([m, s, d])
    
    new_fireballs = []
    for (r, c), balls in grid.items():
        if len(balls) == 1:
            new_fireballs.append([r, c] + balls[0])
            continue
        sum_m, sum_s, cnt = 0, 0, len(balls)
        odd, even = 0, 0 
        
        for m, s, d in balls:
            sum_m += m
            sum_s += s
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
        
        nm = sum_m // 5
        if nm == 0:
            continue
        ns = sum_s // cnt
        if odd == cnt or even == cnt:
            nd_list = [0, 2, 4, 6]
        else:
            nd_list = [1, 3, 5, 7]
            
        for nd in nd_list:
            new_fireballs.append([r, c, nm, ns, nd])
            
    fireballs = new_fireballs

print(sum(f[2] for f in fireballs))