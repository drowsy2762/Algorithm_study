from sys import stdin

input = stdin.readline

count = 0
save = []

def hanoi(n, source, helper, target):
    global count
    if n == 1:
        save.append((source,target))
        count += 1
    else :
        hanoi(n-1, source, target , helper)
        save.append((source,target))
        count += 1
        hanoi(n-1, helper, source, target)


def solution():
    global count
    n = int(input())
    hanoi(n,1,2,3)
    print(count)
    for x,y in save:
        print(x,y)

solution()