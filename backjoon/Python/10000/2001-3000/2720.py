# 세탁소 사장 동혁 : https://www.acmicpc.net/problem/2720 (python3)

t = int(input())
for _ in range(t):
    q = 0
    d = 0
    n = 0
    p = 0
    c = int(input())
    while c >= 25:
        c -= 25
        q += 1
    while c >= 10:
        c -= 10
        d += 1
    while c >= 5:
        c -= 5
        n += 1
    while c >= 1:
        c -= 1
        p += 1
    print(q, d, n, p)
