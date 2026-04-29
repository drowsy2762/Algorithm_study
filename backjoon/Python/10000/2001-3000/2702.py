# 초6 수학 : https://www.acmicpc.net/problem/2702 (python3)


def lcm(x, y):
    return x * y // gcd(x, y)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))
