# 좌표 정렬하기 2 : python3

# n = int(input())
# arr = []
# for i in range(n):
#     x, y = map(int, input().split())
#     arr.append((x, y))
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i][1] > arr[j][1]:
#             arr[i], arr[j] = arr[j], arr[i]
#         elif arr[i][1] == arr[j][1]:
#             if arr[i][0] > arr[j][0]:
#                 arr[i], arr[j] = arr[j], arr[i]
# for i in arr:
#     print(i[0], i[1])
#  시간초과 오류뜸

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key=lambda x: (x[1], x[0]))
for i in arr:
    print(i[0], i[1])
