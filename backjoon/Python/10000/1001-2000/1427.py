n = int(input())
a = []
while(n >= 1) :
    a.append(int(n)%10)
    n = int(n)/10
a.sort(reverse=True)
for i in range(len(a)):
    print(a[i],end='')