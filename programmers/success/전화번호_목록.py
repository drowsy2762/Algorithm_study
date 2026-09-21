# 2026-09-21


def solution(phone_book):
    phone_set = set(phone_book)
    for phone in phone_book:
        prefix = ""
        for char in phone[:-1]:
            prefix += char
            if prefix in phone_set:
                return False

    return True
