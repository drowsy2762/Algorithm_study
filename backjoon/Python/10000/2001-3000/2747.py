n = int(input())
a = [0,1]
for i in range(1,n):
    k = a[i-1]+a[i]
    a.append(k)
print(a[n])