# https://www.acmicpc.net/problem/19237
# 2026-02-14
from sys import stdin
from collections import deque
input = stdin.readline

# 문제 조건: 위, 아래, 왼쪽, 오른쪽
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# n -> 격자의 크기 / m -> 상어가 들어 있는 칸 개수 / k -> 냄새가 사라지는 이동 횟수
# 한칸에 상어 여러마리 시 가장 우선순위 높은 상어 제외 추방
n, m, k = map(int, input().split())
# 0은 빈칸 / 숫자는 상어의 우선순위번호
ocean = [list(map(int, input().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# 1 -> 위, 2 -> 아래, 3 -> 왼쪽, 4 -> 오른쪽
sharks = [[0, 0, 0] for _ in range(m)]
dead_shark = [False for _ in range(m)]
for i in range(n):
    for j in range(n):
        if ocean[i][j] != 0:
            shark_num = ocean[i][j]
            sharks[shark_num - 1][0] = i
            sharks[shark_num - 1][1] = j
            
            smell[i][j] = [shark_num, k]

shark_dir = list(map(int, input().split()))

for i in range(m):
    sharks[i][2] = shark_dir[i] - 1 

shark_dir_priority = [[list(map(lambda x: int(x) - 1, input().split())) for _ in range(4)] for _ in range(m)]

# 모든 냄새 감소
def smell_delete():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0

def smell_add():
    for i in range(m):
        if dead_shark[i]: continue
        x, y = sharks[i][0], sharks[i][1]
        smell[x][y] = [i + 1, k]

# 상어는 1초에 한칸 이동 (모든 상어 이동)
def shark_move():
    new_ocean = [[-1] * n for _ in range(n)]

    for shark_id in range(m):
        if dead_shark[shark_id]: continue

        x, y, d = sharks[shark_id]

        # 좌표 우선순위에 따라 nx, ny, nd를 구하는 로직
        # 우선순위에 따라 갈 수 있는지 확인 후 불가능하면 다음 우선순위 확인
        target_x, target_y, target_d = -1, -1, -1
        my_smell_x, my_smell_y, my_smell_d = -1, -1, -1
        
        for i in shark_dir_priority[shark_id][d]:
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if smell[nx][ny][0] == 0:
                    target_x, target_y, target_d = nx, ny ,i
                    break
                elif smell[nx][ny][0] == shark_id + 1:
                    if my_smell_x == -1:
                        my_smell_x, my_smell_y, my_smell_d = nx, ny, i
        
        if target_x == -1:
            target_x, target_y, target_d = my_smell_x, my_smell_y, my_smell_d

        if new_ocean[target_x][target_y] == -1:
            new_ocean[target_x][target_y] = shark_id + 1
            sharks[shark_id] = [target_x, target_y, target_d]
        else:
            dead_shark[shark_id] = True
    
    return new_ocean

def check():
    for i in range(1, m):
        if not dead_shark[i]:
            return False
    return True

def solution():
    global ocean
    time = 0
    while time < 1000:
        time += 1

        ocean = shark_move()
        smell_delete()
        smell_add()

        if check():
            return time
        
    return -1 

print(solution())