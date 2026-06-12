# 2026-06-12


def solution(targets):
    targets.sort(key=lambda x: x[1])

    answer = 0
    last_intercept = -1
    for s, e in targets:
        if s >= last_intercept:
            answer += 1
            last_intercept = e
    return answer
