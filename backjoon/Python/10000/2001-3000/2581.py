n = int(input())
m = int(input())
sum = 0
c = 0
for i in range(n,m+1): 
    t = 0
    for j in range(2, i+1):
        if(i%j == 0):
            t += 1
    if(t==1):
        sum += i
        c += 1
        if(c==1):
            min = i
if(sum == 0):
    print(-1)
else:
    print(sum)
    print(min)