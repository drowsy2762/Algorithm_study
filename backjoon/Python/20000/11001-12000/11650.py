# 좌표 정렬하기 : python3

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()
for i in arr:
    print(i[0], i[1])
