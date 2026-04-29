# 파티가 끝나고 난 뒤 : https://www.acmicpc.net/problem/2845 (python3)

l, p = map(int, input().split())
n = input().split()
for i in range(5):
    print(int(n[i]) - l * p, end=" ")
