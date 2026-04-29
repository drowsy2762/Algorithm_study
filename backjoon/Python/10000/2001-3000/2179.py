# https://www.acmicpc.net/problem/2179 : 비슷한 단어 (python3)
# 2024-03-05
from sys import stdin

input = stdin.readline

n = int(input())
words = []
for i in range(n) :
    words.append(input().strip())

print(words) 
