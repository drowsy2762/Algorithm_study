# https://www.acmicpc.net/problem/2661
# 2026-02-06
import sys
input = sys.stdin.readline

n = int(input())

def check(seq):
    for i in range(1, len(seq) // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def backtracking(current_seq):
    if len(current_seq) == n:
        print(current_seq)
        sys.exit()
    for i in range(1, 4):
        next_seq = current_seq + str(i)
        if check(next_seq):
            backtracking(next_seq)

backtracking("")