# 2026-08-05


def solution(rows, columns, queries):
    graph = [[0] * columns for _ in range(rows)]
    for i in range(rows * columns):
        r = i // columns
        c = i % columns
        graph[r][c] = i + 1

    def rotate(r1, c1, r2, c2):
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        temp = graph[r1][c1]
        min_val = temp
        for r in range(r1, r2):
            graph[r][c1] = graph[r + 1][c1]
            min_val = min(min_val, graph[r][c1])
        for c in range(c1, c2):
            graph[r2][c] = graph[r2][c + 1]
            min_val = min(min_val, graph[r2][c])
        for r in range(r2, r1, -1):
            graph[r][c2] = graph[r - 1][c2]
            min_val = min(min_val, graph[r][c2])
        for c in range(c2, c1 + 1, -1):
            graph[r1][c] = graph[r1][c - 1]
            min_val = min(min_val, graph[r1][c])

        graph[r1][c1 + 1] = temp

        return min_val

    ans = []
    for x1, y1, x2, y2 in queries:
        ans.append(rotate(x1, y1, x2, y2))
    return ans
