t = int(input())
for _ in range(t):
    sum = 0
    min = 100
    a = list(map(int, input().split()))
    for i in range(7):
        if a[i] % 2 == 0:
            sum += a[i]
            if min > a[i]:
                min = a[i]
    print(sum, min)
