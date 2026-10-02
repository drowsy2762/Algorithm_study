# 2026-10-02


def solution(m, n, board):
    grid = [list(row) for row in board]
    total_removed = 0
    while True:
        matched = set()
        for r in range(m - 1):
            for c in range(n - 1):
                target = grid[r][c]
                if target != " " and (
                    target == grid[r + 1][c] == grid[r][c + 1] == grid[r + 1][c + 1]
                ):
                    matched.add((r, c))
                    matched.add((r + 1, c))
                    matched.add((r, c + 1))
                    matched.add((r + 1, c + 1))

        if not matched:
            break

        total_removed += len(matched)
        for r, c in matched:
            grid[r][c] = " "

        for c in range(n):
            remaining_blocks = [
                grid[r][c] for r in range(m - 1, -1, -1) if grid[r][c] != " "
            ]

            for r in range(m - 1, -1, -1):
                idx = (m - 1) - r
                if idx < len(remaining_blocks):
                    grid[r][c] = remaining_blocks[idx]
                else:
                    grid[r][c] = " "

    return total_removed
