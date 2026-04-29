# https://www.acmicpc.net/problem/16946
# 2026-03-25
import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def solve():
    n, m = map(int, input().split())
    walls = [list(input().rstrip()) for _ in range(n)]
    group_id = [[-1] * m for _ in range(n)]
    group_size = {}
    ans = [['0'] * m for _ in range(n)]
    id_cnt = 0

    def bfs_grouping(start_x, start_y, current_id):
        q = deque([(start_x, start_y)])
        group_id[start_y][start_x] = current_id
        count = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and walls[ny][nx] == '0' and group_id[ny][nx] == -1:
                    group_id[ny][nx] = current_id
                    q.append((nx, ny))
                    count += 1
        return count
    
    for i in range(n):
        for j in range(m):
            if walls[i][j] == '0' and group_id[i][j] == -1:
                group_size[id_cnt] = bfs_grouping(j, i, id_cnt)
                id_cnt += 1

    for i in range(n):
        for j in range(m):
            if walls[i][j] == '1':
                unique_groups = set()
                for d in range(4):
                    nx, ny = j + dx[d], i + dy[d]
                    if 0 <= ny < n and 0 <= nx < m and group_id[ny][nx] != -1:
                        unique_groups.add(group_id[ny][nx])
                
                res = 1
                for g in unique_groups:
                    res += group_size[g]
                ans[i][j] = str(res % 10)

    for row in ans:
        print("".join(row))

if __name__ == "__main__":
    solve()