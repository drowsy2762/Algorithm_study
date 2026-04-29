max = 0
for i in range(5):
    sum = 0
    a = list(map(int,input().split()))
    for j in range(4):
        sum += a[j]
    if (sum>max):
        max = sum
        rank = i+1
print(rank,max)
