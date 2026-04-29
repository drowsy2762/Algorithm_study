# https://www.acmicpc.net/problem/17615 : 볼 모으기 (python3)
# 2023-11-22
from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
balls = str(input().rstrip())
cnt = []

rexplore = balls.rstrip("R")
cnt.append(rexplore.count("R"))

rexplore = balls.rstrip("B")
cnt.append(rexplore.count("B"))

rexplore = balls.lstrip("R")
cnt.append(rexplore.count("R"))

rexplore = balls.lstrip("B")
cnt.append(rexplore.count("B"))

print(min(cnt))
