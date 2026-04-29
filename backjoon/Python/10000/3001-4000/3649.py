# https://www.acmicpc.net/problem/3649
# 2026-01-31
import sys
input = sys.stdin.readline

while True:
    try:
        line = input()
        if not line: 
            break
            
        x = int(line) * 10000000 
        n = int(input())
        
        legos = []
        for _ in range(n):
            legos.append(int(input()))
            
        legos.sort()
        
        left = 0
        right = n - 1
        found = False
        
        while left < right:
            temp_sum = legos[left] + legos[right]
            
            if temp_sum == x:
                print(f"yes {legos[left]} {legos[right]}")
                found = True
                break
            elif temp_sum < x:
                left += 1
            else:
                right -= 1
                
        if not found:
            print("danger")
            
    except:
        break