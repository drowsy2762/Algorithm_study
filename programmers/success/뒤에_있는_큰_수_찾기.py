# 2026-06-25


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            popped_idx = stack.pop()
            answer[popped_idx] = numbers[i]

        stack.append(i)

    return answer
