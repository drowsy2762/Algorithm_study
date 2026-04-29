a = []
for i in range(9):
    n = int(input())
    a.append(n)
    if(max(a) == n):
        cnt = i+1
print(max(a))
print(cnt)