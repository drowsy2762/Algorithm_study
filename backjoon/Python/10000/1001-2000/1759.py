# https://www.acmicpc.net/problem/1759
# 2026-01-26
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(list(input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

def check(password):
    v_count = 0 # 모음 개수
    c_count = 0 # 자음 개수
    
    for char in password:
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
        
    if v_count >= 1 and c_count >= 2:
        return True
    return False

def backtrack(start_idx, current_seq):
    if len(current_seq) == L:
        if check(current_seq):
            print("".join(current_seq))
        return

    for i in range(start_idx, C):
        backtrack(i + 1, current_seq + [chars[i]])

backtrack(0, [])