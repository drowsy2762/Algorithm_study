n = int(input())
k = list(map(int,input().split()))
c = -1
score = 0
for i in range(n):
    if(k[i]==1):
        c+=1
        score = score + c + k[i]

    else:
        c = -1
print(score)