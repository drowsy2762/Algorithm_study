# https://www.acmicpc.net/problem/5373
# 2026-01-20
from sys import stdin
input = stdin.readline

n = int(input())
cube = [[] for _ in range(6)]
for _ in range(3):
    cube[0].append(['r','r','r'])
    cube[1].append(['y','y','y'])
    cube[2].append(['w','w','w'])
    cube[3].append(['g','g','g'])
    cube[4].append(['b','b','b'])
    cube[5].append(['o','o','o'])

direction = {'U' : 2,
             'D' : 1,
             'F' : 0,
             'B' : 5,
             'L' : 3,
             'R' : 4}

"""
                  [2]
[0]               WWW
[1]               WWW
[2]               WWW
             [3]  [0]  [4]  [5]
[0]          GGG  RRR  BBB  OOO
[1]          GGG  RRR  BBB  OOO
[2]          GGG  RRR  BBB  OOO
                  [1]
[0]               YYY
[1]               YYY
[2]               YYY  
"""

def rotate_face(idx, clockwise):
    original = cube[idx]
    new_face = [['']*3 for _ in range(3)]
    
    for r in range(3):
        for c in range(3):
            if clockwise:
                new_face[c][2-r] = original[r][c]
            else:
                new_face[2-c][r] = original[r][c]
    
    cube[idx] = new_face

def rotate_cube(d, clockwise):
    face_idx = direction[d]
    rotate_face(face_idx, clockwise == '+')
    if d == 'U':
        if clockwise == '+':
            idx_list = [0, 4, 5, 3]    
            temp = cube[idx_list[0]][0][:]
            cube[idx_list[0]][0] = cube[idx_list[1]][0][:]
            cube[idx_list[1]][0] = cube[idx_list[2]][0][:]
            cube[idx_list[2]][0] = cube[idx_list[3]][0][:]
            cube[idx_list[3]][0] = temp
        else:
            idx_list = [0, 3, 5, 4]
            temp = cube[idx_list[0]][0][:]
            cube[idx_list[0]][0] = cube[idx_list[1]][0][:]
            cube[idx_list[1]][0] = cube[idx_list[2]][0][:]
            cube[idx_list[2]][0] = cube[idx_list[3]][0][:]
            cube[idx_list[3]][0] = temp
    elif d == 'D':
        if clockwise == '+':
            idx_list = [0, 3, 5, 4]
            temp = cube[idx_list[0]][2][:]
            cube[idx_list[0]][2] = cube[idx_list[1]][2][:]
            cube[idx_list[1]][2] = cube[idx_list[2]][2][:]
            cube[idx_list[2]][2] = cube[idx_list[3]][2][:]
            cube[idx_list[3]][2] = temp
        else:
            idx_list = [0, 4, 5, 3]
            temp = cube[idx_list[0]][2][:]
            cube[idx_list[0]][2] = cube[idx_list[1]][2][:]
            cube[idx_list[1]][2] = cube[idx_list[2]][2][:]
            cube[idx_list[2]][2] = cube[idx_list[3]][2][:]
            cube[idx_list[3]][2] = temp
    elif d == 'F':
        u_row = cube[2][2][:] 
        r_col = [cube[4][i][0] for i in range(3)]
        d_row = cube[1][0][:]
        l_col = [cube[3][i][2] for i in range(3)]

        if clockwise == '+':
            for i in range(3): cube[4][i][0] = u_row[i]
            cube[1][0] = r_col[::-1]
            for i in range(3): cube[3][i][2] = d_row[i]
            cube[2][2] = l_col[::-1]
        else:
            for i in range(3): cube[3][i][2] = u_row[2-i]
            cube[1][0] = l_col[:]
            for i in range(3): cube[4][i][0] = d_row[2-i]
            cube[2][2] = r_col[:]
    elif d == 'B':
        u_row = cube[2][0][:] 
        r_col = [cube[4][i][2] for i in range(3)]
        d_row = cube[1][2][:]
        l_col = [cube[3][i][0] for i in range(3)]

        if clockwise == '+':
            for i in range(3): cube[3][i][0] = u_row[2-i]
            cube[1][2] = l_col[:]
            for i in range(3): cube[4][i][2] = d_row[2-i]
            cube[2][0] = r_col[:]
        else:
            for i in range(3): cube[4][i][2] = u_row[i]
            cube[1][2] = r_col[::-1]
            for i in range(3): cube[3][i][0] = d_row[i]
            cube[2][0] = l_col[::-1]
    elif d == 'L':
        u_col = [cube[2][i][0] for i in range(3)]
        f_col = [cube[0][i][0] for i in range(3)]
        d_col = [cube[1][i][0] for i in range(3)]
        b_col = [cube[5][i][2] for i in range(3)]

        if clockwise == '+':
            for i in range(3): cube[0][i][0] = u_col[i]
            for i in range(3): cube[1][i][0] = f_col[i]
            for i in range(3): cube[5][i][2] = d_col[2-i]
            for i in range(3): cube[2][i][0] = b_col[2-i]
        else:
            for i in range(3): cube[5][i][2] = u_col[2-i]
            for i in range(3): cube[1][i][0] = b_col[2-i]
            for i in range(3): cube[0][i][0] = d_col[i]
            for i in range(3): cube[2][i][0] = f_col[i]
    elif d == 'R':
        u_col = [cube[2][i][2] for i in range(3)]
        f_col = [cube[0][i][2] for i in range(3)]
        d_col = [cube[1][i][2] for i in range(3)]
        b_col = [cube[5][i][0] for i in range(3)]

        if clockwise == '+':
            for i in range(3): cube[5][i][0] = u_col[2-i]
            for i in range(3): cube[1][i][2] = b_col[2-i]
            for i in range(3): cube[0][i][2] = d_col[i]
            for i in range(3): cube[2][i][2] = f_col[i]
        else:
            for i in range(3): cube[0][i][2] = u_col[i]
            for i in range(3): cube[1][i][2] = f_col[i]
            for i in range(3): cube[5][i][0] = d_col[2-i]
            for i in range(3): cube[2][i][2] = b_col[2-i]

def reset_cube():
    for i in range(3):
        cube[0][i] = ['r','r','r']
        cube[1][i] = ['y','y','y']
        cube[2][i] = ['w','w','w']
        cube[3][i] = ['g','g','g']
        cube[4][i] = ['b','b','b']
        cube[5][i] = ['o','o','o']

for _ in range(n):
    m = int(input())
    turn = list(input().rstrip().split())
    for i in range(m):
        rotate_cube(turn[i][0], turn[i][1])
    for i in range(3):
        print("".join(cube[2][i]))
    reset_cube()