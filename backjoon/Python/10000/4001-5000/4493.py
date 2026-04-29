# 가위 바위 보? : https://www.acmicpc.net/problem/4493 (python3)


def rocksizpaper(a, b):
    if a == b:
        return 0
    elif a == "R" and b == "S":
        return 1
    elif a == "S" and b == "R":
        return -1
    elif a == "P" and b == "R":
        return 1
    elif a == "R" and b == "P":
        return -1
    elif a == "S" and b == "P":
        return 1
    elif a == "P" and b == "S":
        return -1


t = int(input())
for i in range(t):
    n = int(input())
    w = 0
    for j in range(n):
        p1, p2 = input().split()
        w += rocksizpaper(p1, p2)
    if w > 0:
        print("Player 1")
    elif w < 0:
        print("Player 2")
    else:
        print("TIE")
