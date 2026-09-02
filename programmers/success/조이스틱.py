# 2026-09-02


def solution(name):
    n = len(name)
    answer = 0
    min_move = n - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        next_idx = i + 1
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1

        min_move = min(min_move, 2 * i + (n - next_idx))
        min_move = min(min_move, 2 * (n - next_idx) + i)

    return answer + min_move
