# 2026-06-26

from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    q = deque([(y, 0)])
    visited = set([y])

    while q:
        curr, dist = q.popleft()
        if curr % 3 == 0:
            nxt = curr // 3
            if nxt == x:
                return dist + 1
            if nxt > x and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, dist + 1))

        if curr % 2 == 0:
            nxt = curr // 2
            if nxt == x:
                return dist + 1
            if nxt > x and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, dist + 1))

        nxt = curr - n
        if nxt == x:
            return dist + 1
        if nxt > x and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, dist + 1))

    return -1
