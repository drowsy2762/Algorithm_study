# 2026-06-10


def solution(land):
    N = len(land)
    M = len(land[0])
    parent = [i for i in range(N * M)]
    size = [0] * (N * M)
    for r in range(N):
        for c in range(M):
            if land[r][c] == 1:
                size[r * M + c] = 1

    def get_id(r, c):
        return r * M + c

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rootX > rootY:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
            else:
                parent[rootY] = rootX
                size[rootX] += size[rootY]

    for r in range(N):
        for c in range(M):
            if land[r][c] == 1:
                curr_id = get_id(r, c)

                for dr, dc in [(1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M:
                        if land[nr][nc] == 1:
                            next_id = get_id(nr, nc)
                            union(curr_id, next_id)

    max_oil = 0

    for c in range(M):
        current_col_oil = 0
        unique_roots = set()
        for r in range(N):
            if land[r][c] == 1:
                oil_id = get_id(r, c)
                unique_roots.add(find(oil_id))

        for root in unique_roots:
            current_col_oil += size[root]

        if current_col_oil > max_oil:
            max_oil = current_col_oil

    return max_oil
