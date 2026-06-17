# 2026-06-17


def solution(board):
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    n, m = len(board), len(board[0])
    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start_x, start_y = i, j
            if board[i][j] == "G":
                end_x, end_y = i, j

    visited = [[float("inf")] * m for _ in range(n)]

    def dfs(x, y, cnt):
        if cnt >= visited[x][y]:
            return
        visited[x][y] = cnt
        if board[x][y] == "G":
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            tx, ty = x, y
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D":
                tx, ty = nx, ny
                nx += dx[i]
                ny += dy[i]

            dfs(tx, ty, cnt + 1)

    dfs(start_x, start_y, 0)
    res = visited[end_x][end_y]
    return res if res != float("inf") else -1
