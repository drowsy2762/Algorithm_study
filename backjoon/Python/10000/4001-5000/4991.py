# https://www.acmicpc.net/problem/4991
# 2026-03-11
import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def get_dist(sx, sy):
    dist = [[-1] * w for _ in range(h)]
    q = deque([(sx, sy)])
    dist[sy][sx] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and dist[ny][nx] == -1:
                if graph[ny][nx] != 'x':
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((nx, ny))
    return dist
    
def build_adj_matrix(num_points, points):
    adj = [[0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        # i번 지점에서 시작하는 거리 지도 전체를 구함
        dists_from_i = get_dist(points[i][0], points[i][1])
        for j in range(num_points):
            # j번 지점의 좌표(x, y)를 확인해서 거리만 가져옴
            target_dist = dists_from_i[points[j][1]][points[j][0]]
            if target_dist == -1:
                return None
            adj[i][j] = target_dist
    return adj

while True:
    # 입력부
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    graph = [list(input().strip()) for _ in range(h)]

    # 위치확인
    robot = None
    dirty_spots = []
    for r in range(h):
        for c in range(w):
            if graph[r][c] == 'o':
                robot = (c, r)
            elif graph[r][c] == '*':
                dirty_spots.append((c, r))
    points = [robot] + dirty_spots
    num_points = len(points)
    num_dirty = len(dirty_spots)
    adj = build_adj_matrix(num_points, points)
    if adj is None:
        print(-1)
        continue

    # 비트마스킹 DP
    dp = [[float('inf')] * num_dirty for _ in range(1 << num_dirty)]
    for i in range(num_dirty):
        dp[1 << i][i] = adj[0][i+1]

    for mask in range(1, 1 << num_dirty):
        for i in range(num_dirty):
            if dp[mask][i] == float('inf'): continue
            for next_node in range(num_dirty):
                if not (mask & (1 << next_node)):
                    new_mask = mask | (1 << next_node)
                    dp[new_mask][next_node] = min(dp[new_mask][next_node], dp[mask][i] + adj[i+1][next_node+1])

    ans = min(dp[(1 << num_dirty) - 1]) if num_dirty > 0 else 0
    print(ans)