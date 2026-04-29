# 특별한 날 : https://www.acmicpc.net/problem/10768 (python3)

m = int(input())
d = int(input())

if m < 2:
    print("Before")
elif m == 2:
    if d < 18:
        print("Before")
    elif d == 18:
        print("Special")
    else:
        print("After")
else:
    print("After")
