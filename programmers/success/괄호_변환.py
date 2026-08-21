# 2026-08-21


def solution(p):
    if not p:
        return ""

    def is_correct(s):
        cnt = 0
        for char in s:
            if char == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    cnt = 0
    split_index = 0

    for i, char in enumerate(p):
        if char == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            split_index = i + 1
            break

    u = p[:split_index]
    v = p[split_index:]

    if is_correct(u):
        return u + solution(v)
    else:
        result = "(" + solution(v) + ")"
        flipped_u = ""
        for char in u[1:-1]:
            if char == "(":
                flipped_u += ")"
            else:
                flipped_u += "("

        return result + flipped_u
