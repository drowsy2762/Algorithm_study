n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    a.sort()
    del a[4]
    del a[0]
    if(a[2] - a[0] >= 4):
        print("KIN")
    else:
        print(sum(a))