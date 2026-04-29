t = int(input())
for i in range(t) :
    s = int(input())
    n = int(input())
    for j in range(n) :
        a, b = map(int,input().split())
        s += (a*b)
    print(s)