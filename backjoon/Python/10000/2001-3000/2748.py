n = int(input())
j = 0
k = 1
t = 0
for i in range(n) :
    s = j + k
    j = k
    k = s
print(j)