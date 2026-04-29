# https://www.acmicpc.net/problem/1747 : 소수&팰린드롬 (python3)
# 2023-06-19 11:49
from sys import stdin

# input runtime 최적화
input = stdin.readline

n = int(input())
# 1은 소수가 아니므로 2부터 시작
if n == 1:
    n = 2
while 1:
    # 소수인지 확인
    isPrime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            isPrime = False
            break
    # 소수이면서 팰린드롬인지 확인
    if isPrime:
        if str(n) == str(n)[::-1]:
            print(n)
            break
    n += 1
