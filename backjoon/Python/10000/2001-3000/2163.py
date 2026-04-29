import sys 

n = int(input()) 
s = 0 
for _ in range(n): 
    s += int(sys.stdin.readline()) 
print(s-n+1)