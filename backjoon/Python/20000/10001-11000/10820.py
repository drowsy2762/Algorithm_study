# 문자열 분석 : https://www.acmicpc.net/problem/10820 (python3)

import sys

while True:
    s = sys.stdin.readline().rstrip("\n")
    if not s:
        break
    lower = 0
    upper = 0
    number = 0
    space = 0
    for i in s:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            space += 1
    print(lower, upper, number, space)
