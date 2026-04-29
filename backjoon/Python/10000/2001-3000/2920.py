# 음계 : https://www.acmicpc.net/problem/2920 (python3)

asc_cnt = 0
des_cnt = 0
n = input().split()
for i in range(8):
    if i + 1 == int(n[i]):
        asc_cnt += 1
    elif 8 - i == int(n[i]):
        des_cnt += 1
if asc_cnt == 8:
    print("ascending")
elif des_cnt == 8:
    print("descending")
else:
    print("mixed")
