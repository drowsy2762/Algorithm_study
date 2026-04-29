# 등장하지 않는 문자의 합 : https://www.acmicpc.net/problem/3059 (python3)


def ascil_num(s):
    spell = []
    ascil_num = 2015
    for i in range(len(s)):
        if s[i] not in spell:
            spell.append(s[i])
    for i in spell:
        ascil_num -= ord(i)
    print(ascil_num)


t = int(input())

for _ in range(t):
    s = input()
    ascil_num(s)
