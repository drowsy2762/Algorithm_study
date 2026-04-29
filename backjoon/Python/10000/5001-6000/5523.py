# 경기 결과 : https://www.acmicpc.net/problem/5523 (python3)

import sys


def match_result(match_scores):
    a_team, b_team = 0, 0

    for score in match_scores:
        a_score, b_score = score[0], score[1]
        if a_score > b_score:
            a_team += 1
        elif a_score < b_score:
            b_team += 1

    return f"{a_team} {b_team}"


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    match_scores = []
    for _ in range(N):
        a_score, b_score = map(int, sys.stdin.readline().split())
        match_scores.append((a_score, b_score))

    print(match_result(match_scores))
