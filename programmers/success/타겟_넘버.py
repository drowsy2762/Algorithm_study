# 2026-08-27


# second code
def solution(numbers, target):
    total = sum(numbers)
    if total < target or (target + total) % 2 != 0:
        return 0

    P = (target + total) // 2
    dp = [0] * (P + 1)
    dp[0] = 1
    for num in numbers:
        for s in range(P, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[P]


# first code


def solution(numbers, target):
    n = len(numbers)
    cnt = 0

    def dfs(i, sum_num):
        nonlocal cnt
        if i == n:
            if sum_num == target:
                cnt += 1
            return
        dfs(i + 1, sum_num + numbers[i])
        dfs(i + 1, sum_num - numbers[i])

    dfs(0, 0)
    print(cnt)
    answer = cnt
    return answer
