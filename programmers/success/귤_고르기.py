# 2026-07-05


def solution(k, tangerine):
    tangerine_counts = {}
    for size in tangerine:
        if size in tangerine_counts:
            tangerine_counts[size] += 1
        else:
            tangerine_counts[size] = 1
    sorted_counts = sorted(tangerine_counts.values(), reverse=True)

    answer = 0
    for count in sorted_counts:
        k -= count
        answer += 1

        if k <= 0:
            break

    return answer
