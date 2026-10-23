# 2026-10-23


def solution(board):
    r = len(board)
    c = len(board[0])
    max_side = 0
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0:
                if board[i][j] == 1:
                    max_side = max(max_side, 1)
            else:
                if board[i][j] == 1:
                    board[i][j] = (
                        min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                    )
                    max_side = max(max_side, board[i][j])

    return max_side * max_side
