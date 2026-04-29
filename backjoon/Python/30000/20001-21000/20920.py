# https://www.acmicpc.net/problem/20920 : 영단어 암기는 괴로워 (python3)
# 2023-10-06
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

word_lst = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) < m:
        continue
    else:
        if word in word_lst:
            word_lst[word] += 1
        else:
            word_lst[word] = 1

word_lst = sorted(word_lst.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in word_lst:
    print(i[0])
