# 과제 안 내신 분..? : https://www.acmicpc.net/problem/5597 (python3)

att = [0] * 30
for i in range(28):
    n = int(input())
    att[n - 1] += 1
for i in range(30):
    if att[i] == 0:
        print(i + 1)
