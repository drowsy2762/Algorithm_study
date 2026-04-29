# https://www.acmicpc.net/problem/11725 : 트리의 부모 찾기 (python3)
# 2024-04-08

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)  # 재귀 호출의 깊이 제한을 늘림


# DFS 알고리즘을 사용하여 트리를 탐색하고 각 노드의 부모를 찾는 함수
def dfs(n, graph):
    v = 1
    visited = [0] * (
        n + 1
    )  # 각 노드의 부모를 저장할 리스트. 인덱스는 노드 번호를 나타냄
    for i in graph[v]:  # 주어진 노드의 자식 노드들을 탐색
        if not visited[i]:  # 아직 부모가 정해지지 않은 노드라면
            visited[i] = v  # 부모를 설정
            dfs(i)  # 자식 노드에 대해 DFS를 수행

    # 루트 노드를 제외한 모든 노드의 부모를 출력
    for i in range(2, n + 1):
        print(visited[i])


# 문제를 해결하는 메인 함수
def solution():
    n = int(input())  # 노드의 개수를 입력받음
    graph = [
        [] for _ in range(n + 1)
    ]  # 트리를 나타내는 2차원 리스트. 각 인덱스는 노드 번호를 나타냄
    # 트리의 간선 정보를 입력받음
    for _ in range(n - 1):
        x, y = map(int, input().split())  # 간선의 양 끝점을 입력받음
        graph[x].append(y)  # 노드 x의 자식 노드로 노드 y를 추가
        graph[y].append(x)  # 노드 y의 자식 노드로 노드 x를 추가

    dfs(n, graph)  # DFS를 수행하여 각 노드의 부모를 찾음


# 메인 함수를 호출하여 문제를 해결
solution()
