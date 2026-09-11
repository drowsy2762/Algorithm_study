# 2026-09-11
import math


def solution(progresses, speeds):
    days_needed = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = []
    current_max_day = days_needed[0]
    count = 0
    for day in days_needed:
        if day <= current_max_day:
            count += 1
        else:
            answer.append(count)
            current_max_day = day
            count = 1
    answer.append(count)

    return answer
