n = int(input())
m = [0] * n
for i in range(n) :
    a, b, c = map(int,input().split())
    if (a == b and b == c) :
        m[i] = 10000 + (a * 1000)
    elif (a == b) :
        m[i] = 1000 + (a * 100)
    elif (b == c) :
        m[i] = 1000 + (b * 100)
    elif (a == c) :
        m[i] = 1000 + (c * 100)
    else :
        m[i] = 100 * max(a,b,c)

s = m[0]

for i in range(n) :
    if(m[i] > s) :
        s = m[i]
print(s)