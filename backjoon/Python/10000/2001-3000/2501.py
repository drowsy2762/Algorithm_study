n, k = map(int,input().split())
a = [0]
for i in range(1,n+1):
    if(n%i == 0):
        a.append(i)
try: 
    print(a[k])
except:
    print(0)