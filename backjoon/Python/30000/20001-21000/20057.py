# https://www.acmicpc.net/problem/20057
# 2026-02-17
from sys import stdin
input = stdin.readline

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

n = int(input())
sands = [list(map(int, input().split())) for _ in range(n)]

x, y = n // 2, n // 2
result = 0

left = [
    [-2, 0, 0.02], [2, 0, 0.02],   # 2% (위, 아래)
    [-1, 1, 0.01], [1, 1, 0.01],   # 1% (뒤쪽 대각선)
    [-1, 0, 0.07], [1, 0, 0.07],   # 7% (위, 아래)
    [-1, -1, 0.1], [1, -1, 0.1],   # 10% (앞쪽 대각선)
    [0, -2, 0.05],                 # 5% (앞쪽 2칸)
    [0, -1, 0]                     # alpha (앞쪽 1칸) 
]

right = [[-x, -y, z] for x, y, z in left]
down = [[-y, x, z] for x, y, z in left]  
up = [[y, -x, z] for x, y, z in left]     

rates = {0: left, 1: down, 2: right, 3: up}

def move_tornado(dist, direction):
    global x, y, result  
    
    for _ in range(dist):
        x += dx[direction]
        y += dy[direction]
        
        if y < 0: 
            break
            
        total_sand = sands[x][y] 
        sands[x][y] = 0 
        
        spread_total = 0
        
        for rx, ry, r in rates[direction]:
            nx = x + rx
            ny = y + ry
            
            # alpha인 경우 남은 모래 다 주기
            if r == 0:
                sand = total_sand - spread_total
            else:
                sand = int(total_sand * r)
                spread_total += sand
            
            if 0 <= nx < n and 0 <= ny < n:
                sands[nx][ny] += sand
            else:
                result += sand

for length in range(1, n):
    for i in range(2):
        direction = (length % 2 == 0) * 2 + i 
        move_tornado(length, direction)

move_tornado(n - 1, 0)

print(result)