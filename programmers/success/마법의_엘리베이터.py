# 2026-06-30


def solution(storey):
    ans = 0

    while storey > 0:
        remainder = storey % 10
        if remainder > 5:
            ans += 10 - remainder
            storey = (storey // 10) + 1
        elif remainder < 5:
            ans += remainder
            storey //= 10
        else:
            next_digit = (storey // 10) % 10
            if next_digit >= 5:
                ans += 5
                storey = (storey // 10) + 1
            else:
                ans += 5
                storey //= 10
    return ans
