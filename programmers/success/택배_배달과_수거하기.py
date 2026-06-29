# 2026-06-29


def solution(cap, n, deliveries, pickups):
    answer = 0
    give = 0
    get = 0

    for i in range(n - 1, -1, -1):
        give -= deliveries[i]
        get -= pickups[i]
        cnt = 0
        while give < 0 or get < 0:
            give += cap
            get += cap
            cnt += 1
        if cnt > 0:
            answer += (i + 1) * 2 * cnt

    return answer
