# 접미사 배열 : https://www.acmicpc.net/problem/11656 (python3)

s = input()
suffix = []
for i in range(len(s)):
    suffix.append(s[i:])
suffix.sort()
for i in suffix:
    print(i)
