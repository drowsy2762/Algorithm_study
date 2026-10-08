# 2026-10-08


def solution(n):
    col_used = [False] * n
    diag1_used = [False] * (2 * n)
    diag2_used = [False] * (2 * n)

    answer = 0

    def place_queen(row):
        nonlocal answer
        if row == n:
            answer += 1
            return

        for col in range(n):
            diag1_idx = row + col
            diag2_idx = row - col + n
            if col_used[col] or diag1_used[diag1_idx] or diag2_used[diag2_idx]:
                continue
            col_used[col] = True
            diag1_used[diag1_idx] = True
            diag2_used[diag2_idx] = True
            place_queen(row + 1)

            col_used[col] = False
            diag1_used[diag1_idx] = False
            diag2_used[diag2_idx] = False

    place_queen(0)

    return answer
