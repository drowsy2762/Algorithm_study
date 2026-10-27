# 2026-10-27
def solution(n):
    num = []
    while n > 0:
        i = n % 3
        if i == 0:
            num.append("4")
            n = (n // 3) - 1
        elif i == 1:
            num.append("1")
            n = n // 3
        else:
            num.append("2")
            n = n // 3
    num.reverse()
    return "".join(num)
