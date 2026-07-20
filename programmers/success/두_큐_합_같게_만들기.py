from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    total_sum = sum1 + sum2
    target_sum = total_sum // 2
    ops = 0
    max_ops = len(queue1) * 4

    if (total_sum) % 2 != 0:
        return -1

    while ops <= max_ops:
        if sum1 == target_sum:
            return ops
        if sum1 > sum2:
            n = q1.popleft()
            q2.append(n)
            sum1 -= n
            sum2 += n
        else:
            n = q2.popleft()
            q1.append(n)
            sum1 += n
            sum2 -= n
        ops += 1
    return -1


"""
결국 두 리스트의 합계를 같게 만들어야함
그리드 알고리즘을 활용하여 무식하게 풀이해봄
"""
