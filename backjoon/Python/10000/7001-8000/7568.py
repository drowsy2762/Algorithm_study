# 덩치 : https://www.acmicpc.net/problem/7568 (python3)

n = int(input())
weight = []
height = []
for _ in range(n):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)
for i in range(n):
    cnt = 1
    for j in range(n):
        if weight[i] < weight[j] and height[i] < height[j]:
            cnt += 1
    print(cnt, end=" ")
