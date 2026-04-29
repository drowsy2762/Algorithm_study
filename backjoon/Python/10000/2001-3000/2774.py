# 아름다운 수 : https://www.acmicpc.net/problem/2774 (python3)


def b_v(x):
    a = [0] * 10
    cnt = 0
    while x >= 10:
        i = x % 10
        a[i] += 1
        x = int(x / 10)
    if x < 10:
        a[x] += 1
    for i in range(10):
        if a[i] > 0:
            cnt += 1
    print(cnt)


t = int(input())
for _ in range(t):
    x = int(input())
    b_v(x)
