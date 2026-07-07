# 2026-07-07

from math import gcd


def solution(arrayA, arrayB):
    gcdA = gcd(*arrayA)
    gcdB = gcd(*arrayB)

    a1 = gcdA if gcdA > 1 and all(x % gcdA != 0 for x in arrayB) else 0
    a2 = gcdB if gcdB > 1 and all(x % gcdB != 0 for x in arrayA) else 0

    return max(a1, a2)


"""
array A = array B
조건 array A 와 array B가 모두 나눌 수 있는 정수 a 중에 가장 큰 수를 구해야함
조건 -> 수학적 
"""
