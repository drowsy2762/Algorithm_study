# 유학 금지 : https://www.acmicpc.net/problem/2789 (python3)

a = "CAMBRIDGE"
s = list(input())
for i in a:
    for j in range(len(s)):
        if i == s[j]:
            s[j] = ""
for i in s:
    print(i, end="")
