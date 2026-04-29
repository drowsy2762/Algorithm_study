# 알파벳 거리

n = int(input())
for i in range(n):
    a, b = input().split()
    print("Distances:", end=" ")
    for j in range(len(a)):
        if ord(a[j]) <= ord(b[j]):
            print(ord(b[j]) - ord(a[j]), end=" ")
        else:
            print(ord(b[j]) + 26 - ord(a[j]), end=" ")
    print()
