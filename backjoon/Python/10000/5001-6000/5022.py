# https://www.acmicpc.net/problem/5022 : 연결
# 2026-04-10
import sys
from collections import deque

INF = float('inf')

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    points = []
    for _ in range(4):
        points.append(list(map(int, input().split())))
    
    def bfs(start, end, blocked_path):
        q = deque([start])
        parent = [[None] * (M + 1) for _ in range(N + 1)]
        dist = [[-1] * (M + 1) for _ in range(N + 1)]
        dist[start[0]][start[1]] = 0
        
        while q:
            r, c = q.popleft()
            if [r, c] == end:
                path = []
                curr = (r, c)
                while curr is not None:
                    path.append(curr)
                    curr = parent[curr[0]][curr[1]]
                return dist[r][c], path
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= N and 0 <= nc <= M:
                    if dist[nr][nc] == -1 and (nr, nc) not in blocked_path:
                        dist[nr][nc] = dist[r][c] + 1
                        parent[nr][nc] = (r, c)
                        q.append((nr, nc))

        return INF, []

    d1, path_a = bfs(points[0], points[1], {tuple(points[2]), tuple(points[3])})
    d2, _ = bfs(points[2], points[3], set(path_a))
    res1 = d1 + d2
    d3, path_b = bfs(points[2], points[3], {tuple(points[0]), tuple(points[1])})
    d4, _ = bfs(points[0], points[1], set(path_b))
    res2 = d3 + d4

    ans = min(res1, res2)
    print(ans if ans < INF else "IMPOSSIBLE")

if __name__ == "__main__":
    solution()