a = []
b = []
for i in range(8):
    n = int(input())
    a.append(n)
    b.append(n)
a.sort()
sum = 0
for i in range(7,3):
    sum += a[i]
print(sum)
for i in range(8):
    if(b[i]>=a[3]):
        print(i+1,end=' ')