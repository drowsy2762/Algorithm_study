# https://www.acmicpc.net/problem/31671 : 특별한 오름 등반(Python3)

from collections import deque  # deque를 사용하기 위해 collections 모듈을 import합니다.

dx = [1, 1]  # x 좌표 이동 방향
dy = [1, -1]  # y 좌표 이동 방향

N, M = map(int, input().split())  # N과 M을 입력받습니다.
graph = [
    [0] * (N + 1) for _ in range(2 * N + 1)
]  # 오름의 모양을 나타내는 2차원 리스트를 초기화합니다.
max_height_stack = []  # max_height의 이전 값을 저장할 스택을 초기화합니다.


for _ in range(M):  # M개의 선생님 위치를 입력받아 그래프에 표시합니다.
    x, y = map(int, input().split())
    graph[x][y] = -1


def bfs():  # 너비 우선 탐색(BFS) 함수를 정의합니다.
    queue = deque([(0, 0)])  # 탐색을 시작할 위치를 큐에 넣습니다.
    graph[0][0] = 1
    max_height = 0  # 최대 높이를 저장할 변수를 초기화합니다.

    while queue:  # 큐가 빌 때까지 반복합니다.
        x, y = queue.popleft()  # 큐에서 위치를 하나 꺼냅니다.

        for i in range(2):  # 두 가지 이동 방향에 대해 반복합니다.
            nx = x + 1
            ny = dy[i] + y  # 다음 y 좌표를 계산합니다.

            # 다음 위치가 오름의 범위를 벗어나면 무시합니다.
            if nx >= N + 1 and ny > 2 * N - nx:
                continue

            # 다음 위치가 오름 내부이고, 아직 방문하지 않았다면
            if 0 <= nx < 2 * N + 1 and 0 <= ny < N + 1 and graph[nx][ny] == 0:
                max_height_stack.append(
                    max_height
                )  # 현재 max_height를 스택에 저장합니다.
                max_height = max(ny, max_height)  # 최대 높이를 업데이트합니다.
                graph[nx][ny] = 1  # 다음 위치를 방문했다고 표시합니다.
                queue.append((nx, ny))  # 다음 위치를 큐에 넣습니다.
            elif (
                0 <= nx < 2 * N + 1 and 0 <= ny < N + 1 and graph[nx][ny] == -1
            ):  # 다음 위치가 -1이라면
                if max_height_stack:  # 스택이 비어있지 않다면
                    max_height = (
                        max_height_stack.pop()
                    )  # max_height를 이전 값으로 롤백합니다.
    return max_height  # 최대 높이를 반환합니다.


max_height = bfs()  # BFS를 수행하고 최대 높이를 구합니다.

# 도착 위치에 도달하지 못했다면 -1을 출력합니다.
if graph[2 * N][0] == 0:
    print(-1)
else:  # 도착 위치에 도달했다면 최대 높이를 출력합니다.
    print(max_height)
