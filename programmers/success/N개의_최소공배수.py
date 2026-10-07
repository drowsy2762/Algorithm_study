# 2026-10-07
import math


def get_lcm(a, b):
    return (a * b) // math.gcd(a, b)


def solution(arr):
    c_lcm = arr[0]
    for num in arr[1:]:
        c_lcm = get_lcm(c_lcm, num)
    return c_lcm
