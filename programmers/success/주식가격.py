# 2026-09-14


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            past_idx = stack.pop()
            answer[past_idx] = i - past_idx
        stack.append(i)

    while stack:
        past_idx = stack.pop()
        answer[past_idx] = (n - 1) - past_idx

    return answer
