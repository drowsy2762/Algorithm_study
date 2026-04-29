# https://www.acmicpc.net/problem/16928 : 뱀과 사다리 게임 (python3)
# 2024-03-28
from sys import stdin
from collections import deque

input = stdin.readline


# bfs 함수는 사다리와 뱀의 정보를 받아, 시작점에서 끝점까지 도달하는 데 필요한 최소 횟수를 출력합니다.
def bfs(ladder, snake):
    visited = [
        False for _ in range(101)
    ]  # 각 위치를 방문했는지 여부를 저장하는 배열입니다.
    graph = [
        0 for _ in range(101)
    ]  # 각 위치에 도달하는 데 필요한 최소 횟수를 저장하는 배열입니다.
    q = deque([1])  # BFS를 위한 큐입니다. 시작점은 1입니다.
    while q:  # 큐가 빌 때까지 반복합니다.
        t = q.popleft()  # 큐에서 가장 먼저 들어온 위치를 꺼냅니다.

        if t == 100:  # 만약 끝점에 도달했다면
            print(graph[t])  # 해당 위치에 도달하는 데 필요한 최소 횟수를 출력하고
            break  # 반복을 종료합니다.
        for dice in range(1, 7):  # 주사위의 모든 가능한 눈금에 대해
            x = t + dice  # 주사위를 던져 이동한 위치를 계산합니다.
            if (
                x <= 100 and not visited[x]
            ):  # 만약 이동한 위치가 보드 내에 있고 아직 방문하지 않았다면
                if x in ladder.keys():  # 만약 이동한 위치에 사다리의 시작점이 있다면
                    x = ladder[x]  # 사다리의 끝점으로 이동합니다.
                if x in snake.keys():  # 만약 이동한 위치에 뱀의 머리가 있다면
                    x = snake[x]  # 뱀의 꼬리로 이동합니다.
                if not visited[x]:  # 만약 이동한 위치를 아직 방문하지 않았다면
                    visited[x] = True  # 해당 위치를 방문했다고 표시하고
                    graph[x] = (
                        graph[t] + 1
                    )  # 해당 위치에 도달하는 데 필요한 최소 횟수를 갱신하고
                    q.append(x)  # 큐에 해당 위치를 추가합니다.


# solution 함수는 문제의 입력을 받아 bfs 함수를 호출합니다.
def solution():
    input = stdin.readline

    n, m = map(int, input().split())  # 사다리의 수와 뱀의 수를 입력받습니다.
    ladder = dict()  # 사다리의 정보를 저장할 딕셔너리입니다.
    snake = dict()  # 뱀의 정보를 저장할 딕셔너리입니다.
    for _ in range(n):  # 각 사다리에 대해
        i, j = map(int, (input().split()))  # 사다리의 시작점과 끝점을 입력받아
        ladder[i] = j  # 딕셔너리에 저장합니다.
    for _ in range(m):  # 각 뱀에 대해
        i, j = map(int, (input().split()))  # 뱀의 머리와 꼬리를 입력받아
        snake[i] = j  # 딕셔너리에 저장합니다.

    bfs(
        ladder, snake
    )  # bfs 함수를 호출하여 시작점에서 끝점까지 도달하는 데 필요한 최소 횟수를 출력합니다.


solution()  # solution 함수를 호출하여 프로그램을 시작합니다.
