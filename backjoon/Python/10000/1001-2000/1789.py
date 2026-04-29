n = int(input())
i = 0
s = 0
while( n >= s ) :
    i += 1
    s += i
if( s > n ) :
    i -= 1
print( i )
