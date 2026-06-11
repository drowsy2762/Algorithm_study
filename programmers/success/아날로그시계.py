# 2026-06-11


def solution(h1, m1, s1, h2, m2, s2):
    FULL_CIRCLE = 360 * 120
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2
    answer = 0

    s_start = (t1 * 720) % FULL_CIRCLE
    m_start = (t1 * 12) % FULL_CIRCLE
    h_start = (t1 * 1) % FULL_CIRCLE

    if s_start == m_start or s_start == h_start:
        answer += 1

    for t in range(t1, t2):
        s_cur = (t * 720) % FULL_CIRCLE
        m_cur = (t * 12) % FULL_CIRCLE
        h_cur = (t * 1) % FULL_CIRCLE
        s_next = (
            FULL_CIRCLE
            if ((t + 1) * 720) % FULL_CIRCLE == 0
            else ((t + 1) * 720) % FULL_CIRCLE
        )
        m_next = (
            FULL_CIRCLE
            if ((t + 1) * 12) % FULL_CIRCLE == 0
            else ((t + 1) * 12) % FULL_CIRCLE
        )
        h_next = (
            FULL_CIRCLE
            if ((t + 1) * 1) % FULL_CIRCLE == 0
            else ((t + 1) * 1) % FULL_CIRCLE
        )

        match_m = s_cur < m_cur and s_next >= m_next
        match_h = s_cur < h_cur and s_next >= h_next

        if match_m:
            answer += 1
        if match_h:
            answer += 1

        if match_m and match_h:
            if s_next == m_next and m_next == h_next:
                answer -= 1

    return answer
