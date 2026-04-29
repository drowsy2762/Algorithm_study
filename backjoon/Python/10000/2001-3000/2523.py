n = int(input())

for i in range(n*2-1) :
    if i < n :
        for j in range(i+1) :
            print('*',end='')
        print('')
    else :
        for j in range(n*2-i-1) :
            print('*',end='')
        print('')