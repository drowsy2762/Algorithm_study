n = list(str(input()))
a = 0
for i in range(len(n)):
    if i == 0:
        a += 10
    elif n[i] == n[i-1]:
        a += 5
    else:
        a += 10 
print(a)
