# https://www.acmicpc.net/problem/23291
# 2026-02-27
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
fishbowls = list(map(int, input().split()))

dr = [0, 1]
dc = [1, 0]

def conditioning_fish(bowls):
    temp_bowls = [[0] * len(row) for row in bowls]

    for r in range(len(bowls)):
        for c in range(len(bowls[r])):
            for i in range(2):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < len(bowls) and 0 <= nc < len(bowls[nr]):
                    diff = abs(bowls[r][c] - bowls[nr][nc]) // 5
                    if diff > 0:
                        if bowls[r][c] > bowls[nr][nc]:
                            temp_bowls[r][c] -= diff
                            temp_bowls[nr][nc] += diff
                        else:
                            temp_bowls[r][c] += diff
                            temp_bowls[nr][nc] -= diff
    
    for r in range(len(bowls)):
        for c in range(len(bowls[r])):
            bowls[r][c] += temp_bowls[r][c]
            
    return bowls

def flatten_bowls(bowls):
    temp = []
    for c in range(len(bowls[-1])):
        for r in range(len(bowls) - 1, -1, -1):
            if c < len(bowls[r]):
                temp.append(bowls[r][c])
    return temp

ans = 0
while True:
    max_val, min_val = max(fishbowls), min(fishbowls)
    if max_val - min_val <= K:
        print(ans)
        break
    ans += 1
    
    for i in range(N):
        if fishbowls[i] == min_val:
            fishbowls[i] += 1

    bowls = [[fishbowls[0]], fishbowls[1:]]
    
    while len(bowls) <= len(bowls[-1]) - len(bowls[0]):
        w = len(bowls[0])
        left = [row[:w] for row in bowls]
        right = bowls[-1][w:]
        rotated_left = list(map(list, zip(*left[::-1])))
        bowls = rotated_left + [right]

    bowls = conditioning_fish(bowls)
    fishbowls = flatten_bowls(bowls)

    bowls = [fishbowls]
    for _ in range(2):
        half = len(bowls[0]) // 2
        left = [row[:half] for row in bowls]
        right = [row[half:] for row in bowls]
        rotated_left = [row[::-1] for row in left[::-1]] 
        bowls = rotated_left + right

    bowls = conditioning_fish(bowls)
    fishbowls = flatten_bowls(bowls)