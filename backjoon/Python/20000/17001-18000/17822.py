# https://www.acmicpc.net/problem/17822
# 2026-02-10
import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())
disk = [deque(map(int, input().split())) for _ in range(n)]
spins = [list(map(int, input().split())) for _ in range(t)]

def turn(x, d, k):
    for i in range(n):
        if (i + 1) % x == 0:
            if d == 0: 
                disk[i].rotate(k)
            else: 
                disk[i].rotate(-k)

def check_and_remove():
    remove_set = set() 
    
    for i in range(n):
        for j in range(m):
            current = disk[i][j]
            if current == 0:
                continue

            if disk[i][(j + 1) % m] == current:
                remove_set.add((i, j))
                remove_set.add((i, (j + 1) % m))
            
            if i + 1 < n and disk[i + 1][j] == current:
                remove_set.add((i, j))
                remove_set.add((i + 1, j))
    
    if remove_set:
        for x, y in remove_set:
            disk[x][y] = 0
        return True 
    else:
        return False 

def adjust_average():
    total_sum = 0
    count = 0
    
    for i in range(n):
        for j in range(m):
            if disk[i][j] != 0:
                total_sum += disk[i][j]
                count += 1
    
    if count == 0: 
        return

    avg = total_sum / count
    
    for i in range(n):
        for j in range(m):
            if disk[i][j] != 0:
                if disk[i][j] > avg:
                    disk[i][j] -= 1
                elif disk[i][j] < avg:
                    disk[i][j] += 1

for x, d, k in spins:
    turn(x, d, k)
    if not check_and_remove():
        adjust_average()

ans = 0
for i in range(n):
    ans += sum(disk[i])
print(ans)