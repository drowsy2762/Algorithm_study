# 2026-06-19


def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def solution(board):
    o_count = 0
    x_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_count += 1
            elif board[i][j] == "X":
                x_count += 1
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    o_win = check_win(board, "O")
    x_win = check_win(board, "X")

    if o_win and x_win:
        return 0
    if o_win and o_count != x_count + 1:
        return 0
    if x_win and o_count != x_count:
        return 0
    return 1
