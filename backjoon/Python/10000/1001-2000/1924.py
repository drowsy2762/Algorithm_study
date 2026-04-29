# 2007년 : python3

x, y = map(int, input().split())
dweeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
dmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dsum = 0
for i, dmonth in enumerate(dmonths):
    if i == x - 1:
        dsum += y
        break
    dsum += dmonth
print(dweeks[dsum % 7 - 1])
