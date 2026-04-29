from sys import stdin

# https://www.acmicpc.net/problem/2293 : 동전 1 (python3)
# 2024-03-31

input = stdin.readline


# dp 함수는 동전들의 배열과 목표 금액을 인자로 받아,
# 목표 금액을 만들 수 있는 동전의 조합의 수를 출력합니다.
def dp(coins, k):
    # dp 배열을 초기화합니다. dp[i]는 금액 i를 만들 수 있는 동전의 조합의 수를 저장합니다.
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1  # 금액 0을 만드는 방법은 동전을 사용하지 않는 한 가지 방법이 있습니다.
    for coin in coins:  # 각 동전에 대해
        for i in range(coin, k + 1):  # 동전의 값부터 목표 금액까지
            # 현재 금액(i)에서 동전의 값을 뺀 금액(i - coin)을 만드는 조합의 수를 더합니다.
            dp[i] += dp[i - coin]
    print(dp[k])  # 목표 금액을 만들 수 있는 동전의 조합의 수를 출력합니다.


# solution 함수는 문제의 입력을 받아 dp 함수를 호출합니다.
def solution():
    n, k = map(int, input().split())  # 동전의 종류의 수와 목표 금액을 입력받습니다.
    coins = []  # 동전들의 값을 저장할 배열을 초기화합니다.
    for _ in range(n):  # 각 동전에 대해
        coins.append(int(input()))  # 동전의 값을 입력받아 배열에 추가합니다.
    dp(
        coins, k
    )  # dp 함수를 호출하여 목표 금액을 만들 수 있는 동전의 조합의 수를 출력합니다.


solution()  # solution 함수를 호출하여 프로그램을 시작합니다.
