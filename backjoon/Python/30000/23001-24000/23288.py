# https://www.acmicpc.net/problem/23288
# 2026-02-23
import sys
from collections import deque
input = sys.stdin.readline

dr, dc= [-1, 0, 1, 0], [0, -1, 0, 1]

n, m, k = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 4, 3, 5, 6]
dice_c, dice_r = 0, 0
direction = 3
ans = 0

# 0 north, 1 west, 2 south, 3 east
def turn(direction):
    global dice
    if direction == 0:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 2:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif direction == 3:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

def get_score(r, c, target):
    q = deque()
    q.append((r, c))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[r][c] = True
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < n and 0 <= nc < m) and visited[nr][nc] == False:
                if maps[nr][nc] == target:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    cnt += 1
    return cnt

# dice[5] -> 밑면
for _ in range(k):
    dice_r += dr[direction]
    dice_c += dc[direction]
    if 0 <= dice_r < n and 0 <= dice_c < m:
        turn(direction)
    else:
        direction = (direction + 2) % 4
        dice_r += dr[direction] * 2
        dice_c += dc[direction] * 2
        turn(direction)
    
    if dice[5] > maps[dice_r][dice_c]:  
        direction = (direction - 1) % 4
    elif dice[5] < maps[dice_r][dice_c]:
        direction = (direction + 1) % 4
    ans += (maps[dice_r][dice_c] * get_score(dice_r, dice_c, maps[dice_r][dice_c]))

print(ans)