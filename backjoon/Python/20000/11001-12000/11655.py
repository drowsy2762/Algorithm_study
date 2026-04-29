# ROT13
s = input()
for i in s:
    if i.isupper():
        if ord(i) + 13 > 90:
            print(chr(ord(i) - 13), end="")
        else:
            print(chr(ord(i) + 13), end="")
    elif i.islower():
        if ord(i) + 13 > 122:
            print(chr(ord(i) - 13), end="")
        else:
            print(chr(ord(i) + 13), end="")
    else:
        print(i, end="")
