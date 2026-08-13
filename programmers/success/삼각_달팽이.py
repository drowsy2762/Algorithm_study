# 2026-08-13


def solution(n):
    triangle = [[0] * (i + 1) for i in range(n)]

    row, col = -1, 0
    num = 1

    for i in range(n):
        mode = i % 3
        for _ in range(i, n):
            if mode == 0:
                row += 1
            elif mode == 1:
                col += 1
            elif mode == 2:
                row -= 1
                col -= 1

            triangle[row][col] = num
            num += 1

    answer = []
    for r in triangle:
        answer.extend(r)

    return answer
