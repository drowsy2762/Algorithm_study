sum = 0
cnt = 0
max = 0
a = [0]*100
for i in range(10):
    n = int(input())    
    sum += n
    a[int(n/10)] += 1
for i in range(100):
    if(a[i] > cnt):
        max = i
        cnt = a[i]
print(int(sum/10))
print(max*10)