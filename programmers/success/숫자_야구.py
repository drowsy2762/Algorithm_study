# 2026-11-16

from itertools import permutations


def get_hint(secret, guess):
    strikes = 0
    balls = 0

    for i in range(4):
        if guess[i] == secret[i]:
            strikes += 1
        elif guess[i] in secret:
            balls += 1

    return f"{strikes}S {balls}B"


def solution(n, submit):
    digits = "123456789"
    candidates = ["".join(p) for p in permutations(digits, 4)]

    for _ in range(n):
        guess_str = candidates[0]
        guess_int = int(guess_str)
        result_hint = submit(guess_int)

        if result_hint == "4S 0B":
            return guess_int

        next_candidates = []
        for cand in candidates:
            if get_hint(cand, guess_str) == result_hint:
                next_candidates.append(cand)

        candidates = next_candidates

    return int(candidates[0])
