# 2026-09-30

from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cache = deque()
    total_time = 0

    for city in cities:
        city_lower = city.lower()
        if city_lower in cache:
            total_time += 1
            cache.remove(city_lower)
            cache.append(city_lower)
        else:
            total_time += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city_lower)

    return total_time
