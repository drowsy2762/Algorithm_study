# https://www.acmicpc.net/problem/1283 : 단축키 지정 (python3)
# 2025-09-29
from sys import stdin
input = stdin.readline

n = int(input())
strings = [input().rstrip().split() for _ in range(n)]
skey = []

for string in strings:
    for i in range(len(string)):
        if string[i][0].lower() not in skey:
            skey.append(string[i][0].lower())

            string[i] = "[" + string[i][0] + "]" + string[i][1:]
            break
    else:
        for i in range(len(string)):
            found = False
            for j in range(1, len(string[i])):
                if string[i][j].lower() not in skey:
                    skey.append(string[i][j].lower())
                    found = True
                    string[i] = string[i][:j] + '[' + string[i][j] + ']' + string[i][j+1:]
                    break
            if found:
                break
            
for string in strings:
    print(' '.join(string))