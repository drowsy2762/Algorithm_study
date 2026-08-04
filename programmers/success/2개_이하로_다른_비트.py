# 2026-08-04


def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            answer.append(x + 1)
        else:
            lowest_zero_bit = (x + 1) & ~x
            answer.append(x + (lowest_zero_bit >> 1))

    return answer
