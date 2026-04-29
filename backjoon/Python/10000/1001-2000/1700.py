# https://www.acmicpc.net/problem/1700
# 2026-01-29
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
outleg = list(map(int, input().split()))

code = []
ans = 0

for i in range(k):
    if outleg[i] in code:
        continue

    if len(code) < n:
        code.append(outleg[i])
        continue

    priority = []
    for c in code:
        if c in outleg[i:]:
            # .index()는 가장 먼저 발견되는 위치를 반환
            priority.append(outleg[i:].index(c))
        else:
            priority.append(1001)
            
    target = priority.index(max(priority))
    
    code.pop(target)
    code.append(outleg[i])
    ans += 1

print(ans)