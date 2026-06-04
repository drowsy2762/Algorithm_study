# 2026-06-04


from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def solution(storage, requests):
    ans = 0
    n = len(storage)
    m = len(storage[0])
    padded_row = ["."] * (m + 2)
    new_storage = [padded_row]
    memo = set()

    for row in storage:
        new_storage.append(["."] + list(row) + ["."])
    new_storage.append(padded_row)
    storage = new_storage
    n += 2
    m += 2

    for request in requests:

        target = request[0]
        if len(request) > 1:
            if target in memo:
                continue
            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    if storage[i][j] == target:
                        storage[i][j] = "."
            memo.add(target)
        else:
            visited = [[False] * m for _ in range(n)]
            visited[0][0] = True
            q = deque([(0, 0)])
            tmp = []
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if not visited[nx][ny]:
                            if storage[nx][ny] == ".":
                                visited[nx][ny] = True
                                q.append((nx, ny))
                            elif storage[nx][ny] == target:
                                visited[nx][ny] = True
                                tmp.append([nx, ny])
            for x, y in tmp:
                storage[x][y] = "."

    print(storage)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if storage[i][j] != ".":
                ans += 1
    return ans
