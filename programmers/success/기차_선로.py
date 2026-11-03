def solution(grid):
    n = len(grid)
    m = len(grid[0])

    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]
    OPPOSITE = [2, 3, 0, 1]
    TRACK_PORTS = {
        1: {1, 3},
        2: {0, 2},
        3: {0, 1, 2, 3},
        4: {0, 3},
        5: {0, 1},
        6: {1, 2},
        7: {2, 3},
    }

    EMPTY_CANDIDATES = {0: [2, 6, 7], 1: [1, 4, 7], 2: [2, 4, 5], 3: [1, 5, 6]}

    board = [row[:] for row in grid]
    is_initial = [[False] * m for _ in range(n)]
    initial_tracks = set()
    initial_crosses = set()

    for r in range(n):
        for c in range(m):
            if 1 <= board[r][c] <= 7:
                is_initial[r][c] = True
                initial_tracks.add((r, c))
                if board[r][c] == 3:
                    initial_crosses.add((r, c))

    visited_normal = set()
    cross_h_visited = set()
    cross_v_visited = set()

    answer = 0

    def get_exit_dir(track, in_dir):
        entry_port = OPPOSITE[in_dir]
        if entry_port not in TRACK_PORTS[track]:
            return -1
        if track == 3:
            return in_dir
        for port in TRACK_PORTS[track]:
            if port != entry_port:
                return port
        return -1

    def dfs(r, c, in_dir):
        nonlocal answer

        if r == n - 1 and c == m - 1:
            all_visited = visited_normal | cross_h_visited | cross_v_visited
            if not initial_tracks.issubset(all_visited):
                return
            if not initial_crosses.issubset(
                cross_h_visited
            ) or not initial_crosses.issubset(cross_v_visited):
                return
            answer += 1
            return

        nr = r + DR[in_dir]
        nc = c + DC[in_dir]

        if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] == -1:
            return

        next_cell = board[nr][nc]
        is_horizontal = in_dir in (1, 3)

        if next_cell > 0:
            if next_cell == 3:
                if is_horizontal:
                    if (nr, nc) in cross_h_visited:
                        return
                    cross_h_visited.add((nr, nc))
                    dfs(nr, nc, in_dir)
                    cross_h_visited.remove((nr, nc))
                else:
                    if (nr, nc) in cross_v_visited:
                        return
                    cross_v_visited.add((nr, nc))
                    dfs(nr, nc, in_dir)
                    cross_v_visited.remove((nr, nc))

            elif not is_initial[nr][nc] and (
                (next_cell == 1 and not is_horizontal)
                or (next_cell == 2 and is_horizontal)
            ):
                board[nr][nc] = 3
                if is_horizontal:
                    cross_h_visited.add((nr, nc))
                    cross_v_visited.add((nr, nc))
                    dfs(nr, nc, in_dir)
                    cross_v_visited.remove((nr, nc))
                    cross_h_visited.remove((nr, nc))
                else:
                    cross_h_visited.add((nr, nc))
                    cross_v_visited.add((nr, nc))
                    dfs(nr, nc, in_dir)
                    cross_v_visited.remove((nr, nc))
                    cross_h_visited.remove((nr, nc))
                board[nr][nc] = next_cell

            elif is_initial[nr][nc] and (nr, nc) not in visited_normal:
                exit_dir = get_exit_dir(next_cell, in_dir)
                if exit_dir != -1:
                    visited_normal.add((nr, nc))
                    dfs(nr, nc, exit_dir)
                    visited_normal.remove((nr, nc))

        elif next_cell == 0:
            for cand_track in EMPTY_CANDIDATES[in_dir]:
                exit_dir = get_exit_dir(cand_track, in_dir)
                board[nr][nc] = cand_track
                visited_normal.add((nr, nc))
                dfs(nr, nc, exit_dir)
                visited_normal.remove((nr, nc))
                board[nr][nc] = 0

    visited_normal.add((0, 0))
    dfs(0, 0, 1)

    return answer
