# 2026-08-07

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        data = i.split()
        conditions = data[:-1]
        score = int(data[-1])
        for k in range(5):
            for comb in combinations(range(4), k):
                temp_cond = conditions[:]
                for idx in comb:
                    temp_cond[idx] = "-"
                key = "".join(temp_cond)
                info_dict[key].append(score)

    for key in info_dict:
        info_dict[key].sort()

    for q in query:
        q_list = q.replace("and ", "").split()
        q_key = "".join(q_list[:-1])
        q_score = int(q_list[-1])
        if q_key in info_dict:
            scores = info_dict[q_key]
            idx = bisect_left(scores, q_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer
