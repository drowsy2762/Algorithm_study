# https://www.acmicpc.net/problem/1946
# 2026-01-30
from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    tc = []
    for _ in range(n):
        document, interview = map(int, input().split())
        tc.append([document, interview])
    tc.sort(key =lambda x: (x[0]))
    document_ranking = 1e9
    interview_ranking = 1e9
    for dr, ir in tc:
        if dr < document_ranking or ir < interview_ranking:
            ans += 1
            document_ranking = min(document_ranking, dr)
            interview_ranking = min(interview_ranking, ir)
    print(ans)