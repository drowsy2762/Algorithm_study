# 2026-07-09


def solution(order):
    answer = 0
    sub_belt = []
    curr_box = 1
    for target in order:
        while curr_box <= target:
            sub_belt.append(curr_box)
            curr_box += 1
        if sub_belt and sub_belt[-1] == target:
            sub_belt.pop()
            answer += 1
        else:
            break

    return answer
