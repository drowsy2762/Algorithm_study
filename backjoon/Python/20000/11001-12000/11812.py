# https://www.acmicpc.net/problem/11812
# 2026-04-13
import sys

def solution():
    input = sys.stdin.readline
    
    n, k, q = map(int, input().split())
    results = []
    
    for _ in range(q):
        x, y = map(int, input().split())
        if k == 1:
            results.append(str(abs(x - y)))
            continue
        
        dist = 0
        while x != y:
            if x > y:
                x = (x + k - 2) // k
            else:
                y = (y + k - 2) // k
            dist += 1
        
        results.append(str(dist))
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solution()