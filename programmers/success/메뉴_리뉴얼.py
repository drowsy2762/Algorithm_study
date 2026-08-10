# 2026-08-10

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            sorted_order = sorted(order)
            for comb in combinations(sorted_order, k):
                candidates.append("".join(comb))
        counter = Counter(candidates)

        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for menu, count in counter.items():
                    if count == max_count:
                        answer.append(menu)

    return sorted(answer)
