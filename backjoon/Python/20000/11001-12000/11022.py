t = int(input())
i = 0 
while(t > i) :
    i += 1
    a, b = input().split()
    print('Case #' + str(i) + ': ' + a + ' + ' + b + ' = ' + str(int(a)+int(b)))