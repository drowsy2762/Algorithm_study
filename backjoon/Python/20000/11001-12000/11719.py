# 그대로 출력하기 2 : python3

while True:
    try:
        print(input())
    except EOFError:
        break
