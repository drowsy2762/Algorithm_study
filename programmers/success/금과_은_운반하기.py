# 2026-05-16


def solution(a, b, g, s, w, t):
    answer = 4 * 10**14
    start = 0
    end = 4 * 10**14
    while end >= start:
        mid = (end + start) // 2
        gold = 0
        silver = 0
        add = 0
        for i in range(len(t)):
            now_g = g[i]
            now_s = s[i]
            now_w = w[i]
            now_t = t[i]
            move_cnt = mid // (now_t * 2)
            if mid % (now_t * 2) >= now_t:
                move_cnt += 1
            gold += min(now_g, move_cnt * now_w)
            silver += min(now_s, move_cnt * now_w)
            add += min(now_g + now_s, move_cnt * now_w)
        if gold >= a and silver >= b and add >= a + b:
            end = mid - 1
            answer = min(mid, answer)
        else:
            start = mid + 1
    return answer
