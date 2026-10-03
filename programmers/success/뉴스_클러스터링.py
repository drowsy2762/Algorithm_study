# 2026-10-03

from collections import Counter


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = [str1[i : i + 2] for i in range(len(str1) - 1) if str1[i : i + 2].isalpha()]
    list2 = [str2[i : i + 2] for i in range(len(str2) - 1) if str2[i : i + 2].isalpha()]

    if not list1 and not list2:
        return 65536

    counter1 = Counter(list1)
    counter2 = Counter(list2)
    intersection = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())

    return int((intersection / union) * 65536)
