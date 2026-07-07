# 2026-07-07


def solution(k, ranges):
    answer = []
    y_values = [k]
    while k > 1:
        if (k % 2) == 0:
            k //= 2
        else:
            k = (k * 3) + 1
        y_values.append(k)
    n = len(y_values) - 1
    areas = [0.0]
    cumulative_area = 0.0

    for i in range(n):
        instant_area = (y_values[i] + y_values[i + 1]) / 2
        cumulative_area += instant_area
        areas.append(cumulative_area)
    for a, b in ranges:
        start = a
        end = n + b
        if start > end:
            answer.append(-1.0)
        else:
            total_area = areas[end] - areas[start]
            answer.append(total_area)

    return answer

    return answer


"""
n이 짝수면 2로 누나기
n이 홀수면 3을 곱하고 1 더하기
결과로 나온수가 1보다 작아질 때 까지 반복
정적분을 해야함? ? 갑자기
문제가 요구하는것 k에 대해 콜라츠 추측 그래프를 그린후
ranges 범위에 대해 편미분 값을 구하는 것
"""
