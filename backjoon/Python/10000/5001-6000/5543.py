bug_cost = 2000
drink_cost = 2000
for _ in range(3) :
    n = int(input())
    if(bug_cost > n):
        bug_cost = n
for _ in range(2) :
    n = int(input())
    if(drink_cost > n):
        drink_cost=n
print(drink_cost+bug_cost-50)