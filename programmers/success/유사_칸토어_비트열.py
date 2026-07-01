# 2026-07-01


def is_one(idx):
    if idx == 0:
        return True

    if idx % 5 == 2:
        return False

    return is_one(idx // 5)


def solution(n, l, r):
    answer = 0
    for i in range(l - 1, r):
        if is_one(i):
            answer += 1

    return answer
