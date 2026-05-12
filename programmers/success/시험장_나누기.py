# 2026-05-12

import sys

sys.setrecursionlimit(10**6)


def solution(k, num, links):
    n = len(num)
    has_parent = [False] * n
    for left, right in links:
        if left != -1:
            has_parent[left] = True
        if right != -1:
            has_parent[right] = True

    root = -1
    for i in range(n):
        if not has_parent[i]:
            root = i
            break

    def check(limit):
        cuts = 0

        def dfs(node):
            nonlocal cuts
            if node == -1:
                return 0
            left_sum = dfs(links[node][0])
            right_sum = dfs(links[node][1])

            if num[node] + left_sum + right_sum <= limit:
                return num[node] + left_sum + right_sum
            if num[node] + min(left_sum, right_sum) <= limit:
                cuts += 1
                return num[node] + min(left_sum, right_sum)

            cuts += 2
            return num[node]

        dfs(root)

        return cuts <= k - 1

    low = max(num)
    high = sum(num)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
