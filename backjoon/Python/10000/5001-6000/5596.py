# 시험점수 : https://www.acmicpc.net/problem/5596 (python3)

min_score = input().split()
man_score = input().split()
s1 = 0
s2 = 0
for i in range(4):
    s1 += int(min_score[i])
    s2 += int(man_score[i])
if s1 > s2:
    print(s1)
else:
    print(s2)
