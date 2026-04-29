w = []
k = []
for i in range(10):
    w.append(int(input()))
for i in range(10):
    k.append(int(input()))
w.sort()
k.sort()
print(sum(w[7:]), sum(k[7:]))
