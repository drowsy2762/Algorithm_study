# 보물 : https://www.acmicpc.net/problem/1026 (python3)


def s(n, a, b):
    s = 0
    for _ in range(n):
        s += max(a) * min(b)
        a.remove(max(a))
        b.remove(min(b))
    return s


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(s(n, a, b))
