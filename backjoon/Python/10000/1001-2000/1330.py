# https://www.acmicpc.net/problem/1330 : 두 수 비교하기 (python3)
# 2023-09-25

a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
