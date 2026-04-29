while( 1 ) :
    a, b = input().split()
    if( int(a) > int(b) ) :
        print('Yes')
    elif ( int(a) == 0 and int(b) == 0 ) :
        break
    else :
        print('No')
    