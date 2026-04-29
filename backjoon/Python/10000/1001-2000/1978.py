n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n): 
    t = 0
    for j in range(a[i]):
        if(a[i]%(j+1) == 0):
            t += 1
    if(t == 2):
        count += 1
print(count)
    #소수 구하는 알고리즘 