a = []
break_point = 0
for i in range(9) :
    a.append(int(input()))
for i in range(9) :
    for j in range(9) :
        if(sum(a)-a[i]-a[j] == 100 and i != j):
            del a[j]
            del a[i]
            break_point += 1
            break;
    if(break_point == 1):
        break;
a.sort()
for i in range(7):
    print(a[i])
