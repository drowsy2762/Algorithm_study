# 2026-08-19
import math


def solution(w, h):
    total_squares = w * h
    broken_squares = w + h - math.gcd(w, h)
    return total_squares - broken_squares
