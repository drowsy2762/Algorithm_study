# 중복 빼고 정렬하기 : https://www.acmicpc.net/problem/10867 (python3)

n = int(input())
num = list(map(int, input().split()))
result = []
for i in num:
    if i not in result:
        result.append(i)
result.sort()
for i in result:
    print(i, end=" ")
