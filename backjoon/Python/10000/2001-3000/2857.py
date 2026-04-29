# FBI : https://www.acmicpc.net/problem/2857 (python3)

cnt = 0
for i in range(5):
    s = input()
    if s.find("FBI") >= 0:
        print(i + 1, end=" ")
        cnt += 1
if cnt > 0:
    print("")
else:
    print("HE GOT AWAY!")
