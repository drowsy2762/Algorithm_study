# 2026-07-06


def solution(k, d):
    answer = 0
    y = (d // k) * k
    d_squared = d**2
    for x in range(0, d + 1, k):
        x_squared = x**2
        while x_squared + (y**2) > d_squared:
            y -= k
        answer += (y // k) + 1

    return answer
