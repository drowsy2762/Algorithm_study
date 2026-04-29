n = int(input())
for _ in range(n) :
    candy, v = map(int,input().split())
    yours = candy / v
    dad = candy % v
    print(f"You get {int(yours)} piece(s) and your dad gets {dad} piece(s).")