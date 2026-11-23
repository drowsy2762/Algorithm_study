from collections import deque

DIR_MAP = {
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
    4: (-1, 0),
}


def extract_apps(board):
    n, m = len(board), len(board[0])
    bounds = {}

    for r in range(n):
        for c in range(m):
            app_id = board[r][c]
            if app_id == 0:
                continue

            if app_id not in bounds:
                bounds[app_id] = [r, c, r, c]
            else:
                min_r, min_c, max_r, max_c = bounds[app_id]
                bounds[app_id] = [
                    min(min_r, r),
                    min(min_c, c),
                    max(max_r, r),
                    max(max_c, c),
                ]

    apps = {}
    for app_id, (min_r, min_c, max_r, _) in bounds.items():
        size = max_r - min_r + 1
        apps[app_id] = [min_r, min_c, size]

    return apps


def get_cells(app, n, m):
    r, c, size = app
    return {((r + dr) % n, (c + dc) % m) for dr in range(size) for dc in range(size)}


def is_inside(app, n, m):
    r, c, size = app
    return r + size <= n and c + size <= m


def render_board(n, m, apps):
    grid = [[0] * m for _ in range(n)]
    for app_id, app in apps.items():
        for r, c in get_cells(app, n, m):
            grid[r][c] = app_id

    return grid


def solution(board, commands):
    n, m = len(board), len(board[0])
    apps = extract_apps(board)

    for app_id, arrow in commands:
        dr, dc = DIR_MAP[arrow]
        queue = deque([app_id])
        in_queue = {app_id}

        while queue:
            pusher_id = queue.popleft()
            in_queue.remove(pusher_id)
            r, c, size = apps[pusher_id]

            apps[pusher_id] = [
                (r + dr) % n,
                (c + dc) % m,
                size,
            ]

            current_cells = get_cells(apps[pusher_id], n, m)

            for other_id in apps:
                if other_id == pusher_id:
                    continue

                other_cells = get_cells(apps[other_id], n, m)

                if current_cells & other_cells:
                    if other_id not in in_queue:
                        queue.append(other_id)
                        in_queue.add(other_id)

            if not is_inside(apps[pusher_id], n, m):
                if pusher_id not in in_queue:
                    queue.append(pusher_id)
                    in_queue.add(pusher_id)

    return render_board(n, m, apps)
