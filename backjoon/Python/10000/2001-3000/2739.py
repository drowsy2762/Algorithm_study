# https://www.acmicpc.net/problem/2739 : 구구단 (python3)
# 2021-10-04

n = int(input())

for i in range(1, 10):
    print(n, "*", i, "=", n * i)
