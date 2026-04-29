n = int(input())
# dragon_curve = [list(map(int,input().split())) for _ in range(n)]
# graph = [[0] * 100 for _ in range(100)]

# def calculate(): # 최종적으로 네 꼭짓점이 모두 1인 정사각형의 개수
#     dragon_curve

# def dragon(x, y, direction, generation):
#     graph[x][y] = 1
#     q = deque()
#     q.append([x+dx[direction], y+dy[direction]])
#     cnt = 0
#     for i in range(1, generation+2):
#         cnt *= 2
#         while q:
#             nx, ny = q.popleft