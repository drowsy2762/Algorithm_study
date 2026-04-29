a = [0]*42
cnt = 0
for i in range(10) :
    n = int(input())
    k = n%42
    a[k] += 1
for j in range(42):
    if(a[j] > 0):
        cnt += 1
print(cnt)
