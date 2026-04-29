# 연속구간 : https://www.acmicpc.net/problem/2495 (python3)

for _ in range(3):
    s = input()
    cnt = 0
    temp = 0
    for i in range(1, 8):
        if s[i - 1] == s[i]:
            temp += 1
        else:
            temp = 0
        if temp > cnt:
            cnt = temp
    if cnt == 0:
        print(1)
    else:
        print(cnt + 1)
