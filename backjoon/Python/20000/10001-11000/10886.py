n = int(input())
a = 0
b = 0
s = 0
while (n) :
    n -= 1
    t = int(input())
    if ( t == 1) :
        a += 1
    else :
        b += 1
if ( b > a ) :
    print('Junhee is not cute!')
else :
    print('Junhee is cute!')
    