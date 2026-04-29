a = int(input())
b = int(input())
c = int(input())

x = a*b*c
a= [0]*10
while( x > 1 ):
    n = x%10
    x = int(x)/10
    a[int(n)] += 1
for i in range(10):
    print(a[i])