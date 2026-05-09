# 2026-05-09


def solution(n, s, a, b, fares):
    INF = float("inf")

    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_total_fare = INF

    for k in range(1, n + 1):
        current_fare = dist[s][k] + dist[k][a] + dist[k][b]

        if current_fare < min_total_fare:
            min_total_fare = current_fare

    return min_total_fare
