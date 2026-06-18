# 2026-06-18


def solution(m, n, startX, startY, balls):
    answer = []

    for targetX, targetY in balls:
        candidates = []
        if not (startY == targetY and targetX < startX):
            dist = (startX - (-targetX)) ** 2 + (startY - targetY) ** 2
            candidates.append(dist)
        if not (startY == targetY and targetX > startX):
            dist = (startX - (2 * m - targetX)) ** 2 + (startY - targetY) ** 2
            candidates.append(dist)
        if not (startX == targetX and targetY < startY):
            dist = (startX - targetX) ** 2 + (startY - (-targetY)) ** 2
            candidates.append(dist)

        if not (startX == targetX and targetY > startY):
            dist = (startX - targetX) ** 2 + (startY - (2 * n - targetY)) ** 2
            candidates.append(dist)

        answer.append(min(candidates))

    return answer
