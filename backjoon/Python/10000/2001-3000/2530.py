a, b, c = input().split()
d = int(input())
h = int(a)
m = int(b)
s = int(c) + d
while( s >= 60 ) :
    s -= 60
    m += 1
while( m >= 60 ) :
    m -= 60
    h += 1
while( h >= 24 ) :
    h -= 24
print( str(h) + ' ' + str(m) + ' ' + str(s) )