# https://www.acmicpc.net/problem/2607 : 비슷한 단어 (python3)
# 2023-10-30
from sys import stdin

input = stdin.readline

n = int(input())
word = list(input())
answer = 0

for _ in range(n - 1):
    compare = word[:]
    s = input()
    cnt = 0

    for w in s:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)
