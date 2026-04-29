# 파일 완전 삭제 : https://www.acmicpc.net/problem/9243 (python3)

n = int(input())
a = input()
b = input()
if n % 2 == 0:
    if a == b:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")
