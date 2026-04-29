n, k = map(int, input().split())
A = []
for i in range(n):
    A.append(int(input()))
cnt = 0
for i in reversed(range(n)):
    cnt += int(k / A[i])
    k = k % A[i]

print(cnt)
