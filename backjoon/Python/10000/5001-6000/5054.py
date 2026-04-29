n = int(input())
for i in range(n):
    k = int(input())
    a = list(map(int, input().split()))
    print((max(a)-min(a))*2)