# 2026-05-19


def solution(a):
    n = len(a)
    left_min = [0] * n
    right_min = [0] * n
    if n <= 2:
        return n

    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = left_min[i - 1] if left_min[i - 1] < a[i] else a[i]
    right_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = right_min[i + 1] if right_min[i + 1] < a[i] else a[i]

    answer = 0
    for i in range(n):
        if a[i] == left_min[i] or a[i] == right_min[i]:
            answer += 1

    return answer
