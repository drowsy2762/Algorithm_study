a, b = map(int,input().split())
if ( b > a ) :
    temp = a
    a = b
    b = temp
t = a*b
while(1) :
    if ( a % b == 0) :
        break;
    n = a % b
    a = b
    b = n
print(b)
print(int(t/b))