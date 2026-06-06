# 2026-06-06


def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid_level = (left + right) // 2
        total_time = 0
        for idx in range(len(diffs)):
            diff = diffs[idx]
            time_cur = times[idx]
            if idx > 0:
                time_prev = times[idx - 1]
            else:
                time_prev = 0

            if diff <= mid_level:
                total_time += time_cur

            else:
                fail_count = diff - mid_level
                total_time += (fail_count * (time_cur + time_prev)) + time_cur

        if total_time <= limit:
            answer = mid_level
            right = mid_level - 1
        else:
            left = mid_level + 1

    return answer
