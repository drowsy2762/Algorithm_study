# 2026-05-27


def solution(numbers):
    answer = []

    def check_tree(s):
        if len(s) == 1 or "1" not in s:
            return True

        mid = len(s) // 2
        root = s[mid]

        if root == "0":
            return False

        left_subtree = s[:mid]
        right_subtree = s[mid + 1 :]
        return check_tree(left_subtree) and check_tree(right_subtree)

    for num in numbers:
        bin_str = bin(num)[2:]
        length = len(bin_str)
        k = 1
        while (1 << k) - 1 < length:
            k += 1

        full_len = (1 << k) - 1
        padded_bin_str = "0" * (full_len - length) + bin_str

        if check_tree(padded_bin_str):
            answer.append(1)
        else:
            answer.append(0)

    return answer
