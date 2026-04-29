n = int(input())
i = 0
while( n > i ) :
    i += 1
    testList = list(map(int, input().split()))
    if ( (testList[1] - testList[2]) > testList [0] ):
        print("advertise")
    elif( (testList[1] - testList[2]) == testList [0] ):
        print("does not matter")
    else:
        print("do not advertise")