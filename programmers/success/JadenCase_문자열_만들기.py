# 2026-10-09


def solution(s):
    result = []
    check = True
    for char in s:
        if char == " ":
            result.append(char)
            check = True
        else:
            if check:
                result.append(char.upper())
                check = False
            else:
                result.append(char.lower())
    return "".join(result)
