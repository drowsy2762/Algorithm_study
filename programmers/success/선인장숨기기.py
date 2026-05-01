# 2026-05-01
from collections import deque


def solution(m, n, h, w, drops):
    field = [[float("inf")] * n for _ in range(m)]
    for i, (r, c) in enumerate(drops):
        if field[r][c] == float("inf"):
            field[r][c] = i

    row_min = [[0] * (n - w + 1) for _ in range(m)]
    for r in range(m):
        dq = deque()
        for c in range(n):
            if dq and dq[0] <= c - w:
                dq.popleft()
            while dq and field[r][dq[-1]] >= field[r][c]:
                dq.pop()
            dq.append(c)
            if c >= w - 1:
                row_min[r][c - w + 1] = field[r][dq[0]]

    final_hit_time = [[0] * (n - w + 1) for _ in range(m - h + 1)]
    for c in range(n - w + 1):
        dq = deque()
        for r in range(m):
            if dq and dq[0] <= r - h:
                dq.popleft()
            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()
            dq.append(r)
            if r >= h - 1:
                final_hit_time[r - h + 1][c] = row_min[dq[0]][c]

    max_time = -1
    answer = [0, 0]

    for r in range(m - h + 1):
        for c in range(n - w + 1):
            current_time = final_hit_time[r][c]
            if current_time > max_time:
                max_time = current_time
                answer = [r, c]

    return answer
