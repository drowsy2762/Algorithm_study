# 별찍기 - 17 : https://www.acmicpc.net/problem/10992 (python3)

n = int(input())
for i in range(n - 1):
    for j in range(n - i - 1):
        print(" ", end="")
    if i > 0:
        print("*", end="")
    for j in range(i * 2 - 1):
        print(" ", end="")
    if i >= 0:
        print("*", end="")
    print("")
for i in range(n * 2 - 1):
    print("*", end="")
