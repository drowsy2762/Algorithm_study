# 니모를 찾아서 : https://www.acmicpc.net/problem/10173 (python3)

while True:
    s = input()
    if s == "EOI":
        break
    s = s.lower()
    if s.find("nemo") > -1:
        print("Found")
    else:
        print("Missing")
