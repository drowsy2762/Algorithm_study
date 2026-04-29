# https://www.acmicpc.net/problem/2667 : 단지번호붙이기(python3)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]


def bfs(x, y):
    queue = [(x, y)]
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


a = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            a.append(bfs(i, j))
a.sort()
print(len(a))
for i in range(len(a)):
    print(a[i])
