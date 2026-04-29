# 피시방 알바 : https://www.acmicpc.net/problem/1453 (python3)

t = int(input())
com = input().split()
cn = [0] * 101
cnt = 0
for i in range(len(com)):
    com[i] = int(com[i])
for i in com:
    cn[i] += 1
for i in range(101):
    if cn[i] > 1:
        while cn[i] > 1:
            cnt += 1
            cn[i] -= 1
print(cnt)
