# 2026-09-23
import re


def solution(files):
    pattern = re.compile(r"^([^\d]+)(\d{1,5})")

    def sort_key(file):
        match = pattern.match(file)
        head = match.group(1)
        number = match.group(2)
        return (head.lower(), int(number))

    return sorted(files, key=sort_key)
