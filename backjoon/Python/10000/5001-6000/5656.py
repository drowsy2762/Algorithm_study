# 비교 연산자 : https://www.acmicpc.net/problem/5656 (python3)


def compare(a, b, op):
    if op == ">":
        return a > b
    elif op == ">=":
        return a >= b
    elif op == "<":
        return a < b
    elif op == "<=":
        return a <= b
    elif op == "==":
        return a == b
    elif op == "!=":
        return a != b


i = 1
while True:
    a, op, b = input().split()
    if op == "E":
        break
    print("Case %d: %s" % (i, str(compare(int(a), int(b), op)).lower()))
    i += 1
