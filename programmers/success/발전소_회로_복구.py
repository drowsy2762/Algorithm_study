from collections import deque
import sys

sys.setrecursionlimit(100000)


def solution(h, grid, panels, seqs):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    n = len(grid)
    m = len(grid[0])
    board = [list(row) for row in grid]

    def bfs(start_x, start_y):
        dist = [[-1] * m for _ in range(n)]
        dist[start_x][start_y] = 0
        q = deque([(start_x, start_y)])

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] != "#" and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        return dist

    el_x, el_y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "@":
                board[i][j] = "."
                el_x, el_y = i, j

    dist_from_el = bfs(el_x, el_y)

    k = len(panels)
    dist_from_panel = []
    for floor, r, c in panels:
        dist_from_panel.append(bfs(r - 1, c - 1))

    p_dist = [[0] * k for _ in range(k)]
    for i in range(k):
        f1, r1, c1 = panels[i]
        r1, c1 = r1 - 1, c1 - 1
        for j in range(k):
            if i == j:
                continue
            f2, r2, c2 = panels[j]
            r2, c2 = r2 - 1, c2 - 1

            if f1 == f2:
                p_dist[i][j] = dist_from_panel[i][r2][c2]
            else:
                to_el = dist_from_el[r1][c1]
                el_m = abs(f1 - f2)
                from_el = dist_from_el[r2][c2]
                p_dist[i][j] = to_el + el_m + from_el

    prereq = [0] * k
    for a, b in seqs:
        u, v = a - 1, b - 1
        prereq[v] |= 1 << u

    ALL_ACTIVATED = (1 << k) - 1
    memo = {}

    def find_min_time(cur, mask):
        if mask == ALL_ACTIVATED:
            return 0
        if (cur, mask) in memo:
            return memo[(cur, mask)]

        min_time = float("inf")

        for nxt in range(k):
            if not (mask & (1 << nxt)) and (mask & prereq[nxt]) == prereq[nxt]:
                cost = p_dist[cur][nxt] + find_min_time(nxt, mask | (1 << nxt))
                if cost < min_time:
                    min_time = cost

        memo[(cur, mask)] = min_time
        return min_time

    initial_mask = 1 if prereq[0] == 0 else 0

    return find_min_time(0, initial_mask)
