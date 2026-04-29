n = int(input())

for _ in range(n):
    a = list(input())
    i = 0  
    s = 0 
    for j in a:
        if j == 'O':
            i += 1
            s += i
        else :
            i = 0
    print(s)