# 2026-05-23


def solution(beginning, target):
    R = len(beginning)
    C = len(beginning[0])

    diff = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if beginning[i][j] != target[i][j]:
                diff[i][j] = 1

    def check_scenario(flip_first_row):
        flip_count = 0
        cols_to_flip = [0] * C
        for j in range(C):
            current_state = 1 - diff[0][j] if flip_first_row else diff[0][j]
            if current_state == 1:
                cols_to_flip[j] = 1
                flip_count += 1

        if flip_first_row:
            flip_count += 1

        for i in range(1, R):
            row_diff_sum = 0
            for j in range(C):
                current_val = 1 - diff[i][j] if cols_to_flip[j] else diff[i][j]
                row_diff_sum += current_val
            if row_diff_sum == 0:
                pass
            elif row_diff_sum == C:
                flip_count += 1
            else:
                return float("inf")
        return flip_count

    ans1 = check_scenario(False)
    ans2 = check_scenario(True)
    answer = min(ans1, ans2)
    return answer if answer != float("inf") else -1
