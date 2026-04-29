# https://www.acmicpc.net/problem/1244 : 스위치 켜고 끄기(python3)
# 2023-09-29
from sys import stdin

input = stdin.readline


def c_switch(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return 0


n = int(input())
switch = [-1] + list(map(int, input().split()))
student = int(input())
for i in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        for j in range(0, n + 1, num):
            c_switch(j)
    else:
        c_switch(num)
        for k in range(n // 2):
            if num + k > n or num - k < 1:
                break
            if switch[num + k] == switch[num - k]:
                c_switch(num + k)
                c_switch(num - k)
            else:
                break
for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print("")
