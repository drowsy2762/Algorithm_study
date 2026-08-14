# 2026-08-14

from itertools import permutations


def solution(expression):
    def parse_expression(text):
        tokens = []
        curr_num = ""

        for char in text:
            if char.isdigit():
                curr_num += char
            else:
                tokens.append(curr_num)
                tokens.append(char)
                curr_num = ""
        tokens.append(curr_num)
        return tokens

    def calculate(a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b

    tokens = parse_expression(expression)
    operators = ["+", "-", "*"]
    all_priorities = permutations(operators)
    max_reward = 0

    for priority in all_priorities:
        temp_tokens = tokens[:]

        for op in priority:
            i = 0
            while i < len(temp_tokens):
                if temp_tokens[i] == op:
                    prev_val = int(temp_tokens[i - 1])
                    next_val = int(temp_tokens[i + 1])
                    calc_val = calculate(prev_val, next_val, op)

                    temp_tokens = (
                        temp_tokens[: i - 1] + [str(calc_val)] + temp_tokens[i + 2 :]
                    )
                    i -= 1
                else:
                    i += 1

        final_result = abs(int(temp_tokens[0]))
        max_reward = max(max_reward, final_result)

    return max_reward
