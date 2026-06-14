# 2026-06-14


def solution(sequence, k):
    n = len(sequence)
    left = 0
    right = 0
    current_sum = sequence[0]
    min_len = float("inf")
    answer = []
    while right < n:
        if current_sum == k:
            current_len = right - left + 1
            if current_len < min_len:
                min_len = current_len
                answer = [left, right]
            current_sum -= sequence[left]
            left += 1

        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]

        else:
            current_sum -= sequence[left]
            left += 1

    return answer
