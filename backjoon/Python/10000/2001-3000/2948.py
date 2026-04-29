# 2009년 : https://www.acmicpc.net/problem/2948 (python3)

d, m = map(int, input().split())
dweeks = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
dmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dsum = 0
for i, dmonth in enumerate(dmonths):
    if i == m - 1:
        dsum += d
        break
    dsum += dmonth
print(dweeks[dsum % 7])
