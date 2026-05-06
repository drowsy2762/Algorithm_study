# 2026-05-06


def solution(s):
    count = 0

    for char in s:
        if char == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0
