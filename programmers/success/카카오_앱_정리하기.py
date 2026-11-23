# 2026-11-23
from collections import deque

DIR_VECTORS = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def wrap_coord(val, limit):
    return ((val - 1) % limit) + 1


def extract_apps(board):
    n = len(board)
    m = len(board[0])
    app_cells = {}

    for r in range(n):
        for c in range(m):
            app_id = board[r][c]
            if app_id != 0:
                if app_id not in app_cells:
                    app_cells[app_id] = [r + 1, c + 1, r + 1, c + 1]
                else:
                    min_r, min_c, max_r, max_c = app_cells[app_id]
                    app_cells[app_id] = [
                        min(min_r, r + 1),
                        min(min_c, c + 1),
                        max(max_r, r + 1),
                        max(max_c, c + 1),
                    ]

    apps = {}
    for app_id, (min_r, min_c, max_r, _) in app_cells.items():
        size = max_r - min_r + 1
        apps[app_id] = [min_r, min_c, size]
    return apps


def build_grid(n, m, apps):
    grid = [[0] * m for _ in range(n)]
    for app_id, (r, c, size) in apps.items():
        for dr in range(size):
            for dc in range(size):
                rr = wrap_coord(r + dr, n) - 1
                cc = wrap_coord(c + dc, m) - 1
                grid[rr][cc] = app_id
    return grid


def solution(board, commands):
    n = len(board)
    m = len(board[0])
    apps = extract_apps(board)

    for app_id, direction in commands:
        if app_id not in apps:
            continue

        dr_move, dc_move = DIR_VECTORS[direction]
        grid = build_grid(n, m, apps)

        to_move = set([app_id])
        queue = deque([app_id])

        while queue:
            curr_id = queue.popleft()
            r, c, size = apps[curr_id]

            for dr in range(size):
                for dc in range(size):
                    nr = wrap_coord(r + dr + dr_move, n) - 1
                    nc = wrap_coord(c + dc + dc_move, m) - 1
                    hit_id = grid[nr][nc]
                    if hit_id != 0 and hit_id != curr_id and hit_id not in to_move:
                        to_move.add(hit_id)
                        queue.append(hit_id)

        for target_id in to_move:
            r, c, size = apps[target_id]
            new_r = wrap_coord(r + dr_move, n)
            new_c = wrap_coord(c + dc_move, m)
            apps[target_id] = [new_r, new_c, size]

    result = []
    for app_id in sorted(apps.keys()):
        r, c, size = apps[app_id]
        result.append([r, c, size])

    return result
