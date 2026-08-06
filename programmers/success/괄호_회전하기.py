# 2026-08-06


def is_valid_brackets(s):
    stack = []
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0


def solution(s):
    answer = 0
    n = len(s)

    for x in range(n):
        rotated_s = s[x:] + s[:x]
        if is_valid_brackets(rotated_s):
            answer += 1

    return answer
