# 2026-06-05

import itertools


def solution(n, q, ans):
    all_combinations = list(itertools.combinations(range(1, n + 1), 5))

    for idx in range(len(q)):
        current_hint = q[idx]
        target_count = ans[idx]
        survived_codes = []

        for code in all_combinations:
            match_count = 0
            for number in code:
                if number in current_hint:
                    match_count += 1

            if match_count == target_count:
                survived_codes.append(code)

        all_combinations = survived_codes

    return len(all_combinations)
