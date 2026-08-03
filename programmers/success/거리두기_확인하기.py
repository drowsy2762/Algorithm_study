# 2026-08-03

from collections import deque


def check_place(place):
    people = []
    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                people.append((r, c))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for start_r, start_c in people:
        queue = deque([(start_r, start_c, 0)])
        visited = [[False] * 5 for _ in range(5)]
        visited[start_r][start_c] = True
        while queue:
            r, c, dist = queue.popleft()
            if dist == 2:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if place[nr][nc] == "X":
                        continue
                    if place[nr][nc] == "P":
                        return 0
                    queue.append((nr, nc, dist + 1))

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_place(place))
    return answer
