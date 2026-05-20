# 2026-05-20


def solution(board, skill):
    answer = 0
    R = len(board)
    C = len(board[0])

    tmp = [[0] * (C + 1) for _ in range(R + 1)]
    for status, x1, y1, x2, y2, damage in skill:
        d = -damage if status == 1 else damage

        tmp[x1][y1] += d
        tmp[x1][y2 + 1] -= d
        tmp[x2 + 1][y1] -= d
        tmp[x2 + 1][y2 + 1] += d

    for i in range(R + 1):
        for j in range(1, C + 1):
            tmp[i][j] += tmp[i][j - 1]

    for j in range(C + 1):
        for i in range(1, R + 1):
            tmp[i][j] += tmp[i - 1][j]

    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += tmp[y][x]
            if board[y][x] > 0:
                answer += 1

    return answer
