# A + B - 4 : python3

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
