max_people = 0
in_people = 0

for i in range(10):
    a, b=map(int,input().split())
    in_people += b - a
    if(in_people > max_people):
        max_people = in_people
print(max_people)