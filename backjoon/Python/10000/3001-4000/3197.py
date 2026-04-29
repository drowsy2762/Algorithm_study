# https://www.acmicpc.net/problem/3197 : 백조의 호수 (python3)
from collections import deque
from sys import stdin

input = stdin.readline

# 호수의 크기를 입력받음
r, c = map(int, input().split())
lake = [list(input()) for _ in range(r)]
day = 0

# L 은 오리 .은 물 X 는 빙판
# 시간 조절필요
mq1, mq2 = deque(), deque()
sq1, sq2 = deque(), deque()
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[False] * c for _ in range(r)]
visited2 = [[False] * c for _ in range(r)]


# 빙판을 녹이는 과정
def melt():
    while mq1:
        x, y = mq1.popleft()
        lake[x][y] = "."
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= r or 0 > ny or ny >= c or visited[nx][ny]:
                continue
            if lake[nx][ny] == ".":
                mq1.append((nx, ny))
            else:
                mq2.append((nx, ny))
            visited[nx][ny] = True


# 오리가 만나는지 확인
def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= r or 0 > ny or ny >= c or visited2[nx][ny]:
                continue
            if lake[nx][ny] == ".":
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            visited2[nx][ny] = True
    return False


# 호수의 정보를 입력받음
# 오리와 호수의 위치를 저장
# 빙판과 물의 위치를 저장
for i in range(r):
    for j in range(c):
        if lake[i][j] == "L":
            if not sq1:
                sq1.append((i, j))
                visited[i][j] = True
            else:
                ex, ey = i, j
            lake[i][j] = "."
        if lake[i][j] == ".":
            mq1.append((i, j))
            visited[i][j] = True

# 반복을 통해 호수를 녹이고 오리가 만나는지 확인
while True:
    day += 1
    melt()
    if swan():
        break
    mq1, mq2 = mq2, deque()
    sq1, sq2 = sq2, deque()
print(day - 1)
