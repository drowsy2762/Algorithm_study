# 배수 찾기 : https://www.acmicpc.net/problem/4504 (python3)

n = int(input())
while True:
    a = int(input())
    if a == 0:
        break
    if a % n == 0:
        print(a, "is a multiple of", n, end=".\n")
    else:
        print(a, "is NOT a multiple of", n, end=".\n")
