i = 0
s = 0
while( 5 > i ) :
    a = int(input())
    if( a < 40 ) :
        s += 40
    else :
        s += a
    i += 1
print(int(s/5))
