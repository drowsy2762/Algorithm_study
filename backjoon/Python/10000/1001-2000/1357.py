def Rev(a):
    a = str(a)
    return int(a[::-1])


x, y = map(int, input().split())
print(Rev(Rev(x) + Rev(y)))
