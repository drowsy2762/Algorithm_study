k = int(input())
data = []
for i in range(k):
    n = int(input())
    data.append(n)
    if(n == 0):
        data.pop()
        data.pop()
print(sum(data))