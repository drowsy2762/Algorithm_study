while(1) :
    n = int(input())
    if(n == -1) :
        break
    a = []
    s = 0
    i = 1
    for i in range(1, n):
            if n % i == 0:
                a.append(i)
    if(n == sum(a)) :
        print(n,end=' = ')
        print(*a,sep=" + ")
    else :
        print(n,'is NOT perfect.')
    
