n = int(input())
remaning_apple = 0
for i in range(n) :
    student, apple = map(int, input().split())
    remaning_apple += apple % student
print(remaning_apple)