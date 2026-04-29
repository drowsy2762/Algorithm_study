# https://www.acmicpc.net/problem/1637 : 날카로운 눈 (Python3)
# 2026-04-16
import sys

def solution():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    info = []
    idx = 1
    for _ in range(n):
        a = int(data[idx])
        c = int(data[idx+1])
        b = int(data[idx+2])
        info.append((a, c, b))
        idx += 3

    def get_sum(target):
        total = 0
        for a, c, b in info:
            if target >= a:
                limit = c if c < target else target
                total += (limit - a) // b + 1
        return total

    left = 1
    right = 2147483647
    ans_val = -1

    if get_sum(right) % 2 == 0:
        print("NOTHING")
        return

    while left <= right:
        mid = (left + right) // 2
        if get_sum(mid) & 1:
            ans_val = mid
            right = mid - 1
        else:
            left = mid + 1

    if ans_val == -1:
        print("NOTHING")
    else:
        count = get_sum(ans_val) - get_sum(ans_val - 1)
        print(f"{ans_val} {count}")

if __name__ == "__main__":
    solution()