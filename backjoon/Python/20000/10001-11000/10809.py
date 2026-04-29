s = input()
alphabet = [-1] * 26
s = list(s)

for i in range(len(s)):
    if alphabet[ord(s[i]) - 97] == -1:
        alphabet[ord(s[i]) - 97] = i
for i in range(26):
    print(alphabet[i], end=" ")
