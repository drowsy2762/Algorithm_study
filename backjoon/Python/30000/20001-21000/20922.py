# https://www.acmicpc.net/problem/20922 : 겹치는 건 싫어 (python3)
# 2023-11-17
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * (max(arr) + 1)
left, right = 0, 0
answer = 0
while right < n:
    if cnt[arr[right]] < k:
        cnt[arr[right]] += 1
        right += 1
    else:
        cnt[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)
