# Affine Cipher : https://www.acmicpc.net/problem/11575 (python3)


def E_x(a, b, x):
    print(chr((a * x + b) % 26 + 65), end="")


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = input()
    for i in range(len(s)):
        E_x(a, b, ord(s[i]) - 65)
    print("")
