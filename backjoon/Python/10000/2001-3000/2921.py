#도미노
sum = 0
n = int(input())
for i in range(n+1) :
    for j in range(i+1) :
        sum += j + i

print(sum)
# 0(0) 1(0 1) 2(0 1 2) i(0 1 2)