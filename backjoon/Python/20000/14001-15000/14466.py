# https://www.acmicpc.net/problem/14466
# 2026-03-07
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, k, r = map(int, input().split())
    roads = [[set() for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(r):
        r1, c1, r2, c2 = map(int, input().split())
        roads[r1][c1].add((r2, c2))
        roads[r2][c2].add((r1, c1))
    
    cow_map = [[False] * (n + 1) for _ in range(n + 1)]
    cow_list = []
    for _ in range(k):
        cr, cc = map(int, input().split())
        cow_map[cr][cc] = True
        cow_list.append((cr, cc))

    visited = [[False] * (n + 1) for _ in range(n + 1)]
    cows_in_groups = []
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if not visited[r][c]:
                q = deque([(r, c)])
                visited[r][c] = True
                cnt = 0
                while q:
                    cr, cc = q.popleft()
                    if cow_map[cr][cc]:
                        cnt += 1
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dr, cc + dc
                        if 1 <= nr <= n and 1 <= nc <= n and not visited[nr][nc]:
                            if (nr, nc) not in roads[cr][cc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                if cnt > 0:
                    cows_in_groups.append(cnt)

    total_pairs = k * (k - 1) // 2
    
    can_meet_pairs = 0
    for count in cows_in_groups:
        can_meet_pairs += count * (count - 1) // 2
        
    print(total_pairs - can_meet_pairs)

solve()