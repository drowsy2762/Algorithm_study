# 2026-07-21


def solution(n, info):
    max_diff = 0
    best_comb = [-1]

    def dfs(idx, arrows_left, ryan_shot):
        nonlocal max_diff, best_comb
        if idx == 11:
            ryan_shot[10] += arrows_left
            ryan_score, apeach_score = 0, 0
            for i in range(11):
                if info[i] == 0 and ryan_shot[i] == 0:
                    continue  # 둘 다 0발이면 점수 없음
                if ryan_shot[i] > info[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i

            diff = ryan_score - apeach_score

            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    best_comb = ryan_shot[:]
                elif diff == max_diff:
                    if ryan_shot[::-1] > best_comb[::-1]:
                        best_comb = ryan_shot[:]

            ryan_shot[10] -= arrows_left
            return

        needed = info[idx] + 1
        if arrows_left >= needed:
            ryan_shot[idx] = needed
            dfs(idx + 1, arrows_left - needed, ryan_shot)
            ryan_shot[idx] = 0

        dfs(idx + 1, arrows_left, ryan_shot)

    dfs(0, n, [0] * 11)

    return best_comb
