# 2026-09-03


def solution(brown, yellow):
    total = brown + yellow
    h = 3
    while True:
        if total % h == 0:
            w = total // h
            if w + h == (brown + 4) // 2:
                return [w, h]
        h += 1
