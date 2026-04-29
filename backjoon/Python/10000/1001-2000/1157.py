s = input().lower()
s_l = list(set(s))
cnt = []

for i in s_l:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(s_l[cnt.index(max(cnt))].upper())
