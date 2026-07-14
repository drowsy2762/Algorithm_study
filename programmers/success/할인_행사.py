# 2026-07-14
"""
Counter 편법
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
"""


def solution(want, number, discount):
    answer = 0
    target_dict = {w: n for w, n in zip(want, number)}
    current_dict = {}
    for i in range(10):
        item = discount[i]
        current_dict[item] = current_dict.get(item, 0) + 1

    if current_dict == target_dict:
        answer += 1

    for i in range(10, len(discount)):
        out_item = discount[i - 10]
        current_dict[out_item] -= 1
        if current_dict[out_item] == 0:
            del current_dict[out_item]
        in_item = discount[i]
        current_dict[in_item] = current_dict.get(in_item, 0) + 1

        if current_dict == target_dict:
            answer += 1

    return answer
