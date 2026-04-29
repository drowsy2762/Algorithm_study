# https://www.acmicpc.net/problem/2529
# 2026-01-28
import sys
input = sys.stdin.readline

k = int(input())
inequality = input().split()
visited = [False] * 10 # 0~9 사용 여부 체크
ans = []

def check(a, b, op):
    if op == '<':
        return a < b
    if op == '>':
        return a > b
    return True

def backtrack(depth, current_num_str):
    if depth == k + 1:
        ans.append(current_num_str)
        return

    for i in range(10):
        if not visited[i]: 
            
            if depth > 0:
                prev_num = int(current_num_str[-1])
                if not check(prev_num, i, inequality[depth-1]):
                    continue 

            visited[i] = True
            backtrack(depth + 1, current_num_str + str(i))
            visited[i] = False

backtrack(0, "")

print(ans[-1]) 
print(ans[0]) 