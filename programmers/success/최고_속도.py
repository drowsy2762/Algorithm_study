# 2026-11-06
import heapq
from collections import defaultdict


def solution(city, road):
    INF = float("inf")
    cities = [(x * 2, y * 2) for x, y in city]
    roads = []
    for x1, y1, x2, y2, limit in road:
        if x1 > x2 or y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        roads.append((x1 * 2, y1 * 2, x2 * 2, y2 * 2, limit))

    point_limit = defaultdict(lambda: INF)
    points_on_road = [set() for _ in range(len(roads))]

    for i, (x1, y1, x2, y2, limit) in enumerate(roads):
        points_on_road[i].add((x1, y1))
        points_on_road[i].add((x2, y2))
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        points_on_road[i].add((mid_x, mid_y))
        point_limit[(mid_x, mid_y)] = min(point_limit[(mid_x, mid_y)], limit)
        for cx, cy in cities:
            if x1 <= cx <= x2 and y1 <= cy <= y2:
                points_on_road[i].add((cx, cy))

    num_roads = len(roads)
    for i in range(num_roads):
        x1, y1, x2, y2, _ = roads[i]
        for j in range(i + 1, num_roads):
            x3, y3, x4, y4, _ = roads[j]
            ix1, iy1 = max(x1, x3), max(y1, y3)
            ix2, iy2 = min(x2, x4), min(y2, y4)
            if ix1 <= ix2 and iy1 <= iy2:
                points_on_road[i].add((ix1, iy1))
                points_on_road[j].add((ix1, iy1))
                points_on_road[i].add((ix2, iy2))
                points_on_road[j].add((ix2, iy2))

    graph = defaultdict(list)
    for i in range(num_roads):
        sorted_pts = sorted(points_on_road[i])
        for k in range(len(sorted_pts) - 1):
            u = sorted_pts[k]
            v = sorted_pts[k + 1]
            graph[u].append(v)
            graph[v].append(u)

    start_city = cities[0]
    max_speed = defaultdict(lambda: 0)
    max_speed[start_city] = INF
    pq = [(-INF, start_city)]

    while pq:
        neg_speed, curr_pt = heapq.heappop(pq)
        curr_speed = -neg_speed

        if curr_speed < max_speed[curr_pt]:
            continue

        for next_pt in graph[curr_pt]:
            next_speed = min(curr_speed, point_limit[next_pt])
            if next_speed > max_speed[next_pt]:
                max_speed[next_pt] = next_speed
                heapq.heappush(pq, (-next_speed, next_pt))

    answer = []
    for target_city in cities[1:]:
        res = max_speed[target_city]
        answer.append(0 if res == INF else res)

    return answer
