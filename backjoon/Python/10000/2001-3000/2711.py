n = int(input())

for i in range(n):
    a, k = input().split()
    a = int(a)
    print(k[:a-1],k[a:],sep='')
