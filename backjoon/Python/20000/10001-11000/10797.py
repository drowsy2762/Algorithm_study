n = int(input())
a = list(map(int,input().split()))

c = 0
for i in range(5):
    if(a[i] == n):
        c += 1
print(c)