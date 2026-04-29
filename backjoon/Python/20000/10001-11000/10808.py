s = input()
spel = [0] * 26
for i in range(len(s)):
    spel[ord(s[i]) - 97] += 1
for i in range(26):
    print(spel[i], end=" ")
