# 2026-09-22


def convert_to_base(num, base):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = []
    while num > 0:
        result.append(digits[num % base])
        num //= base

    return "".join(reversed(result))


def solution(n, t, m, p):
    required_length = t * m

    game_stream = []
    current_num = 0
    total_len = 0

    while total_len < required_length:
        base_str = convert_to_base(current_num, n)
        game_stream.append(base_str)
        total_len += len(base_str)
        current_num += 1

    full_string = "".join(game_stream)
    tube_answer = full_string[p - 1 : required_length : m]

    return tube_answer
