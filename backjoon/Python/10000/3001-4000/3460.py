n = int(input())
for i in range(n):
    i = 0
    t = int(input())
    while(t >= 1):
        if(t%2 == 1):
            print(i, end=' ')
        i += 1
        t = t/2
        t = int(t)
    print('')