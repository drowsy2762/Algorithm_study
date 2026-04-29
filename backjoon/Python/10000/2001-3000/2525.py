a, b = input().split()
t = int(input())
h = int(a)
m = int(b) + t
while( m >= 60 ) :
    m -= 60
    h += 1
while( h >= 24 ) :
    h -= 24
print( str(h) + ' ' + str(m) )
