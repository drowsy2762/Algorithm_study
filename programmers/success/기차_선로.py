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
        4: {0, 1},
        5: {0, 3},
        6: {1, 2},
        7: {2, 3},
    }

    board = [row[:] for row in grid]
    initial_tracks = set()
    placed_cross_tracks = set()

    for r in range(n):
        for c in range(m):
            if 1 <= board[r][c] <= 7:
                initial_tracks.add((r, c))
                if board[r][c] == 3:
                    placed_cross_tracks.add((r, c))

    answer = 0
    visited_tracks = set()
    cross_h_visited = set()
    cross_v_visited = set()

    def can_be_cross(r, c):
        for d in range(4):
            nr, nc = r + DR[d], c + DC[d]
            if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] == -1:
                return False
        return True

    def is_valid_layout():
        all_visited = visited_tracks | cross_h_visited | cross_v_visited
        if not initial_tracks.issubset(all_visited):
            return False

        if (
            cross_h_visited != placed_cross_tracks
            or cross_v_visited != placed_cross_tracks
        ):
            return False

        for cr, cc in placed_cross_tracks:
            for d in range(4):
                nr, nc = cr + DR[d], cc + DC[d]
                neighbor = board[nr][nc]
                if (
                    neighbor not in TRACK_PORTS
                    or OPPOSITE[d] not in TRACK_PORTS[neighbor]
                ):
                    return False

        return True

    def dfs(r, c, in_dir):
        nonlocal answer
        if r == n - 1 and c == m - 1:
            dest_track = board[r][c]
            if (dest_track == 1 and in_dir == 1) or (dest_track == 2 and in_dir == 2):
                if is_valid_layout():
                    answer += 1
            return

        nr = r + DR[in_dir]
        nc = c + DC[in_dir]

        if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] == -1:
            return

        entry_port = OPPOSITE[in_dir]

        if board[nr][nc] > 0:
            track = board[nr][nc]
            if entry_port not in TRACK_PORTS[track]:
                return

            if track == 3:
                if entry_port in (1, 3):
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
            else:
                if (nr, nc) in visited_tracks:
                    return
                exit_port = next(iter(TRACK_PORTS[track] - {entry_port}))
                visited_tracks.add((nr, nc))
                dfs(nr, nc, exit_port)
                visited_tracks.remove((nr, nc))

        elif board[nr][nc] == 0:
            for cand_track, ports in TRACK_PORTS.items():
                if entry_port not in ports:
                    continue

                if cand_track == 3:
                    if not can_be_cross(nr, nc):
                        continue
                    board[nr][nc] = 3
                    placed_cross_tracks.add((nr, nc))

                    if entry_port in (1, 3):
                        cross_h_visited.add((nr, nc))
                        dfs(nr, nc, in_dir)
                        cross_h_visited.remove((nr, nc))
                    else:
                        cross_v_visited.add((nr, nc))
                        dfs(nr, nc, in_dir)
                        cross_v_visited.remove((nr, nc))

                    placed_cross_tracks.remove((nr, nc))
                    board[nr][nc] = 0
                else:
                    board[nr][nc] = cand_track
                    exit_port = next(iter(ports - {entry_port}))
                    visited_tracks.add((nr, nc))
                    dfs(nr, nc, exit_port)
                    visited_tracks.remove((nr, nc))
                    board[nr][nc] = 0

    visited_tracks.add((0, 0))
    dfs(0, 0, 1)

    return answer
