n = int(input())
judgesVotes = str(input())
j = list(judgesVotes)
a = 0
b = 0
for i in j :
    if( i == 'A' ) :
        a += 1
    else :
        b += 1
if ( a > b ) :
    print('A')
elif( a == b ) :
    print('Tie')
else :
    print('B')