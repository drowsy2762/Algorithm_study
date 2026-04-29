# 좋은 자동차 번호판 : https://www.acmicpc.net/problem/1871 (python3)
import math


def num_value(a):
    a_sum = 0
    n_sum = 0
    for i in range(4):
        n_sum += int(a[4 + i]) * int((10000 / (10 ** (i + 1))))
    for i in range(3):
        k = ord(a[i]) - 65
        a_sum += k * (math.pow(26, 2 - i))
    if abs(int(a_sum) - int(n_sum)) <= 100:
        print("nice")
    else:
        print("not nice")


n = int(input())
num = []
for i in range(n):
    num_value(input())
