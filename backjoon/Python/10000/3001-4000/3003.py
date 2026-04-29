# 킹, 퀸, 룩, 비숏, 나이트, 폰 : https://www.acmicpc.net/problem/3003 (python3)
# Compare this snippet from Python/basic/151~200/3003.py: drowsy

s = input().split()
for i in range(6):
    s[i] = int(s[i])
print(1 - s[0], 1 - s[1], 2 - s[2], 2 - s[3], 2 - s[4], 8 - s[5])
