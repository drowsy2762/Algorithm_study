# 2026-07-14

from collections import Counter


def solution(want, number, discount):
    answer = 0
    target_dict = Counter(dict(zip(want, number)))

    for i in range(len(discount) - 9):
        current_window = discount[i : i + 10]
        current_dict = Counter(current_window)
        if current_dict == target_dict:
            answer += 1

    return answer
