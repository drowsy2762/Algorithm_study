# 2026-06-23


def solution(book_time):
    timeline = [0] * 1450

    for start, end in book_time:
        start_min = int(start[:2]) * 60 + int(start[3:])
        end_min = int(end[:2]) * 60 + int(end[3:]) + 10
        for i in range(start_min, end_min):
            timeline[i] += 1

    return max(timeline)
