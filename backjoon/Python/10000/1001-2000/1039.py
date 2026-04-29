# https://www.acmicpc.net/problem/1039
# 2026-03-14
import sys
from collections import deque
input = sys.stdin.readline

n, k = input().rstrip().split()
k = int(k)
m = len(n)
q = deque([(n, 0)])
visited = set()
visited.add((n, 0))

answer = -1

while q:
    now, cnt = q.popleft()
    if cnt == k:
        answer = max(answer, int(now))
        continue
    
    for i in range(m - 1):
        for j in range(i + 1, m):
            now_list = list(now)
            now_list[i], now_list[j] = now_list[j], now_list[i]
            next_num = "".join(now_list)
            if next_num[0] == '0':
                continue
                
            if (next_num, cnt + 1) not in visited:
                visited.add((next_num, cnt + 1))
                q.append((next_num, cnt + 1))

print(answer)