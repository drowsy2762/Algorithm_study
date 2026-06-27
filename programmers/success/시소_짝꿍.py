# 2026-06-27

from collections import Counter


def solution(weights):
    answer = 0
    weight_counts = Counter(weights)

    for w in weight_counts:
        count = weight_counts[w]
        if count > 1:
            answer += (count * (count - 1)) // 2
        if (w * 4) % 3 == 0 and (w * 4) // 3 in weight_counts:
            answer += count * weight_counts[(w * 4) // 3]
        if (w * 3) % 2 == 0 and (w * 3) // 2 in weight_counts:
            answer += count * weight_counts[(w * 3) // 2]
        if w * 2 in weight_counts:
            answer += count * weight_counts[w * 2]

    return answer
