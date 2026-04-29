
i , j ,k = input().split()
a1 = int(i)
a2 = int(j)
a3 = int(k)

#순서정리 알고리즘
if( a2 > a1 ):
    a2 , a1 = a1, a2
if ( a3 > a1 ):
    a3, a1 = a1, a3
if ( a3 > a2):
    a3 , a2 = a2, a3

if ( a1 == a2 == a3):
    print(a1 * 1000 + 10000)
elif (a1 == a2 != a3 or a1 == a3 != a3 or a2 == a3 != a1 ):
    if( a1 == a2 ):
        print(1000 + a1*100)
    elif ( a2 == a3 ):
        print(1000 + a2 * 100)
    else:
        print(1000 + a3 * 100)
else:
    print( a1 * 100 )#