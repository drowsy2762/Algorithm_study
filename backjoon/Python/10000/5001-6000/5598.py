# 카이사르 암호 : https://www.acmicpc.net/problem/5598 (python3)
import sys

word = input()
for i in range(len(word)):
    if ord(word[i]) > 67 and ord(word[i]) < 91:
        s = ord(word[i]) - 3
    else:
        s = ord(word[i]) + 23
    print(chr(s), end="")
