# 2026-11-04
def solution(depth, money, excavate):
    w = len(depth)
    INF = float("inf")
    dp_row = [[0] * (w + 2) for _ in range(w + 2)]
    dp_col = [[0] * (w + 2) for _ in range(w + 2)]
    opt = [[0] * (w + 2) for _ in range(w + 2)]

    for i in range(1, w + 1):
        cost = depth[i - 1]
        dp_row[i][i] = cost
        dp_col[i][i] = cost
        opt[i][i] = i

    for length in range(2, w + 1):
        for i in range(1, w - length + 2):
            j = i + length - 1
            best_cost = INF
            best_k = i
            row_i = dp_row[i]
            col_j = dp_col[j]

            for k in range(i, j + 1):
                left_cost = row_i[k - 1]
                right_cost = col_j[k + 1]
                worst_sub = left_cost if left_cost > right_cost else right_cost
                total_cost = depth[k - 1] + worst_sub
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_k = k

            dp_row[i][j] = best_cost
            dp_col[j][i] = best_cost
            opt[i][j] = best_k

    left = 1
    right = w

    while left <= right:
        target_col = opt[left][right]
        result = excavate(target_col)

        if result == 0:
            return target_col
        elif result < 0:
            right = target_col - 1
        else:
            left = target_col + 1

    return -1
