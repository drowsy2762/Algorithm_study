# 카드게임 : https://www.acmicpc.net/problem/10801 (python3)


def cardgame(a, b):
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1


a = list(map(int, input().split()))
b = list(map(int, input().split()))
w = 0
for i in range(10):
    w += cardgame(a[i], b[i])
if w > 0:
    print("A")
elif w < 0:
    print("B")
else:
    print("D")
