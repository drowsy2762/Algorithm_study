# https://www.acmicpc.net/problem/20061
# 2026-02-12 
from sys import stdin
input = stdin.readline

blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

n = int(input())
# 블럭은 테트리스가 완성되었을 때 끝까지 이동하는 것이 아닌 한칸만 이동
# blocks의 원소는 t, x, y (x, y는 좌표) t=1 : 1x1, t=2 : 1x2, t=3 : 2x1
blocks = [list(map(int,input().split())) for _ in range(n)]

ans = 0

def move(t, x, y):
    if t == 1:
        c = 0

        while c < 5 and blue[x][c + 1] == 0:
            c += 1

        blue[x][c] = 1
        r = 0

        while r < 5 and green[r + 1][y] == 0:
            r += 1

        green[r][y] = 1

    elif t == 2:
        c = 0 

        while c < 4 and blue[x][c + 2] == 0:
            c += 1

        blue[x][c] = 1
        blue[x][c + 1] = 1
        r = 0

        while r < 5 and green[r + 1][y] == 0 and green[r + 1][y + 1] == 0:
            r += 1

        green[r][y] = 1
        green[r][y + 1] = 1

    elif t == 3:
        c = 0

        while c < 5 and blue[x][c + 1] == 0 and blue[x + 1][c + 1] == 0:
            c += 1

        blue[x][c] = 1
        blue[x + 1][c] = 1
        r = 0
        
        while r < 4 and green[r + 2][y] == 0:
            r += 1

        green[r + 1][y] = 1
        green[r][y] = 1

def clear():
    global ans
    j = 5
    while j >= 2:
        cnt = 0
        for i in range(4):
            if blue[i][j] == 1:
                cnt += 1
        
        if cnt == 4:
            ans += 1
            for i in range(4):
                blue[i].pop(j)
                blue[i].insert(0, 0)
            continue
            
        j -= 1

    i = 5
    while i >= 2:
        cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                cnt += 1
        
        if cnt == 4: 
            ans += 1
            green.pop(i)
            green.insert(0, [0, 0, 0, 0])
            continue
            
        i -= 1

def Max():
    push_cnt = 0
    
    for i in range(4):
        if blue[i][0] == 1:
            push_cnt = 2
            break
            
    if push_cnt == 0:
        for i in range(4):
            if blue[i][1] == 1:
                push_cnt = 1
                break
                
    for _ in range(push_cnt):
        for i in range(4):
            blue[i].pop()    
            blue[i].insert(0, 0)

    push_cnt = 0
    
    if sum(green[0]) > 0:
        push_cnt = 2
    elif sum(green[1]) > 0:
        push_cnt = 1
        
    for _ in range(push_cnt):
        green.pop() 
        green.insert(0, [0, 0, 0, 0])

def left():
    G, B = 0, 0
    for i in range(4):
        for j in range(2, 6):
            if blue[i][j] == 1:
                B += 1
    for i in range(2, 6):
        for j in range(4):
            if green[i][j] == 1:
                G += 1
    return G+B

def solution():
    for t, x, y in blocks:
        move(t, x, y)
        clear()
        Max()
    print(ans)
    print(left())

solution()  