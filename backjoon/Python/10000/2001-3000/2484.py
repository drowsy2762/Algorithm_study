# 주사위 네개 : https://www.acmicpc.net/problem/2484 (python3)


def check(a, b, c, d):
    if a == b == c == d:
        return 50000 + a * 5000
    elif a == b == c or a == b == d or a == c == d:
        return 10000 + a * 1000
    elif b == c == d:
        return 10000 + b * 1000
    elif a == b and c == d:
        return 2000 + a * 500 + c * 500
    elif a == c and b == d:
        return 2000 + a * 500 + b * 500
    elif a == d and b == c:
        return 2000 + a * 500 + b * 500
    elif a == b or a == c or a == d:
        return 1000 + a * 100
    elif b == c or b == d:
        return 1000 + b * 100
    elif c == d:
        return 1000 + c * 100
    else:
        return max(a, b, c, d) * 100


n = int(input())
max_p = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if check(a, b, c, d) > max_p:
        max_p = check(a, b, c, d)
print(max_p)
