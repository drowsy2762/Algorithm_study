# https://www.acmicpc.net/problem/12886
# 2026-03-31
import sys
from collections import deque

def solve():
    a, b, c = map(int, sys.stdin.readline().split())
    if (a + b + c) % 3 != 0:
        print(0)
        return

    q = deque([(a, b)])
    visited = set([(a, b)])
    while q:
        x, y = q.popleft()
        z = (a + b + c) - x - y
        if x == y == z:
            print(1)
            return
        
        for na, nb in [(x, y), (y, z), (z, x)]:
            if na < nb:
                na, nb = na * 2, nb - na
            elif na > nb:
                na, nb = na - nb, nb * 2
            else:
                continue
            
            nc = (a + b + c) - na - nb
            next_state = tuple(sorted((na, nb, nc)))[:2]
            if next_state not in visited:
                visited.add(next_state)
                q.append(next_state)
                
    print(0)

if __name__ == "__main__":
    solve()