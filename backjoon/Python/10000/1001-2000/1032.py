# 명령 프롬프트 : https://www.acmicpc.net/problem/1032 (python3)

n = int(input())
for i in range(n):
    if i == 0:
        word = input()
        continue
    temp = input()
    for j in range(len(word)):
        if word[j] != temp[j]:
            word = word[:j] + "?" + word[j + 1 :]
print(word)
