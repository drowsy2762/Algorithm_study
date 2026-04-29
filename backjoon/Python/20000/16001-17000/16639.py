# https://www.acmicpc.net/problem/16639
# 2026-03-04
import sys
input = sys.stdin.readline

n = int(input())
expression = list(input().rstrip())
num = [int(expression[i]) for i in range(0, n, 2)]
ops = [expression[i] for i in range(1, n, 2)]

num_c = len(num)

max_dp = [[-float('inf')] * num_c for _ in range(num_c)]
min_dp = [[float('inf')] * num_c for _ in range(num_c)]

for i in range(num_c):
    max_dp[i][i] = num[i]
    min_dp[i][i] = num[i]

def calculate(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b

for step in range(1, num_c):         # 1. 간격
    for i in range(num_c - step):    # 2. 시작점
        j = i + step                 # 3. 끝점
        for k in range(i, j):        # 4. 식을 두 동강 낼 기준점 (연산자 인덱스와 동일)
            op = ops[k]
            
            # 가능한 모든 조합 계산
            candidates = [
                calculate(max_dp[i][k], max_dp[k+1][j], op),
                calculate(max_dp[i][k], min_dp[k+1][j], op),
                calculate(min_dp[i][k], max_dp[k+1][j], op),
                calculate(min_dp[i][k], min_dp[k+1][j], op)
            ]
            
            # 현재 구간 [i, j]의 최댓값과 최솟값 갱신
            max_dp[i][j] = max(max_dp[i][j], max(candidates))
            min_dp[i][j] = min(min_dp[i][j], min(candidates))
print(max_dp[0][num_c - 1])