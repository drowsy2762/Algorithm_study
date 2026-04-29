sum = 0
a = []
for i in range(7):
    n = int(input())
    if (n%2 != 0):
        sum += n
        a.append(n)
if(sum == 0):
    print(-1)
else:
    print(sum)
    print(min(a))